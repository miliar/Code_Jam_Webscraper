#include <iostream>
#include <cstdio>
#include <set>
#include <algorithm>
#define M 2<<11
using namespace std;
int P,n;
struct datas
{
	int pt;
	int num;
};
datas mt[M];
int ck[M];
int sum[M];
int price[M];
bool cmp(datas a,datas b)
{
	return a.num<b.num;
}
int Count()
{
	int i,cnt=0;
	for (i=0;i<n;i++)
		if (mt[i].num) return 1;
	return 0;
}
int main()
{
	int i,j,k,T,cases=0;
	freopen("D:\\B-small-attempt2.in","r",stdin);
	freopen("D:\\B-small-attempt2.out","w",stdout);
	scanf("%d",&T);
	while (T--)
	{
		memset(ck,0,sizeof(ck));
		memset(mt,0,sizeof(mt));
		memset(sum,0,sizeof(sum));
		cases++;
		scanf("%d",&P);
		n=(1<<P);
		int t,tt=1,temp=1<<P;
		while (temp)
		{
			sum[tt]=sum[tt-1]+temp;
			tt++;
			temp/=2;
		}
		for (i=0;i<n;i++)
		{
			scanf("%d",&mt[i].num);
			mt[i].num=P-mt[i].num;
			mt[i].pt=i;
		}
		for(i = 0; i < P; i++)
		{
			tt = 1 << (P- 1 - i);
			for(int j = 0; j < tt; j++)  
				scanf("%d", &t);
		}
		tt=n;
		int ans=0;
		while (Count())
		{
			int tmp=n/tt;
			for (i=0;i<tmp;i++)
			{
				bool check=0;
				for(int j=i*tt;j<(i + 1)*tt; j++)
				{
					if(mt[j].num)
					{
						mt[j].num--;
						check = 1;
					}
				}
				if(check)  ans++;
			}
			tt>>=1;
		}
		printf("Case #%d: %d\n",cases,ans);
	}
	return 0;
}
