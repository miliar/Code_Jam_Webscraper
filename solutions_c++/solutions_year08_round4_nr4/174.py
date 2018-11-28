#include<iostream>
using namespace std;
char a[10000];
char b[10000];
int m;
int Min=1000000;
int c[100];
void solve(int t)
{
	if(t==m)
	{
		int i;
		for(i=0;a[i];i+=m)
		{
			for(int j=0;j<m;j++)
				b[i+j]=a[i+c[j]];
		}
		b[i]=0;
		int pre=-1;
		int num=0;
		for(i=0;b[i];i++)
		{
			if(b[i]==pre)continue;
			pre=b[i];
			num++;
		}
		if(Min>num)
			Min=num;
	}
	else
	{
		for(int i=t;i<m;i++)
		{
			swap(c[i],c[t]);
			solve(t+1);
			swap(c[i],c[t]);
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
		scanf("%d",&m);
		scanf("%s",a);
		Min=1000000;
		for(int i=0;i<m;i++)
			c[i]=i;
		solve(0);
		printf("Case #%d: %d\n",g++,Min);
	}

}
