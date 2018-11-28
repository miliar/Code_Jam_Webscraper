#include <stdio.h>
#include <set>
using namespace std;
int num[1002];
int n;
set<int> s;
int maxs;
void Dfs(int lv,int sum)
{
	if (lv>n)
	{
		int sz = s.size();
		int s1=0,s2=0;
		for (int i=1; i<=n; i++)
		{
			if (s.find(i)!=s.end())
			{
				s1 ^= num[i];
				//printf("num: %d\n",num[i]);
			}
			else
			{
				s2 ^= num[i];
			}
		}
		if (s1!=0 && s1==s2)
		{
			maxs = max(sum,maxs);
			//printf("maxs: %d\n",maxs);
		}
		//printf("\n");
		return;
	}
	s.insert(lv);
	Dfs(lv+1,sum+num[lv]);
	s.erase(lv);
	Dfs(lv+1,sum);
}

void Solve()
{
	maxs = 0;
	s.clear();
	Dfs(1,0);
	if (maxs==0)
	{
		printf("NO\n");
	}
	else
		printf("%d\n",maxs);
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int ncase;
	scanf("%d",&ncase);
	for (int c=1; c<=ncase; c++)
	{
		printf("Case #%d: ",c);
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%d",&num[i]);
		}
		Solve();
	}
}