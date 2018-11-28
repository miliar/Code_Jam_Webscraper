#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl

int A,B,tests,ans;
int a[11];

void work(int x)
{
	int xx = x, y;
	a[0] = 0;
	while (xx)
	{
		a[++a[0]] = xx % 10;
		xx /= 10;
	}
	for (int st=a[0]-1;st;st--) if (a[st]>0)
	{
		y = 0;
		for (int i=0;i<a[0];i++)
			y = y * 10 + a[(st-i+a[0]-1)%a[0]+1];
		if (x==y) return;
		if (x<y && y<=B)
		{
			ans++;
			//printf("%d %d\n",x,y);
		}
	}
}

int main()
{
	freopen("c2.in","r",stdin);
	freopen("c2.out","w",stdout);
	scanf("%d",&tests);
	for (int test=1;test<=tests;test++)
	{
		scanf("%d%d",&A,&B);
		ans = 0;
		for (int i=A;i<=B;i++)
		{
			work(i);
		}
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}
