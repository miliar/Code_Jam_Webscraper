#include<iostream>
using namespace std;
int max1(int a,int b)
{
	return a>b?a:b;
}
int min1(int a,int b)
{
	return a<b?a:b;
}
int main()
{
	int t;
	int g = 1;

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		int oft,bft;
		int op,bp;
		op = bp = 1;
		oft = bft = 0;
		int n;
		int i;
		scanf("%d",&n);
		int ans = 0;
		for( i = 0 ; i < n ; i ++)
		{
			char ch[2];
			int p;
			scanf("%s%d",ch,&p);
			if(ch[0] == 'O')
			{
				int l = abs(p-op);
				int k = min1(oft,l);
				oft = 0;
				l -= k;
				l ++;
				if(l > 0)
				{
					ans += l;
					bft += l;
				}
				op = p;
			}
			else
			{
				int l = abs(p-bp);
				int k = min1(bft,l);
				bft = 0;
				l-=k;
				l ++;
				if( l > 0)
				{
					ans += l;
					oft += l;
				}
				bp = p;
			}
		}
		printf("Case #%d: %d\n",g++,ans);
	}
	return 0;
}