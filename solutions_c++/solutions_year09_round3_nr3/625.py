#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <list>
#include <vector>
#include <stack>
#include <cmath>
using namespace std;

#define MAX_ARRAY_SIZE 1000000
#define __MYMIN LLONG_MIN 
#define __MYMAX LLONG_MAX

void print(int* p, int n)
{
  for(int i = 0; i < n; ++i) 
    cout << p[i] << " ";
  cout << endl;
}

template <class T> void swap(T& t1, T& t2)
{
  T temp = t1;
  t1 = t2;
  t2 = temp;
  return;
}

int cal(int index, vector<bool>& p)
{
  p[index] = 0;
  int count = 0;
  int j = index+1;
  while(p[j]) {
    if(j >= p.size())
      break;
    count++;
    ++j;
  }
  j = index-1;
  while(p[j]) {
    if(j < 0)
      break;
    count++;
    --j;
  }
  return count;
}

int release(vector<int> v, vector<bool>& p)
{
  int b = 0;
  for(int i = 0; i < v.size(); ++i) {
    b += cal(v[i], p);
  }
  return b;
}

int main(int argc, char *argv[])
{
  if(argc != 2) {
    cout << "Usage: a.out test_file>" << endl;
    exit (-1);
  }

  FILE* fp = fopen(argv[1], "r");

  int N;
  fscanf(fp, "%d", &N);

  for(int i = 1; i <= N; ++i) {
    int P, Q;
    fscanf(fp, "%d", &P);
    fscanf(fp, "%d", &Q);
    vector<int> vc;
    int min_diff = LLONG_MAX;
    int index = -1;
    for(int j = 0; j < Q; ++j) {
      int x;
      fscanf(fp, "%d", &x);
      vc.push_back(x-1);
    }
    long min_bribe = LLONG_MAX;
    do {
      vector<bool> vp;
      for(int ll = 0; ll < P; ++ll)
        vp.push_back(true);
      int bribe = release(vc, vp);
      if(bribe < min_bribe)
        min_bribe = bribe;
     } while ( next_permutation (vc.begin(), vc.end()) );
  
     cout << "Case #" << i << ": " <<  min_bribe << endl;
  }

  fclose(fp);
  return 1;
}
