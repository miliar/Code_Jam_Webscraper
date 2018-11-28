#include <iostream>
#include <vector>
using namespace std;

const int MAX = 1005;

//int mm[MAX][MAX];
vector<vector<int> > mm;
int d[MAX];
int s[MAX];

int n;

bool dfs(int u)
{
	if(s[u])  return true;
	s[u] = 1;

	//for(int i = 1; i <= n; i++)
	for(int i = 0; i < mm[u].size(); i++)
	{
		if(dfs(mm[u][i])) 
			return true;
	}
	return false;
}

bool go()
{
	for(int i = 1; i <= n; i++)
	{
		if(d[i] == 0)
		{
			memset(s, 0, sizeof(s));
			if(dfs(i)) 
				return true;
		}
	}
	return false;
}

int main()
{
	freopen("C:\\Users\\Administrator\\Desktop\\GCJ\\A-large.in", "r", stdin);
	freopen("C:\\Users\\Administrator\\Desktop\\GCJ\\A-large.out", "w", stdout);

	int T, c = 0;
	scanf("%d", &T);
	while(T--)
	{
		memset(d, 0, sizeof(d));
		//memset(s, 0, sizeof(s));
		//memset(mm, 0, sizeof(mm));
		scanf("%d", &n);
		mm.clear();
		mm.resize(n + 1);

		for(int i = 1; i <= n; i++)
		{
			int t;
			scanf("%d", &t);
			while(t--)
			{
				int b;
				scanf("%d", &b);
				//mm[i][b] = 1;
				mm[i].push_back(b);
				d[b]++;
			}
		}

		printf("Case #%d: ", ++c);
		puts(go() ? "Yes" : "No");
	}

	//system("pause");
}