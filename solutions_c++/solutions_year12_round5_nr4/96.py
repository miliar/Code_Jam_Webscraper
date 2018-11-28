#include <cstdio>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int INF = 1e9;
const double EPS = 1e-9;

char buff[1010];
char v[4010][3];
int p[128];
char l1[] = "oieastbg";
char l2[] = "01345789";
void init()
{
	for (int i = 0; i < 8; ++i)
		p[l1[i]] = l2[i];
}
const int MAXVERT = 5000;
struct matching
{
	int PairL[MAXVERT];
	int PairR[MAXVERT];
	vector<int> G[MAXVERT];
	int szL, szR;
	matching(){}

	int used[MAXVERT*2];
	int _tm;

	void init(int _szL, int _szR)
	{
	    szL = _szL;
	    szR = _szR;
	    for (int i = 0; i < szL; ++i)
	    	G[i].clear();
		memset(PairL, 0xff, sizeof(PairL));
		memset(PairR, 0xff, sizeof(PairR));
		_tm = 0;
		memset(used, 0, sizeof(used));
	}
	void addEdge(int from, int to) 	// from - ����� ����, to - ������. 
									// ������� ����������: 0..(szL-1) - �����, szL..(szL+szR-1) - ������								
	{
		G[from].push_back(to - szL);
	}
	
	bool dfs(int frm)
	{
		if (used[frm] == _tm)
		{
			return false;
		}
		used[frm] = _tm;
		for (int i = 0; i < G[frm].size(); ++i)
		{
			int nxt = G[frm][i];
			used[nxt + szL] = _tm;
			if (PairR[nxt] == -1 || dfs(PairR[nxt]))
			{
				PairR[nxt] = frm;
				return true;
			}
		}
		return false;
	}
	
	int buildMatching()
	{
		int ans = 0;
		for (int i = 0; i < szL; ++i)
		{
			++_tm;
			if (dfs(i))
				++ans;
		}
		for (int i = 0; i < szR; ++i)
		{
			if (PairR[i] != -1)
			{
				int v = PairR[i];
				PairL[v] = i + szL;
			}
		}
		return ans;
	}
	int getPair(int v)
	{
		if (v < szL) return PairL[v];
		else return PairR[v - szL];
	}
	vector<int> getIndep()
	{
		++_tm;
		for (int i = 0; i < szL; ++i)
		{
			if (PairL[i] == -1)
			{
				dfs(i);
			}
		}
		vector<int> ans;
		for (int i = 0; i < szL; ++i)
		{
			if (used[i] != _tm)
			{
				ans.push_back(i);
			}
		}
		for (int i = szL; i < szL + szR; ++i)
		{
			if (used[i] == _tm)
			{
				ans.push_back(i);
			}
		}
		return ans;
	}
} P;
void solve()
{
	int k;
	scanf ("%d", &k);
	scanf ("%s", buff);
	int len = strlen(buff);
	int cnt = 0;
	set<string> x;
	for (int i = 0; i < len - 1; ++i)
	{
		v[cnt][0] = buff[i];
		v[cnt][1] = buff[i + 1];
		if (x.find(v[cnt]) == x.end())
		{
			x.insert(v[cnt]);
			++cnt;
		}
		if (p[buff[i]] != 0)
		{
			v[cnt][0] = p[buff[i]];
			v[cnt][1] = buff[i + 1];
			if (x.find(v[cnt]) == x.end())
			{
				x.insert(v[cnt]);
				++cnt;
			}
		}
		if (p[buff[i + 1]] != 0)
		{
			v[cnt][0] = buff[i];
			v[cnt][1] = p[buff[i + 1]];
			if (x.find(v[cnt]) == x.end())
			{
				x.insert(v[cnt]);
				++cnt;
			}
		}
		if (p[buff[i]] != 0 && p[buff[i + 1]] != 0)
		{
			v[cnt][0] = p[buff[i]];
			v[cnt][1] = p[buff[i + 1]];
			if (x.find(v[cnt]) == x.end())
			{
				x.insert(v[cnt]);
				++cnt;
			}
		}
	}
	P.init(cnt, cnt);
	for (int i = 0; i < cnt; ++i)
	{
		for (int j = 0; j < cnt; ++j)
		{
			if (i == j) continue;
			if (v[i][1] == v[j][0])
			{
				P.addEdge(i, j+cnt);
			}
		}
	}
	int ans = P.buildMatching();
	if (ans == cnt) --ans;
	printf("%d\n", cnt*2 - ans);
}
int main()
{
	freopen("Dtest.txt", "r", stdin);
	freopen("Dout.txt", "w", stdout);

	init();
	int T;
	scanf ("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		printf("Case #%d: ", i + 1);
		fprintf(stderr, "%d/%d\n", i+1, T);
		solve();
	}
	return 0;
}