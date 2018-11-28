#include <iostream>
#include <cstdio>
#define see(x) cerr << " LINE " << __LINE__ << " : " << #x << " : " << x << endl
using namespace std;
int v[1005];
int cha(int x,int y)
{
	int z = 0;
	for(int i = 0;i < 30;i++)
		z = z | (((x >> i)^ (y >> i)) << i);
	return z;
}
void solve()
{
	int n;
	scanf("%d",&n);
	for(int i = 0;i < n;i++)
		scanf("%d",&v[i]);
	int res = 0,ans1,ans2,temp1,temp2;
	for(int i = 1;i < (1 << n) - 1;i++)
	{
		ans1 = ans2 = temp1 = temp2 = 0;
		for(int j = 0;j < n;j++)
		{
			if((i >> j) & 1)
			{
				temp1 = cha(temp1,v[j]);
				ans1 += v[j];
			}
			else
			{
				temp2 = cha(temp2,v[j]);
				ans2 += v[j];
			}
		}
		//see(temp1);
		//see(temp2);
		if(temp1 == temp2)
			res = max(res,max(ans1,ans2));
	}
	if(res == 0)
		printf("NO\n");
	else
		printf("%d\n",res);
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i = 1;i <= t;i++)
	{
		printf("Case #%d: ",i);
		solve();
		/*int x,y;
		scanf("%d %d",&x,&y);
		cout << cha(x,y) << endl;*/
	}
}
