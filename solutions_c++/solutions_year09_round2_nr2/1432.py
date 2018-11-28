#include <iostream>
#include <vector>
#include <iterator>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <algorithm>
#include <ext/algorithm>
using namespace std;
using namespace __gnu_cxx;

int digits[10];
int digits1[10];

void printAr(int *p, int m)
{
   for(int i=0; i!=m; i++) cout << p[i] << " ";
   cout << endl;
}

#define FOR(i,begin,end) for((i)=(begin);(i)<(end);(i)++)


template<class T>
ostream& operator<<(ostream& o, const vector<T>& v)
{ 
// o << " * vector of size " << v.size() << ": < ";
// int i;
// FOR(i,0,v.size()) o << v[i] << " ";
   copy(v.begin(),v.end(),ostream_iterator<T>(o, ""));
// o << "> ";
   return o;
}

int main()
{
   int i,j,jj,k,kk,T,N;
   cin >> T;
   string s;
   getline(cin,s);

   FOR(i,1,T+1)
   {
      unsigned N;
      cin >> N;

      unsigned N1=N;
      FOR(j,0,10) digits[j]=0;
      while (N1)
      {
         digits[N1%10]++;
         N1/=10;
      }
//    printAr(&digits[0],10);

      N1=N;
      bool found=false;
      while(!found)
      {
        N1++;
        unsigned N2=N1;
        FOR(j,0,10) digits1[j]=0;
        while (N2)
        {
           digits1[N2%10]++;
           N2/=10;
        }
        found=true;
        FOR(j,1,10) {if (digits1[j]!=digits[j]) { found=false; break; } }
      }

      cout << "Case #" << i << ": " << " " << N1 << endl;
   }
}
