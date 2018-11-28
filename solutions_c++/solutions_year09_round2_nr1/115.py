#include<iostream>
#include<string>
#include<sstream>
#include<set>
using namespace std;

const int maxn = 80;
string z;
string word[maxn];
double p[maxn];
int lc[maxn], rc[maxn], tnum;
bool leaf[maxn];
set<string> tt;

void build(int le, int ri)
{
//	for (int i = le; i <= ri; i++) cout << z[i];
//	cout << endl;
	string s;
	int i;
	for (i = le; i <= ri; i++)
		if (z[i] == '(')
			break;
		else s += z[i];
	stringstream ss(s);
	ss >> p[++tnum];
	if (!(ss >> word[tnum])) leaf[tnum] = true;
	if (leaf[tnum]) return;
	s = "";
	le = ++i;
	for (int sum = 1;  ; i++)
	{
		if (z[i] == '(') sum++;
		if (z[i] == ')') sum--;
		if (sum == 0) break;
	}
	int cur = tnum;
	lc[cur] = tnum + 1;
	build(le, i - 1);
	for (; z[i] != '('; i++);
	le = ++i;
	for (int sum = 1; ; i++)
	{
		if (z[i] == '(') sum++;
		if (z[i] == ')') sum--;
		if (sum == 0) break;
	}
	rc[cur] = tnum + 1;
	build(le, i - 1);
}

void count(int cur, double &ret)
{
	ret *= p[cur];
	if (leaf[cur]) return;
	if (tt.find(word[cur]) != tt.end())
		count(lc[cur], ret);
	else count(rc[cur], ret);
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T, t;
	for (cin >> T, t = 1; t <= T; t++)
	{
		printf("Case #%d:\n", t);
		int L;
		scanf("%d\n", &L);
		z = "";
		string s;
		for (int i = 0; i < L; i++)
		{
			getline(cin, s);
			z += s;
		}
		tnum = 0;
		memset(leaf, 0, sizeof(leaf));
		int le = 0, ri = z.size() - 1;
		while (z[le] != '(') le ++;
		while (z[ri] != ')') ri--;
		build(le + 1, ri - 1);
	//	for (int i = 1; i <= tnum; i++) cout << p[i] << " " << word[i] << " " << lc[i] << " " << rc[i] << "  " << (leaf[i] ? "true" : "false") << endl;
		int n, m;
		scanf("%d", &n);
		while (n--)
		{
			cin >> s >> m;
			tt.clear();
			for (int i = 0; i < m; i++)
			{
				cin >> s;
				tt.insert(s);
			}
			double ans = 1;
			count(1, ans);
			printf("%.7lf\n", ans);
		}
	}
}