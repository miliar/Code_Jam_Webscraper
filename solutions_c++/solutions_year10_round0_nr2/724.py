#ifndef __GNUC__
#include "stdafx.h"
#endif 

#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <string.h>
#include <iterator>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <algorithm>

using namespace std;

/*
#ifdef __GNUC__
#include <ext/hash_map>
#include <ext/algorithm>
using namespace __gnu_cxx;
#else
using namespace stdext;
#endif
*/
  
struct eqstr
{
  bool operator()(const char* s1, const char* s2) const
  {
    return strcmp(s1, s2) == 0;
  }
};

/*
#ifdef __GNUC__
hash_map<const char*, int, hash<const char*>, eqstr> fHash;
#else 
hash_map<const char*, int> fHash;
#endif
*/

void printAr(int *p, int m)
{
   for(int i=0; i!=m; i++) cout << p[i] << " ";
   cout << endl;
}

#define FOR(i,begin,end) for((i)=(begin);(i)<(end);(i)++)

template<class T>
ostream& operator<<(ostream& o, const vector<T>& v)
{ 
   o << " * vector of size " << v.size() << ": < ";
// int i;
// FOR(i,0,v.size()) o << v[i] << " ";
   copy(v.begin(),v.end(),ostream_iterator<T>(o, " "));
   o << "> ";
   return o;
}


#ifdef __GNUC__
int main()
#else
int _tmain(int agrc, _TCHAR* argv[])
#endif
{
   int i,j,jj,k,kk,T,N;
   cin >> T;
   string s;
   getline(cin,s);

   FOR(i,1,T+1)
   {
      getline(cin,s);
      stringstream ss(s);
      vector<long long int> v,v1;
     
      ss >> N; 
      while(ss)
      {
        int tmp=-1;
        ss >> tmp;
        if (tmp!=-1) v.push_back(tmp);
      }
      cout << v << endl;
      long long minE= *min_element(v.begin(),v.end());
      long long maxE= *max_element(v.begin(),v.end());
      v1 = v;
      FOR(j,0,v1.size()) v1[j]-=minE;
//    cout << v1 << endl;
      long long gcd=-1;
      FOR(j,0,v1.size()) 
      {
         if (v1[j]==0) continue;
         if (gcd==-1) { gcd=v1[j]; continue; }
         long long a=v1[j], b=gcd;
         cout << "Computing GCD of " << a << " " << b << endl;
         while (a>1 && b>1) 
            if (a>b) a%=b; else b%=a;
         if (a==1 || b==1) { gcd=1;   continue; }
         if (a==0 || b==0) { gcd=a+b; continue; }
      }
      long long apocTime=(maxE/gcd)*gcd;
      if (apocTime<maxE) apocTime+=gcd;
//    cout << " GCD = " << gcd << "  Apoc time = " << apocTime << endl;
      cout << "Case #" << i << ": " << apocTime-maxE << endl;     
   }
}
