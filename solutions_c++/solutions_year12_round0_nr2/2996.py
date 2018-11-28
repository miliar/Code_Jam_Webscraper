#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;
int mm[105];
int cmp(int a,int b)
{
	return a>b;
}
int main ()
{
	freopen("in2.in","r",stdin);
	freopen("out.out","w",stdout);
	int T;
	int n,s,p;
	int ans;
	int cnt;
	cnt = 0;
	scanf("%d",&T);
	while (T--)
	{
		++cnt;
		ans = 0;
		scanf("%d%d%d",&n,&s,&p);
		for(int i=0;i<n;++i)
		{
			scanf("%d",&mm[i]);
		}
		sort(mm,mm+n,cmp);
		for(int i=0;i<n;i++)
		{
			if((mm[i]+2)/3 >= p)
			{
				ans++;
			}
			else
			{
				if(s == 0)break;
				--s;
				if(mm[i] >= 2 &&(mm[i]+4)/3 >= p)ans++;
			}
		}
		printf("Case #%d: %d\n",cnt,ans);
	}
}