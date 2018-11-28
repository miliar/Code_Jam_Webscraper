#include<iostream>
#include<cstring>
#include<cstdlib>
#include<algorithm>
using namespace std;
const int MAXN=1050;

int a[MAXN],n;
bool used[MAXN];
int main()
{
	/*
	double p=0.130006;
	double ans=0,now=p;
	for (int i=1;i<=1000;i++)
	{
		ans += now * i;
		now *= (1 - p);
	}
	cout << ans << " " << 1/p << endl;
	*/
	int cases;
	scanf("%d",&cases);
	for (int tcase=1;tcase<=cases;tcase++)
	{
		scanf("%d",&n);
		double ans=0;
		for (int i=1;i<=n;i++) 
		{
			scanf("%d",&a[i]);
			ans += a[i]!=i;
		}
		
		printf("Case #%d: %.6f\n",tcase,ans);
	}
	return 0;
}
