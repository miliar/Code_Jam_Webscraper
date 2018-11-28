#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <deque>
#include <algorithm>
#include <memory.h>
#include <complex>
#include <ctime>
using namespace std;


typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
typedef vector<pair<int,PII> > VIII;
typedef vector<string> VS;
typedef complex<double> base;
const double pi=3.1415926535897932384626433832795;
const double eps=1e-9;

#define pb push_back
#define mp make_pair
#define sz size()
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define FOR(i,a,b) for(int i=(a),_b(b); i<_b; ++i)
#define RFOR(i,a,b) for(int i=(a)-1,_b(b); i>=_b; --i)
#define CLR(a,v) memset((a),(v),sizeof(a))
#define CPY(a,b) memcpy((a),(b),sizeof(a))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) ((a)<(0)?-(a):(a))
#define HAS(x,k) ((x).find(k)!=(x).end())
#define sqr(a) ((a)*(a))
//#pragma comment(linker,"/STACK:200000000")

#define PREV(x) ((x)&((x)-1))
#define NEXT(x) (((x)<<1) - PREV(x))

char ch[1<<20];
string gs(){scanf("%s",ch); return string(ch);}
string gl(){gets(ch); return string(ch);}
LL gcd(LL a, LL b) {return (!a)?b:gcd(b%a,a);}

LL powmod(LL a, LL n, LL mod)
{
	LL r=1;
	while(n)
	{
		if (n&1) r=(r*a)%mod;
		a=(a*a)%mod;
		n>>=1;
	}
	return r;
}
LL inv(LL x, LL p)
{
	return powmod(x,p-2,p);
}




int er[1<<20];
int pr[1<<20],pn=0; 
int X[100],N,K;
int st[]={1,10,100,1000,10000,100000,1000000};

LL solve()
{
	LL mx=X[0]; FOR(i,1,N) mx=MAX(mx,X[i]);

	if (N==1)
	{
		return -1;
	}
	else
	{
		LL val=-1;
		int bb=lower_bound(pr,pr+pn,mx+1)-pr;
		FOR(i,0,pn) if (pr[i]>st[K]) break; else
		if (pr[i]>mx)
		{
			LL p=pr[i];
			if (X[0]==0)
			{
				LL S=0;
				LL B=X[1];
				if (N==2)
					if (X[0]==X[1]) return X[0];
					else return -1;
				else
				{
					LL A=((LL)X[2]-B+p)%p;
					A=(A*inv(B,p))%p;
					LL g=((LL)X[N-1]*A+B)%p;
					int ok=1; FOR(i,0,N-1) if (((LL)X[i]*A+B)%p!=(LL)X[i+1]) ok=0;
					if (ok)
						if (g!=val && val!=-1) return -1;
						else val=g;
				}
			}else
			{
				LL S=X[0];
				if (N==2)
					if (X[0]==X[1]) return X[0];
					else return -1;
				LL A=((LL)X[1]-(LL)X[2]+p)%p;
				A=(A*inv( (S-(LL)X[1]+p)%p ,p ))%p;
				LL B=((LL)X[1]-A*S)%p; B+=p; B%=p;
				LL g=((LL)X[N-1]*A+B)%p;
				int ok=1; FOR(i,0,N-1) if (((LL)X[i]*A+B)%p!=(LL)X[i+1]) ok=0;
				if (ok)
					if (g!=val && val!=-1) return -1;
					else val=g;
			}
		}
			return val;
	}
}

LL brut()
{
	LL res=-1;
	LL mx=X[0]; FOR(i,1,N) mx=MAX(mx,X[i]);
	int bb=lower_bound(pr,pr+pn,mx+1)-pr;
	FOR(i,bb,pn) if (pr[i]>st[K]) break; else
		if (pr[i]>mx)
	{
		LL p=pr[i];
		for(LL A=0; A<p; ++A)
			for(LL B=0; B<p; ++B)
		{
			int ok=1;
			FOR(i,0,N-1) if ((X[i]*A+B)%p!=X[i+1]){ok=0; break;}
			if (ok)
			{
				LL g=X[N-1]*A+B; g%=p;
				if (res!=-1 && res!=g) return -1;
				res=g;
			}
		}
	}
	return res;
}

void gen()
{
	N=1+rand()%10;
	K=3;
	int x=rand()%pn;
	while(pr[x]>=st[K])
		x=rand()%pn;
	LL p=pr[x];
	LL S=rand()%p;
	LL A=rand()%p;
	LL B=rand()%p;
	X[0]=S;
	FOR(i,1,N) X[i]=(X[i-1]*A+B)%p;
}

int main()
{
	CLR(er,0);
	FOR(i,2,1<<20)
		if (!er[i])
		{
			pr[pn++]=i;
			for(int j=i+i; j<1<<20; j+=i) er[j]=1;
		}
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	/*
	FOR(tt,0,1000)
	{
		gen();
		LL a=solve();
		LL b=brut();
		if (a!=b)
		{
			printf("\n%d %d\n",K,N);
			FOR(i,0,N) printf("%d ",X[i]+1);
			printf("\n");
			exit(0);
		}else printf("ok");
	}
	exit(0);
	//*/

	int t; cin >> t;
	int tn=0; 
	while(t--)
	{
		++tn;
		printf("Case #%d: ",tn);
		fprintf(stderr,"Case #%d: ",tn);
		
		scanf("%d%d",&K,&N); K=6;
		FOR(i,0,N)scanf("%d",X+i);
		//if (K>3) {printf("\n");continue;}
		LL next=solve();
		if (next==-1) 
			printf("I don't know.\n");
		else printf("%d\n",(int)next);

		//LL next2=brut();
		//if (next2==-1) printf("         I don't know.\n");
		//else printf("          %d\n",(int)next2);
	}
	
	return 0;
}