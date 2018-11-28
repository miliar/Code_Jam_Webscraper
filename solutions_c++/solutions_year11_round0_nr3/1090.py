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
#define MAXIMO 10000000
int Num[21],Numtmp[21];
void Binary(unsigned long long n);
int main()
{
//	freopen("C-small-attempt0.in", "r", stdin);
//	freopen("respuestaS.out", "w", stdout);
	
	freopen("C-large.in", "r", stdin);
	freopen("respuestaL.out", "w", stdout);

	int i, j, tc,T,N,b;
	unsigned long long C,sumD,sum,min;

	cin >>T;
	
	FORnm(tc,1,T)
	{
		forn(i,21)Num[i]=0;
		sum=0;sumD=0;min=MAXIMO;;
		cin >> N;		
		forn(i,N)
		{	    
	    forn(k,21)Numtmp[k]=0;
		  cin >> C;	
			sum+=C;
			min<?=C;			 
		  Binary(C);
		  forn(j,21)Num[j]=(Num[j]+Numtmp[j])%2;
		}
		forn(i,21)sumD+=Num[i];
		// print cases
		if(sumD != 0)
				cout<<"Case #"<<tc<<": NO"<<endl;
		else
		    cout<<"Case #"<<tc<<": "<<sum-min<<endl;
	}
	return 0;
}

void Binary(unsigned long long n)
{
 	int pos=0;	 
  while(n>0)
		{
	     Numtmp[pos++]=n%2;
	     n/=2;
		}	
}
