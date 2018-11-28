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
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define fornm(i,n,m) for (int i=n; i<=(int)(m); i++)
#define forn(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)

int dx[]={1,1,0,-1},dy[]={0,1,1,1};
#define MAXIMO 2000000

int dig=1;
int Res[MAXIMO];

int saca( int64 n, int64 m)
{
    int cont=0,tmp;
    int64 newn,front,back,npow=1,mpow=1;
    tmp=dig;
    set<int64> vR;
    vR.clear();
    while(tmp>1)
    {tmp--;mpow*=10;}
    fornm(i,1,dig-1)
    {
      npow*=10;
      front=n%npow;
      back=n/npow;
      if(front==0){ mpow/=10;continue;}
      newn=front*mpow+back;
      mpow/=10;
      
      if(newn > n && newn<=m)
         vR.insert(newn);
    }
    return vR.size();
}
int main()
{
//	freopen("C-small-attempt0.in", "r", stdin);	freopen("respuestaS.out", "w", stdout);	
	freopen("C-large.in", "r", stdin);	freopen("respuestaL.out", "w", stdout);

    int T,cont;
	int64 A,B,tmp;
    cin>>T;
    fornm(tc,1,T)
    {
      cin >> A >> B;
      tmp=A;
      cont=0;
      dig=1;
      while(tmp>9)
      { tmp/=10;dig++;}
      
      for(int64 n=A;n<=B;n++)             
        cont += saca(n,B);
    
    	// print cases
      cout<<"Case #"<<tc<<": "<<cont<<endl;
     }
     return 0;
}
