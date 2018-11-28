#include <iostream>
#include <vector>


using namespace std;


vector<int> v;
vector<int> room[146];
int cnt;
bool f[146][146];
int ans;
int col[146], colc[146];
bool used[10];
int beg[146], endd[146];


void divide(vector<int> v)
{
	vector<int> v1, v2;
	for(int i = 0; i < v.size(); i++)
		for(int j = 0; j < v.size(); j++)
			if(f[v[i]][v[j]])
			{
				v1.clear();
				v2.clear();
				for(int cur = i; cur != j; cur = (cur + 1) % v.size())
					v1.push_back(v[cur]);
				v1.push_back(v[j]);
				for(int cur = j; cur != i; cur = (cur + 1) % v.size())
					v2.push_back(v[cur]);
				v2.push_back(v[i]);
				if(v1.size() > 2 && v2.size() > 2)
				{
					divide(v1);
					divide(v2);
					return;
				}
			}
	room[cnt++] = v;
}


bool check(int n)
{
	for(int i = 0; i < cnt; i++)
	{
		memset(used, false, sizeof(used));
		for(int j = 0; j < n; j++)
			used[colc[j]] = true;
		for(int j = 0; j < room[i].size(); j++)
			used[colc[room[i][j]]] = false;
		for(int j = 0; j < n; j++)
			if(used[j])
				return false;
	}
	return true;
}


void rec(int cur, int colCnt, int n)
{
	if(cur == n)
	{
		if(check(n))
		{
			int maxx = colCnt;
			if(maxx > ans)
			{
				ans = maxx;
				for(int i = 0; i < n; i++)
					col[i] = colc[i];
			}
		}
		return;
	}
	for(int i = 0; i < colCnt; i++)
	{
		colc[cur] = i;
		rec(cur + 1, colCnt, n);
	}
	colc[cur] = colCnt;
	rec(cur + 1, colCnt + 1, n);
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for(int _ = 0; _ < t; _++)
	{
		int n, m;
		scanf("%d%d", &n, &m);
		fprintf(stderr, "%d\n", _);
		memset(f, false, sizeof(f));
		for(int i = 0; i < m; i++)
			scanf("%d", &beg[i]);
		for(int i = 0; i < m; i++)
			scanf("%d", &endd[i]);
		for(int i = 0; i < m; i++)
		{
			beg[i]--;
			endd[i]--;
			f[beg[i]][endd[i]] = f[endd[i]][beg[i]] = true;
		}
		v.clear();
		for(int i = 0; i < n; i++)
			v.push_back(i);
		for(int i = 0; i < n; i++)
			room[i].clear();
		cnt = 0;
		divide(v);
		int maxCol = 0;
		for(int i = 0; i < cnt; i++)
			maxCol = max(maxCol, (int)room[i].size());
		ans = 0;
		rec(0, 0, n);
		printf("Case #%d: %d\n", _ + 1, ans);
		for(int i = 0; i < n; i++)
			printf("%d ", col[i] + 1);
		printf("\n");
	}
}