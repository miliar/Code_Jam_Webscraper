			  #include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
#define MAXN 55
int lc[MAXN];
int sp[MAXN];
int main()
{
	freopen("D:\\B-large.in","r",stdin);
	freopen("D:\\B.txt","w",stdout);
	int T;
	int cases=0;
	scanf("%d",&T);
	while(T-->0)
	{
		cases++;
		int n,k,b,t;
		scanf("%d %d %d %d",&n,&k,&b,&t);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&lc[i]);
		}
		for(int i=0;i<n;i++)
		{
			scanf("%d",&sp[i]);
		}
		int rc=0;
		int cc=	0;
		int swaps=0;
		for(int i=n-1;i>=0;i--)
		{
			if(lc[i]+sp[i]*t>=b)
			{
				rc++;
				swaps+=cc;
				if(rc>=k)
					break;
			}else   cc++;
			
		}
		if(rc>=k)
		{
			printf("Case #%d: %d\n",cases,swaps);
		}else printf("Case #%d: IMPOSSIBLE\n",cases);
	}


	return 0;
}