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

const int N=55;

int n,m,end,tim;
int loc[N],vv[N],st[N];

void myin()
{
	int i;
	cin>>n>>m>>end>>tim;
	for(i=1;i<=n;i++)
		cin>>loc[i];
	for(i=1;i<=n;i++)
		cin>>vv[i];
}

int calc(int id)
{
	int len=end-loc[id];
	return len%vv[id]==0?len/vv[id]:len/vv[id]+1;
}

void work()
{
	int i,j,cnt,ans=0;
	for(i=1;i<=n;i++)
		st[i]=calc(i);
	cnt=0;
	for(i=n;i>=1;i--)
	{
		if(st[i]<=tim)
			cnt++;
		if(cnt>=m)
			break;
	}
	if(i==0)
	{
		cout<<"IMPOSSIBLE"<<endl;
		return ;
	}
	for(;i<=n;i++)
	{
		if(st[i]<=tim)
		{
			for(j=i;j<=n;j++)
			{
				if(st[j]>tim)
					ans++;
			}
		}
	}
	cout<<ans<<endl;
}

int main()
{
	freopen("t1.in","r",stdin);
	freopen("t1.out","w",stdout);
	int i,tests;
	cin>>tests;
	for(i=1;i<=tests;i++)
	{
		cout<<"Case #"<<i<<": ";
		myin();
		work();
	}
return 0;
}