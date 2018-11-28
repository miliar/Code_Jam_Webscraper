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
#define FORnm(i,n,m) for (int i=n; i<=(int)(m); i++)
#define forn(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)

int dx[]={1,1,0,-1},dy[]={0,1,1,1};
#define MAXIMO 10000

#define Small
//#define Large

vi F;
int main()
{

	freopen("C-small-attempt0.in", "r", stdin);	freopen("respuestaS_C.out", "w+", stdout);
//	freopen("C-large.in", "r", stdin);	freopen("respuestaL.out", "w+", stdout);


	int i, j, tc,m,n,b,cnt,T,N,L,H;
	cin >>T;	
	
	FORnm(tc,1,T)
	{
	
	F.clear();
	 cin >> N >>L >>H ;
	 forn(i,N)
	 {cin >> n;
	   F.pb(n);
		 }
		int min=-1; 
	bool posible=false;
	 FORnm(j,L,H)
	 {
     int cont=0;
	 	  forn(i,N)
	 	  {
			 		if (j%F[i]==0 || F[i]%j==0) 		 
			 		  cont++;
						
		  }
		  if(cont==N)
			{
			 					 min=j;
			 					 posible= true;
									 break;
			}
		}
	   
  if(posible)
		cout<<"Case #"<<tc<<": "<<min<<endl;
		else
		  cout<<"Case #"<<tc<<": NO"<<endl;
	   
		 }
	return 0;
}
