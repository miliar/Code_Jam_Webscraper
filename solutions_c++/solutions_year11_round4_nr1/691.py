//A

#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

#define s first
#define l second
#define LD long double

int main()
{
	//files
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	//vars
	int t,T;
	int X,S,R,N;
	int a,b,c;
	LD K,ans,len;
	pair <int,int> fast[1005];	//speed boost, length
	//testcase loop
	scanf("%d",&T);
		for (t=1; t<=T; t++)
		{
			//input
			scanf("%d%d%d%Lf%d",&X,&S,&R,&K,&N);
				for (a=0; a<N; a++)
				{
					scanf("%d%d%d",&b,&c,&fast[a].s);
					fast[a].l=c-b;
					X-=fast[a].l;
				}
			fast[N].s=0;
			fast[N++].l=X;
			//sort walkways by speed
			sort(fast,fast+N);
			//greedy
			ans=0;
				for (a=0; a<N; a++)
					if (K==0)	//don't run
						ans+=(LD)fast[a].l/(fast[a].s+S);
					else
					if ((LD)fast[a].l/(fast[a].s+R)<=K)	//run for the whole thing
					{
						ans+=(LD)fast[a].l/(fast[a].s+R);
						K-=(LD)fast[a].l/(fast[a].s+R);
					}
					else
					{
						len=K*(fast[a].s+R);
						ans+=(LD)len/(fast[a].s+R);
						len=fast[a].l-len;
						ans+=(LD)len/(fast[a].s+S);
						K=0;
					}
			//output
			printf("Case #%d: %Lf\n",t,ans);
		}
	return(0);
}