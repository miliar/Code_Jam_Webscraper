#pragma warning (disable : 4786)

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>

using namespace std;

#define min(a,b) ((a) < (b) ? (a) : (b))
#define max(a,b) ((a) > (b) ? (a) : (b))

#define CLR(a) memset(a,0,sizeof(a))

int cases,caseno;

int A,B,P,deg[1001],sv[1001][1001],L[1001],len;

#define PrimeLIMIT 2000

unsigned int prime[PrimeLIMIT],pr[1000],prlen;

#define gP(n) (prime[n>>6]&(1<<((n>>1)&31)))
#define rP(n) (prime[n>>6]&=~(1<<((n>>1)&31)))

void sieve()
{
	unsigned int i,j,sqrtN,i2;

	memset( prime, -1, sizeof( prime ) );
	sqrtN = (unsigned int)sqrt(( double )PrimeLIMIT) + 1;
	pr[prlen++]=2;
	for(i=3;i<sqrtN;i+=2) if(gP(i))
	{
		i2=i<<1;
		for(j=i*i;j<PrimeLIMIT;j+=i2) rP(j);
	}
	for(i=3;i<PrimeLIMIT;i+=2) if(gP(i)) pr[prlen++]=i;
}

void input()
{
	scanf("%d %d %d",&A,&B,&P);
}

int parent[1001],Count[1001];

int findParent(int i)
{
	if(i==parent[i]) return i;
	parent[i]=findParent(parent[i]);
	return parent[i];
}

void process()
{
	int res=0,i,j,k,xx,yy;

	CLR(Count);
	for(i=0;pr[i]<1000;i++)
	{
		parent[pr[i]]=pr[i];
	}
	for(i=0;pr[i]<1000;i++)
	{
		if(pr[i] < P) continue;
		for(j=1;;j++)
		{
			if(pr[i]*j > B) break;
			if(pr[i]*j < A) continue;
			Count[pr[i]]++;
		}
	}
	for(i=0;pr[i]<=1000;i++)
	{
		if(pr[i] < P) continue;
		for(j=i+1;pr[i]*pr[j]<=1000;j++)
		{
			for(k=1;;k++)
			{
				if(pr[i]*pr[j]*k > B) break;
				if(pr[i]*pr[j]*k < A) continue;

				xx=findParent(pr[i]);
				yy=findParent(pr[j]);
				if(xx<yy)
				{
					parent[yy]=xx;
					Count[xx]+=Count[yy];
				}
				else if(xx>yy)
				{
					parent[xx]=yy;
					Count[yy]+=Count[xx];
				}
				break;
			}
		}
	}
	k=0;
	CLR(deg);
	len=0;
	for(i=0;pr[i]<=B;i++)
	{
		if(pr[i]<P) continue;
		xx=findParent(pr[i]);
		if(!deg[xx]) L[len++]=xx;
		sv[xx][deg[xx]++]=pr[i];
	}
	bool flag;
	res=0;
	CLR(Count);
	for(i=A;i<=B;i++)
	{
		flag=false;

		for(j=0;j<len;j++)
		{
			xx=L[j];
			for(k=0;k<deg[xx];k++)
			{
				if(i%sv[xx][k]==0)
				{
					flag=true;
					break;
				}
			}
			if(flag)
			{
				Count[xx]=1;
				break;
			}
		}
		if(!flag) res++;
	}
	for(i=0;pr[i]<=B;i++) res+=Count[pr[i]];
	printf("Case #%d: %d\n",++caseno,res);
}

int main()
{
	freopen("Inputs\\fk.txt","r",stdin);
	freopen("Inputs\\B1.txt","w",stdout);

	sieve();
	scanf("%d",&cases);
	while(cases--)
	{
		input();
		process();
	}
	return 0;
}