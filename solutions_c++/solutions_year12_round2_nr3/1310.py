#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<sstream>
using namespace std;
#define INF 2000000000
#define INFLL (1LL<<62)
#define SS ({int x;scanf("%d", &x);x;})
#define SSL ({LL x;scanf("%lld", &x);x;})
#define rep(i,n) for(int i=0;i<(n);i++)
#define rept(i,m,n) for(int i=(m);i<(n);i++)
#define ull unsigned long long
#define lint long long
#define MX 10000001

int main()
{
	int i,j,k,l,n,m,t;
	t=SS;
	for(k=1;k<=t;++k)
	{
		n=SS;
		int a[n];
		for(i=0;i<n;++i)
			cin>>a[i];
		printf("Case #%d:\n",k);
		
		map<int,int> done;
		int bi=-1,bj=-1;
		
		for(i=0;i<(1<<n);++i)
		{
			int csum=0;
			for(j=0;j<n;++j)
			{
				if(i&(1<<j))
					csum+=a[j];
			}
			if(done[csum])
			{
				bi=done[csum]-1;
				bj=i;
				break;	
			}
			else
			{
				done[csum]=i+1;
			}
		}
		if(bi==-1)
		{
			printf("Impossible");
		}
		else
		{
			for(j=0;j<n;++j)
			{
				if(bi&(1<<j))
					printf("%d ",a[j]);
			}
			printf("\n");
			for(j=0;j<n;++j)
			{
				if(bj&(1<<j))
					printf("%d ",a[j]);
			}
		}
		printf("\n");
	}	
	return 0;
}
