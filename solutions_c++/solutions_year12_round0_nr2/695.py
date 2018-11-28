#include<cstdio>
#include <cctype>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include <deque>
#include <math.h>
#include<stdio.h>
#include<memory.h>
using namespace std;


typedef stringstream ss;
typedef vector<string> vs;
typedef vector<int> vi;
typedef long long int64;

#define PI 3.14159265
#define pb push_back
#define ALL(t) t.begin(),t.end()
#define fornm(i,n,m) for (int i=n; i<=(int)(m); i++)
#define forn(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)

int dx[]={1,1,0,-1},dy[]={0,1,1,1};
#define MAXIMO 10000
int main()
{
//	freopen("B-small-attempt4.in", "r", stdin);	freopen("respuestaS.txt", "w+", stdout);

	freopen("B-large.in", "r", stdin);	freopen("respuestaL.out", "w+", stdout);

	
    int T,cont;
    int N,S,p,t;
    double val;
    int maxi;
    vi vT;    
    cin>>T;
    fornm(tc,1,T)
    {
       vT.clear();
       cont=0;
       cin >> N >> S >> p ;
       forn(i,N)
       {
          cin >> t;
          vT.pb(t);      
       }   
       
       forn(i,vT.size())
       {
          double v=double(vT[i])/3;
          (v-floor(v)<0.5)? val=floor(v):val=ceil(v);
          if(val < vT[i]-2*val)
            maxi= vT[i]-2*val;
          else
            maxi = val;
          
          if(maxi>=p){cont++;continue;}
          if(maxi==0)continue;
          if(vT[i]==1)
             {if(1>=p){cont++;continue;}}            
          if(S>0)
          {
             if(3*val>= vT[i])
             if(maxi+1 >= p)
             {
               cont++;
               S--;
             }
          }
                    
       }
         	// print cases
		printf("Case #%d: %d\n", tc,cont);

	}
	return 0;
}

