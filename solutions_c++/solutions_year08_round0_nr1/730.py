#include <cstdio>
#include <set>
#include <cstring>
using namespace std;

struct SearchE
{
	char name[101];
	mutable int num;
};

bool operator<(const SearchE lhs,const SearchE rhs)
{
	return strcmp(lhs.name,rhs.name) == -1;
}

int ans,T,s,q,n[1001],num;
bool vis[101];

set<SearchE> base;

void input()
{
	scanf("%d\n",&s);
	SearchE temp;
	base.clear();
	for(int i = 1;i <= s;++i)
	{
		temp.num = i;
		gets(temp.name);
		base.insert(temp);
	}
	scanf("%d\n",&q);
	set<SearchE>::iterator p;
	for(int i = 0;i < q;++i)
	{
		gets(temp.name);
		p = base.find(temp);
		if(p == base.end())
			n[i] = 0;
		else
			n[i] = p->num;
	}
}

int find(int i)
{
	num = 0;
	memset(vis,0,sizeof(vis));
	int j;
	for(j = i;j < q && num < s;++j)
		if(n[j] && (!vis[n[j]]))
		{
			vis[n[j]] = 1;
			num++;
		}
	return j;
}

void solve()
{
	ans = 0;
	int i = 0;
	while(i < q)
	{
		int j = find(i);
		if(num == s)
		{
			ans++;
			i = j-1;
			continue;
		}
		if(j == q)
			return;
	}
}

int main()
{
	freopen("out.txt","w",stdout);
	int t = 1;
	scanf("%d",&T);
	while(T--)
	{
		input();
		solve();
		printf("Case #%d: %d\n",t,ans);
		t++;
	}
	return 0;
}