#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<cstdio>
#include <iomanip>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000

typedef __int64 LL;

typedef pair<LL,LL> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

#define inf 1000000000
#define MAXN 1000001
//typedef long long LL;


char flag[MAXN];
int primes[100000],sz;

void sieve()
{
	int i,j;
	for(i=3;i*i<MAXN;i+=2) 
		if(!flag[i]) for(j=i*i;j<MAXN;j+=2*i) flag[j]=1;
	primes[sz++]=2;
	for(i=3;i<MAXN;i+=2)  
		if(!flag[i]) primes[sz++]=i;
}

int gcd(int a,int b)
{
	if(b==0) return a;
	return gcd(b,a%b);
}

pi extended_gcd(LL a,LL b)
{
	pi ret;

    if (a % b ==0)
        return MP(0,1);
    else
		ret= extended_gcd(b,a% b);
	ret=MP(ret.second,ret.first-ret.second*(a/b));
   return ret;
}

int solveCong(int a,int b,int m)
{
	int g=gcd(a,m);
	pi now=extended_gcd(a,m);
	LL x=(LL)(b/g)*now.first;
	x%=m;if(x<0) x+=m;
	return x;
}

int main()
{
	int i,j,k,l,tests,cs=0,n,d;
	int vals[20];


	sieve();


	//freopen("D:\\gcj\\A-large.in","r",stdin);
	freopen("D:\\gcj\\A-large","w",stdout);

	scanf("%d",&tests);
	while(tests--)
	{
		scanf("%d%d",&d,&n);

		for(i=0;i<n;i++)
			scanf("%d",&vals[i]);

		printf("Case #%d: ",++cs);

		

		if(n<=2)
		{
			if(n==2 && vals[0]==vals[1])
				printf("%d\n",vals[0]);
			else
				puts("I don't know.");
			continue;
		}

	
		int ans=-1,flag=1;

		

		int pp=pow(10,d);
		for(i=0;i<sz && flag;i++)
		{
			if(primes[i]>pp) break;
			for(j=0;j<n;j++)
				if(vals[j]>=primes[i]) break;


			if(j<n) continue;

			
			int p=primes[i];
			int a=(vals[0]-vals[1])%p;
			int b=(vals[1]-vals[2])%p;


			if(a<0) a+=p;
			if(b<0) b+=p;

			if(n==2)
			{
				int A=1,B=(vals[1]-vals[0])%p;
				if(B<0) B+=p;
				int S=(vals[1]+B)%p;

			//	if(cs==31)
				//	printf("==%d %d %d\n",p,S,ans);
				if(ans!=-1 && S!=ans)
					flag=0;
				else
					ans=S;

				continue;
			}

			int g=gcd(a,p);

			if(b%g) continue;

			int A=solveCong(a,b,p);

			int B=(vals[1]-((LL)A*vals[0])%p)%p;
			if(B<0) B+=p;

			int ok=1;

			//printf("%d %d %d\n",p,A,B);

			for(j=1;j<=n && ok;j++)
			{
				LL S=(((LL)vals[j-1]*A)%p+B)%p;
				int s=S;

				if(j<n)
				{
					if(s!=vals[j]) ok=0;
				}
				else
				{
					if(ans!=-1 && S!=ans)
						flag=0;
					else
						ans=S;
				}
			}

		}
		if(flag==0)
			puts("I don't know.");
		else
			printf("%d\n",ans);
		
	}

	return 0;
} 


