#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

char c[256][256];
bool o[256][256];
vector<char> ans;

void init()
{
	memset(c,0,sizeof(c));
	memset(o,false,sizeof(o));
	char s[5];
	int i,n;
	scanf("%d",&n);
	for (i = 0; i < n; i++)
	{
		scanf("%s",s);
		c[s[0]][s[1]] = s[2];
		c[s[1]][s[0]] = s[2];
	}
	scanf("%d",&n);
	for (i = 0; i < n; i++)
	{
		scanf("%s",s);
		o[s[0]][s[1]] = true;
		o[s[1]][s[0]] = true;
	}
}

void work()
{
	int k = ans.size();
	for (int i = 0; i < k; i++)
		for (int j = i + 1; j < k; j++)
			if (o[ans[i]][ans[j]])
			{
				ans.clear();
				return;
			}
}

void solve()
{
	char s[512];
	ans.clear();
	int n;
	scanf("%d",&n);
	scanf("%s",s);
	for (int i = 0; i < n; i++)
	{
		ans.push_back(s[i]);
		while (1)
		{
			int k = ans.size();
			char com;
			if (k >= 2 && (com = c[ans[k - 1]][ans[k - 2]]))
			{
				ans.pop_back();
				ans.pop_back();
				ans.push_back(com);
			} else break;
		}
		work();			
	}
}

int main()
{
//	freopen("B.in","r",stdin);
//	freopen("B.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i = 1; i <= T; i++)
	{
		init();
		solve();
		printf("Case #%d: [",i);
		if (ans.size() >= 1) printf("%c",ans[0]);
		for (int j = 1; j < ans.size(); j++)
		{
			printf(", %c",ans[j]);
		}
		printf("]\n");
	}
	return 0;
}