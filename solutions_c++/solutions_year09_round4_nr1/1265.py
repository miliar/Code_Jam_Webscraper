#include <iostream>
#include <iomanip>
#include <list>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <cctype>
#include <sstream>
#include <cassert>

using namespace std;

typedef pair<pair<int,int>, int> triple;

triple make_triple(int a, int b, int c) {
  return make_pair(make_pair(a,b),c);
}

int first(triple x) {
  return x.first.first;
}
int second(triple x) {
  return x.first.second;
}
int third(triple x) {
  return x.second;
}

int matrix[41][41];

bool good_matrix(int M, int *perm) {
  for (int i=0;i<M;i++) {
    for (int j=i+1;j<M;j++) {
      if (matrix[perm[i]][j]==1) return false;
    }
  }
  return true;
}
int count_swaps(int M, int *perm) {
  int temp[M];
  for (int i=0;i<M;i++) {
    temp[i]=perm[i];
  }
  bool done = false;
  int count = 0;
  while (!done) {
    done = true;
    for (int i=0;i<M-1;i++) {
      
      if (temp[i]>temp[i+1]) {swap(temp[i],temp[i+1]); count++; done =false;}
    }
  }
  return count;
}



int main() {

  int N;
  cin >> N;
  
  int M;

  for (int i10=0;i10<N;i10++) {
    cin >> M;
    //cout << M << endl;
    for (int j=0;j<M;j++) {
      for (int k=0;k<M;k++) {
	char c;
	cin >> c;
	if (c=='0') matrix[j][k]=0;
	if (c=='1') matrix[j][k]=1;
      }
    }
    int perm[M];
    for (int i=0;i<M;i++) {
      perm[i] = i;
    }
    int min = M*M;
    do {
      if (good_matrix(M,perm)) {
	int c = count_swaps(M,perm);
        if (c<min) min =c;
      }
    } while (next_permutation(perm,perm+M));
    
    cout << "Case #"<<(i10+1) <<": " << min << endl;
  }

}
