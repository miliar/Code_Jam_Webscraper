#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

struct Like
{
	int num;
	bool matel;
	bool operator<(const Like& rhs) const
	{
		return matel < rhs.matel;
	}
};

vector<Like> v[2000];
vector<int> pre[2000];
bool vis[2000],ismatle[2000];
int n,m,C,t;

void input()
{
	Like temp;
	for(int i = 0;i < n;++i)
		pre[i].clear();
	for(int i = 0;i < m;++i)
		v[i].clear();
	for(int i = 0;i < m;++i)
	{
		scanf("%d",&t);
		for(int j = 0;j < t;++j)
		{
			scanf("%d%d",&temp.num,&temp.matel);
			temp.num--;
			v[i].push_back(temp);
		}
		sort(v[i].begin(),v[i].end());
	}
}

bool myfind(int i)
{
	for(int j = 0;j < v[i].size();++j)
	{
		if(!vis[v[i][j].num])
		{
			vis[v[i][j].num] = 1;
			if(pre[v[i][j].num].size() == 0 || ismatle[v[i][j].num] == v[i][j].matel)
			{
				ismatle[v[i][j].num] = v[i][j].matel;
				pre[v[i][j].num].push_back(i);
				return true;
			}
			else
			{
				int k;
				for(k = 0;k < pre[v[i][j].num].size();++k)
				{
					if(!myfind(pre[v[i][j].num][k]))
						break;
				}
				if(k == pre[v[i][j].num].size())
				{				
					ismatle[v[i][j].num] = v[i][j].matel;
					pre[v[i][j].num].clear();
					pre[v[i][j].num].push_back(i);
					return true;
				}
			}
		}
	}
	return false;
}

int main()
{
	freopen("out.txt","w",stdout);
	scanf("%d",&C);
	for(int c = 1;c <= C;++c)
	{
		int ans = 0;
		scanf("%d%d",&n,&m);
		memset(ismatle,0,sizeof(ismatle));
		input();
		int i;
		for(i = 0;i < m;++i)
		{
			memset(vis,0,sizeof(vis));
			if(!myfind(i))
				break;
		}
		printf("Case #%d:",c);
		if(i == m)
		{
			for(int i = 0;i < n;++i)
				printf(" %d",ismatle[i]);
			printf("\n");
		}
		else
		{
			int i;
			for(i = 0;i < m;++i)
			{
				int j;
				for(j = 0;j < v[i].size();++j)
				{
					if(v[i][j].matel == 1)
					{
						break;
					}
				}
				if(j == v[i].size())
					break;
			}
			if(i < m)
				printf(" IMPOSSIBLE\n");
			else
			{
				for(int i = 0;i < n;++i)
					printf(" 1");
				printf("\n");
			}
		}
	}
}


