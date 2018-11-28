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
     map<char, int> mp;
    
    char str[1024];
    fscanf(fp, "%s", str);
    string cs(str);
    int index = 1;
    for(int j = 0; j < cs.size(); ++j) {
      map<char, int>::iterator itx = mp.find(cs[j]);
      if(itx == mp.end()) {
          mp[cs[j]] = index++;
      }
    }
    int base = mp.size();
    if(base == 1)
      base = 2;
    int num = 0;
    int cur = 1;
    int len = cs.size()-1;
    for(int k = 0; k < cs.size(); ++k) {
      int dgt = 0;
      map<char, int>::iterator itx = mp.find(cs[k]);
       if(itx->second == 2) 
         continue;
       if(itx->second == 1) 
         dgt = 1;
       if(itx->second > 2) 
         dgt = itx->second-1;
       num += dgt*pow((double)base, (double)len-k); 
    }
    cout << "Case #" << i << ": " << num << endl;
  }

  fclose(fp);
  return 1;
}
