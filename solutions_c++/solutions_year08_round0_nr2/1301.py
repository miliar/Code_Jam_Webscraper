#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

#define MAX 10000
int fA[MAX], fB[MAX], nA, nB;
vector< pair<string,string> > A, B;
string tmp1, tmp2;
int i,j,n,m;
int T;
ifstream fin("train.in");
ofstream fout("train.out");

void add(int *arr, int pos, int amm) {
  int i;
  for (i=pos;i<MAX;i++)
    arr[i] += amm;
}

int hash(string input) {
  int ret(0);
  ret = ((input[0]-'0')*10+(input[1]-'0'))*60 + (input[3]-'0')*10+input[4]-'0';
  return ret;
}

bool sorter(const pair<string,string> &a, const pair<string, string> &b) {
  if (a.first != b.first) return a.first < b.first;
  return a.second < b.second;
}

int main() {
  int TEST, nTEST;
  fin >> nTEST;
  for (TEST = 0; TEST < nTEST; TEST++ ) {
  fin >> T;
  fin >> n >> m;
  A.resize(0); B.resize(0);
  for (i=0;i<n;i++) {
    fin >> tmp1 >> tmp2;
    A.push_back( make_pair(tmp1,tmp2) );
  }
  for (i=0;i<m;i++) {
    fin >> tmp1 >> tmp2;
    B.push_back( make_pair(tmp1,tmp2) );
  }
  fill (fA,fA+MAX,0); fill(fB,fB+MAX,0);
  sort(A.begin(),A.end(),sorter); sort(B.begin(),B.end(),sorter);
 
  int solA(0), solB(0);
  for (i=0;i<MAX && !(A.empty() && B.empty());i++) {
  
    while (!A.empty() && hash(A[0].first) == i) {
      if (!fA[i]) solA++;
      else add(fA,i,-1);
      add(fB,hash(A[0].second)+T,1);
      A.erase(A.begin());
    }
    while (!B.empty() && hash(B[0].first) == i) {
      if (!fB[i]) solB++;
      else add(fB,i,-1);
      add(fA,hash(B[0].second)+T,1);
      B.erase(B.begin());
    }
  }
  fout << "Case #" << TEST + 1 << ": " << solA << " " << solB << endl;
  }
  system("pause");
}
