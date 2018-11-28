#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<algorithm>
#include<iostream>
#define MAX_N 111
#define INF 2100000000
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int z, n, s, p, res, t;
	scanf("%d",&z);
	for(int o=1; o<=z; o++)
	{
		res=0;
		scanf("%d%d%d",&n, &s, &p);
		for(int i=0; i<n; i++)
		{
			scanf("%d",&t);
			if(t==0)
			{
				if(p<=0) res++;
			}
			else if(t==1)
			{
				if(p<=1) res++;
			}
			else if(t==2)
			{
				if(p<=1) res++;
				else if(p<=2 && s>0)
				{
					res++;
					s--;
				}
			}
			else if(t%3==0)
			{
				if(t/3>=p)
					res++;
				else if(t/3+1>=p && s>0)
				{
					res++;
					s--;
				}
			}
			else if(t%3==1)
			{
				if(t/3+1>=p)
					res++;
			}
			else
			{
				if(t/3+1>=p)
					res++;
				else if(t/3+2>=p && s>0)
				{
					res++;
					s--;
				}
			}
		}
		printf("Case #%d: %d\n",o,res);
	}
}
