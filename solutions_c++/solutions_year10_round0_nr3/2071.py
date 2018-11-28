#ifndef __GNUC__
#include "stdafx.h"
#endif 

#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
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
   int i,j,jj;
   long long int k,kk,T,N,R;
   cin >> T;
   string s;
   getline(cin,s);

   FOR(i,1,T+1)
   {
      cin >> R >> k >> N;
 //   cout << R << " runs of up to " << k << " people from " 
 //        << N << " groups " << endl;
      kk=N;
      vector<long long int> v;
      
      while(kk--)
      {
        long long int tmp=-1;
        cin>> tmp;
        if (tmp!=-1) v.push_back(tmp);
      }
      queue<long long int> q, q_rol;
      long long int Eur=0, people=0;
      FOR(j,0,v.size()) { people+= v[j]; q.push(v[j]); }

      if (people< k) 
      {
         Eur=people*R;
         cout << "Case #" << i << ": " << Eur << endl;     
         continue;
      }

      FOR(j,0,R)
      {
        people=0;
//      cout << " Run " << j << " : ";
        while(people+q.front()<=k)
        {
           people+=q.front();
//         cout << q.front() << " " ;
           q_rol.push(q.front());
           q.pop();
        }
//      cout << "\n with " << people << " people " << endl;
        Eur+=people;
        while(!q_rol.empty()) 
        {
           q.push(q_rol.front());
           q_rol.pop();
        } 
//     cout <<" Q size " << q.size() << " Q-rol size " << q_rol.size() << endl;
      }
      cout << "Case #" << i << ": " << Eur << endl;     
//       cout << v << endl;

   }
}
