#include<Cstdio>
#include<queue>
#include<vector>
#include<stack>
#include<algorithm>
#include<cmath>
#include<Cstring>
#include<string>
#include<memory>

using namespace std;

int n;
int a[100];

void input()
{
	char t[100];
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
	{
		scanf("%s",t+1);
		a[i]=0;
		for(int j=1;j<=n;j++)
		{
			if(t[j]=='1') a[i]=j;
		}
	}
}

int process()
{
	int cnt=0;
	for(int i=1;i<=n;i++)
	{
		int j;
		for(j=i;j<=n&&a[j]>i;j++);
		for(;j>i;j--)
		{
			swap(a[j],a[j-1]);
			cnt++;
		}
	}
	return cnt;
}

int main()
{
//	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		input();
		printf("Case #%d: %d\n",i+1,process());
	}
}