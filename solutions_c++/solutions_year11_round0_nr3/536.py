#include<iostream>
#include<fstream>
#include<algorithm>
#include<cstring>
using namespace std;

void init();
void solve();
void print();
const int inf=10000000;
int n,minnow,sum,ans;
int data[1001];
bool flag;

int main()
{
	freopen("candy.in","r",stdin);
	freopen("candy.out","w",stdout);
	
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
	memset(data,0,sizeof(data));
	scanf("%d", &n);
	minnow=inf; sum=0;
	for(int i=0; i<n; i++)
	{
		scanf("%d", &data[i]);
		minnow=min(minnow,data[i]);
		sum+=data[i];
	}
}

void solve()
{
	flag=0;
	int tmp=data[0];
	for(int i=1; i<n; i++)
		tmp^=data[i];
	if(tmp)
	{
		flag=1; return;
	}
	ans=sum-minnow;
}

void print()
{
	if(flag) printf("NO\n");
	else printf("%d\n", ans);	
}
