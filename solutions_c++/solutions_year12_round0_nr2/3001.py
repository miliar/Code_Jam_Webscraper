#include <algorithm>
#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;

#define zero(a) memset(a,0,sizeof(a))
#define one(a) memset(a,1,sizeof(a))
#define fone(a) memset(a,-1,sizeof(a))

int main()
{
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	int T,TT=1;
	scanf("%d",&T);
	while(T--)
	{
		int n,s,p,t;
		int sum=0;
		scanf("%d%d%d",&n,&s,&p);
		while(n--)
		{
			scanf("%d",&t);
			if(p==1)
			{
				if(t>0)
					sum++;
				continue;
			}
			if(t>3*(p-1))
				sum++;
			else if(s>0&&t>3*p-5)
				sum++,s--;
		}
		printf("Case #%d: %d\n",TT++,sum);
	}
	return 0;
}