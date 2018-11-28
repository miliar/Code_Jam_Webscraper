#include <stdio.h>
#include <string.h>
#include <set>
#include <string>
#include <map>
#include <iostream>
using namespace std;
const int N = 5005;

bool curg[N][N];
bool g[N][N];
bool vis[N];
int link[N];
int n, T;
char s[N];
int cid;
set<string> M;
map<string, int> str2id;
map<int, string> id2str;
set<char> change[256];

bool find(int x)
{
	for (int i = 1; i <= cid; ++i) if (!vis[i] && g[x][i]) {
		vis[i] = true;
		if (link[i] == 0 || find(link[i])) {
			link[i] = x;
			return true;
		}
	}
	return false;
}

int dfs(int x, int target)
{
	for (int i = 1; i <= cid; ++i) if (curg[x][i])
		if (i == target) 
			return 1;
		else if (!vis[i]) {
			vis[i] = true;
			if (dfs(i, target)) return 1;
		}
	return 0;
}

void work()
{
	id2str.clear();
	str2id.clear();
	scanf("%*d\n");
	gets(s);
	M.clear();
	for (int i = 0; s[i + 1]; ++i) {
		string tmp;
		tmp += s[i];
		tmp += s[i + 1];
		for (set<char>::iterator it1 = change[s[i]].begin(); it1 != change[s[i]].end(); ++it1)
		for (set<char>::iterator it2 = change[s[i+1]].begin(); it2 != change[s[i+1]].end(); ++it2) {
			tmp[0] = *it1;
			tmp[1] = *it2;
		
			M.insert(tmp);
		}
	}
	cid = 0;
	for (set<string>::iterator it = M.begin(); it != M.end(); ++it) {
		string str = *it;
		str2id[str] = ++cid;
		id2str[cid] = str;
		//cout << str << endl;
	}
//	printf("%d\n", cid);
	memset(g, 0, sizeof(g));
	for (int i = 1; i <= cid; ++i) for (int j = 1; j <= cid; ++j) if (i != j) {
		string str1 = id2str[i], str2 = id2str[j];
		if (str1[1] == str2[0])
			g[i][j] = true;
	}
	memset(link, 0, sizeof(link));
	int ans = cid * 2;
	for (int i = 1; i <= cid; ++i) {
		memset(vis, 0, sizeof(vis));
		if (find(i)) --ans;
	}
	memset(curg, 0, sizeof(curg));
	memset(vis, 0, sizeof(vis));
	for (int i = 1; i <= cid; ++i) if (link[i] != 0)
		curg[link[i]][i] = true;
	/*
	for (int i = 1; i <= cid; ++i) if (!vis[i]) {
		vis[i] = true;
		ans += dfs(i, i);
	}
	*/
	if (ans == cid) ++ans;
	static int ttt = 0;
	printf("Case #%d: ", ++ttt);
	printf("%d\n", ans);
}

void gao(char a, char b)
{
	change[a].insert(b);
	change[b].insert(a);
}

int main()
{
	gao('o', '0');
	gao('i', '1');
	gao('e', '3');
	gao('a', '4');
	gao('s', '5');
	gao('t', '7');
	gao('b', '8');
	gao('g', '9');
	for (char c = 'a'; c <= 'z'; ++c)
		change[c].insert(c);
	
	scanf("%d", &T);
	while (T--) work();
}
