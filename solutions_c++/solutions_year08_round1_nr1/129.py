#include<iostream>
using namespace std;
int a[100];
int b[100];
int d[100];
int Min;
const int inf=1000000000;
int m;
void solve(int t)
{
	if(t==m)
	{
		int sum=0;
		for(int i=0;i<m;i++)
			sum+=a[i]*b[d[i]];
		if(sum<Min)
			Min=sum;
	}
	else
	{
		for(int i=t;i<m;i++)
		{
			swap(d[i],d[t]);
			solve(t+1);
			swap(d[i],d[t]);
		}
	}
}
int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int zu;
	scanf("%d",&zu);
	int g=1;
	while(zu--)
	{
		Min=inf;
		scanf("%d",&m);
		int i;
		for(i=0;i<m;i++)
			scanf("%d",a+i);
		for(i=0;i<m;i++)
			scanf("%d",b+i);
		for(i=0;i<m;i++)
			d[i]=i;
		solve(0);
		printf("Case #%d: %d\n",g++,Min);
	}
}