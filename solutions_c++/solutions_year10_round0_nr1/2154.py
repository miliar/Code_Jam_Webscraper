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
   unsigned i,j,jj,k,kk,T,N;
   cin >> T;
   string s;
   getline(cin,s);

   FOR(i,1,T+1)
   {
      cin >> N >> k;
/*
      getline(cin,s);
      stringstream ss(s);
      vector<int> v;
      
      while(ss)
      {
        int tmp=-1;
        ss >> tmp;
        if (tmp!=-1) v.push_back(tmp);
      }
*/
// //    cout << v << endl;
      
      if (N==1) kk=k%2;
      else
      {
          unsigned rem= k % (1<<N);
          kk= (rem+1 == (1<<N));
      }
/*
      if (k==0) kk=0;
      else
      {
         while( (N-1) && k) { k/=2; N--; }
         if (N==0) kk=0; else kk=k%2;
      }
*/
      

      cout << "Case #" << i << ": " << (kk ? "ON" : "OFF") << endl;     
   }
}
