#include <iostream>
#include <algorithm>
using namespace std;
struct wire
{
	int a,b;
}wires[1500];
bool cmp(wire x,wire y)
{
	return x.a > y.a;
}
int main()
{
	freopen("g1.in","r",stdin);
	freopen("g1.out","w",stdout);
	int t;
	scanf("%d",&t);
	int i,j;
	int k;
	int n;
	int ans;
	for (i = 1;i <= t;i++)
	{
		ans = 0;
		scanf("%d",&n);
		for (j =1;j <= n;j++)
			scanf("%d%d",&wires[j].a,&wires[j].b);
		sort(&wires[1],&wires[1+n],cmp);
		for (j = 1;j <= n;j++)
			for (k = j+1;k <= n;k++)
			{
				if (wires[k].b > wires[j].b)
					ans++;
			}
		printf("Case #%d: %d\n",i,ans);
	}
}