#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;

typedef long long ll;
typedef complex<double> pt;

bool check(map<int, int> mm, int len)
{
  map<int, int> nn;
  while(mm.size()>0){
    if (mm.begin()->second==0){
      mm.erase(mm.begin());
      continue;
    }

    int fst = mm.begin()->first;
    for (int i=0; i<len; i++){
      if (mm[fst+i]==0){
        if (nn[fst+i]==0)
          return false;
        nn[fst+i]--;
      }
      else{
        mm[fst+i]--;
      }
    }
    fst+=len;
    while(mm[fst]>0){
      mm[fst]--;
      nn[fst]++;
      fst++;
    }
  }
  return true;
}

int main(int argc, char *argv[])
{
  int cases; cin>>cases;
  for (int cn=1; cn<=cases; cn++){
    int n; cin>>n;
    map<int, int> mm;
    for (int i=0; i<n; i++){
      int t; cin>>t;
      mm[t]++;
    }

    int l = 0, u = n+1;
    while(u-l>1){
      int m = (l+u)/2;
      if (check(mm, m))
        l = m;
      else
        u = m;
    }

    cout<<"Case #"<<cn<<": "<<l<<endl;
  }
  
  return 0;
}

