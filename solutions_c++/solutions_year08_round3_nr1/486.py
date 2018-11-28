/*#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
*/

#include <cmath>
#include <stdio.h>
#include <conio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <limits.h>
#include <string.h>
#include <list>
using namespace std;

#define ll long long

#define FOR(v,f) for(ll (v)=0;(v)<(f);(v)++)
#define FORS(v,f,s) for(ll (v)=0;(v)<(f);(v)=(v)+s)
#define FORI(type,cont,var) for ( type::iterator (var)=(cont).begin(); (var)!=(cont).end(); ++(var))

#define DEBUG               




template <typename T> inline int minOf(T *min, T i)
{
       if (i<*min) *min = i;
       return (i<*min);
}

template <typename T> inline int maxOf(T *max, T i)
{
       if (i>*max) *max = i;
       return (i<*max);
}

void test(int n)
{ 
         #ifdef DEBUG               
        //cout << "---- control " << n << " ----------" << endl;

        //cout << "    : " <<  << endl;

        //FOR (i, ) cout << 
        
        #endif
}
 


int main(void)
{
   int N;
   
   string filename = "A-large";
   string infilepath =  "c:\\GJam\\Round1C\\Problem A\\" + filename + ".in";
   string outfilepath = "c:\\GJam\\Round1C\\Problem A\\" + filename + ".out";
   
   freopen(infilepath.c_str(), "rt", stdin);
   freopen(outfilepath.c_str(), "wt", stdout);

   
   long fr[1010];
   
   cin >> N;

   FOR(n,N)
   {       
        ll nkp = 0;
        int P, K, L; 
        
        cin >> P >> K >> L;
        FOR(i,L) cin >> fr[i];  
        
        int end = 0;
        int kc=0, pc=0, lc=L; 
        
        while(!end)
        {
              
              long max=0;
              int imax=0;

              //cout << endl << endl;
              //cout << "vect: ";
             // FOR(i,lc) cout << fr[i] << " ";  
              //cout << endl;

              FOR(i,lc) 
                  if (fr[i]>max)
                  {
                     max = fr[i];
                     imax = i;
                     //cout << imax << " " << max;  
                  }
              
              nkp += fr[imax] * (pc+1);
              
              if (imax!=lc-1) fr[imax] = fr[lc-1];
              lc--;

              //cout << endl;
              //cout << imax << " -> " << fr[imax] << "(";
              //cout << nkp << ") ";
              
              kc++; 
              if (kc==K) 
              {  kc=0;
                 pc++;   
                 if (pc==P)
                 {
                    end=1;
                 }
              }
              
              if(lc==0) end=1;    
        }
   
   
        if (lc==0) cout << "Case #" << n+1 << ": " << nkp << endl;
        else cout << "Case #" << n+1 << ": Impossible" << endl;
   
   
   
         //cout << "Case #" << n+1 << ": ";
         //cout       << endl;
         

   }

   return 0;
}       
   
   
   
