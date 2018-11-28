#include <iostream>
#include <cstdio>

using namespace std;

string s[10010];
string g[10010];
string h[10010];
string l_[110];
int st[20];
//bool flag[10010];
int n,m;
bool exist(int l, int r, char ch)
{
	int i, j;
	for (i = l; i < r; ++i) {
		//cout << "exist " << ch << " " << g[i] << " " << endl;
		for (j = 0; j < g[i].size(); ++j) if (g[i][j] == ch) return true;
	}
	return false;
}
bool doit(string t, string &s, char ch)
{
	bool ret = false;
	int i;
	for (i = 0; i < t.size(); ++i)
		if (t[i] == ch) {
			if (s[i] != ch) ret = true;
			s[i] = ch;
		}
	return ret;
}
int get(string s, string list)
{
//	cout << "Get " << s << "   where l = " << list << endl;
	int l = st[s.size()], r = st[s.size() + 1];//[l,r)

	int i;
	int rem = 0;
	for (i = l; i < r; ++i) if (g[i] == s) {
		swap(g[i], g[l]);
		break;
	}
	//if (g[l] != s) while (1);
	//if (g[l].size() != g[r-1].size()) while (1);
	if (l + 1== r) return 0;
	for (i = l; i < r; ++i) h[i] = string(s.size(), '_');
	//lÊÇÑ¡ÔñµÄword 
	int id = 0;
	bool guess[30] = {0};
	int ans = 0;
	while (1) {
		//cout << "guess " << list[id] << endl;
		while (guess[id] || !exist(l, r, list[id])) id = (id + 1) % 26;
		//cout << "guess " << list[id] << endl;
		guess[id] = true;
		if (!doit(g[l], h[l], list[id])) --ans;
		for (i = l + 1; i < r; ++i) doit(g[i], h[i], list[id]);
		//for (i = l; i < r; ++i) cout << i << " " << h[i] << endl;
		if (h[l] == g[l]) return ans;
		//--ans;
		for (i = r - 1; i > l; --i)
			if (h[i] != h[l]) {
				swap(h[i], h[r - 1]);
				swap(g[i], g[r - 1]);
				//h[i] = h[r - 1];
				--r;
			}
		if (l + 1 == r) return ans;
		id = (id + 1) % 26;
	}
	return ans;
}
string calc(string l)
{
	//int id = 0;
	int ans = 1;
	int i;
	string ret;
	for (i = 0; i < n; ++i) {
		int cur = get(s[i], l);
		if (cur < ans) {
			ans = cur;
			ret = s[i];
		}
	}
	//cout<<"  "<<ans<<"  ";
	return ret;
}
bool cmp(const string& a, const string& b)
{
	return a.size() < b.size();
}
int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cin>>n>>m;
		int i;
		//memset(len, 0, sizeof(len));
		for (i = 0; i < n; ++i) {
			cin >> s[i];
			g[i] = s[i];
		}
		sort(g, g + n, cmp);
		int j;
		for (i=j=0; i <= n && j <= 11; ) {
			if (i >= n) {
				st[j] = n;
				++j;
				continue;
			}
			if (j < g[i].size()) {
				st[j] = i;
				++j;
				continue;
			}
			if (j > g[i].size()) {
				++i;
				continue;
			}
			if (j == g[i].size()) {
				st[j] = i;
				++i;++j;
				continue;
			}
		}
		//for (j = 0; j <= 11; ++j) cout << j << " " << st[j] <<endl;
		for (i = 0; i < m; ++i) cin >> l_[i];
		
		printf("Case #%d:", t);
		
		for (i = 0; i < m; ++i) printf(" %s", calc(l_[i]).c_str());
		printf("\n");
	}
}
