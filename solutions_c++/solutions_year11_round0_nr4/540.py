#include<iostream>
#include<fstream>
using namespace std;

void init();
void solve();
void print();
int a[1001];
int n,ans;

int main()
{
	freopen("sort.in","r",stdin);
	freopen("sort.out","w",stdout);
	
	int tt;
	scanf("%d", &tt);
	for(int i=0; i<tt; i++)
	{
		init();
		solve();
		printf("Case #%d: ", i+1);
		print();
	}
	
	return 0;	
}

void init()
{
	scanf("%d", &n);
	for(int i=1; i<=n; i++)
		scanf("%d", &a[i]);
}

void solve()
{
	ans=0;
	for(int i=1; i<=n; i++)
		ans+=a[i]!=i;
}

void print()
{
	printf("%d.000000\n", ans);
}
