#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdio>
#include<iomanip>
#include<map>
#include<set>
#include<vector>
#include<list>
#include<deque>
#include<cstdlib>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

const int N=510;
const int mod=100003;

int ans[N],n;
int rec[N];
int rk[N];

void update()
{
	int i,p=n;
	for(i=1;i<=n;i++)
		rk[i]=rk[i-1]+rec[i];
	if(rec[n]==0)
		return ;
	while(1)
	{
		if(rk[p]==1)
		{
			ans[n]++;
			break;
		}
		if(rec[rk[p]])
			p=rk[p];
		else
			break;
	}
}

void dfs(int dep)
{
	if(dep>n)
	{
		update();
		return ;
	}
	rec[dep]=1;
	dfs(dep+1);
	rec[dep]=0;
	dfs(dep+1);
}

void init()
{
	memset(ans,0,sizeof(ans));
	for(n=2;n<=25;n++)
		dfs(2);
}

int main()
{
	freopen("t1.in","r",stdin);
	freopen("t1.out","w",stdout);
	int i,tests,n;
	cin>>tests;
	memset(ans,0,sizeof(ans));
	init();
	for(i=1;i<=tests;i++)
	{
		cout<<"Case #"<<i<<": ";
		cin>>n;
		cout<<ans[n]%mod<<endl;
	}
return 0;
}