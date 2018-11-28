#include <iostream>
#include <set>
#include <cmath>
#include <string>
#include <cstring>
using namespace std;

int st[100000], sz;
int par[100000];
double w[100000];
int le[100000], ri[100000];
string f[100000];
set<string> S;
int main()
{
	freopen("ain", "r", stdin);
	freopen("aout", "w", stdout);
	char ch;
	double p;
	string str;
	int T, t, L, u, n, m, num, i, state, pos;
	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		memset(st, 0, sizeof(st));
		memset(par, 0, sizeof(par));
		memset(le, 0, sizeof(le));
		memset(ri, 0, sizeof(ri));
		sz = 0;
		scanf("%d", &L);
		getchar();
		n = sz = 0;
		state = pos = 0;
		while (L)
		{
			ch = getchar();
			if (ch == '\n')
			{
				state = pos = 0;
				L--;
			}
			if (ch == ' ')
				state = pos = 0;
			if (ch >= '0' && ch <= '9')
			{
				if (state == 0)
					w[n-1] = w[n-1]*10+ch-'0';
				else
				{
					w[n-1] += (ch-'0')*pow(10.0, -pos);
					pos++;
				}
			}
			if (ch == '.')
				state = pos = 1;
			if (ch >= 'a' && ch <= 'z')
				f[n-1] += ch;
			if (ch == '(')
			{
				f[n] = "";
				w[n] = 0.0;
				if (sz)
					par[n] = st[sz-1];
				else
					par[n] = -1;
				n++;
				st[sz++] = n-1;
			}
			if (ch == ')')
				sz--;
		}
		for (i = 1; i < n; i++)
			if (le[par[i]] == 0)
				le[par[i]] = i;
			else
				ri[par[i]] = i;
		scanf("%d", &m);
		printf("Case #%d:\n", t);
		while (m--)
		{
			p = 1.0;
			u = 0;
			cin >> str;
			scanf("%d", &num);
			S.clear();
			while (num--)
			{
				cin >> str;
				S.insert(str);
			}
			do
			{
				p *= w[u];
				if (f[u] == "")
					break;
				if (S.find(f[u]) == S.end())
					u = ri[u];
				else
					u = le[u];
			}
			while (f[u] != "LEAF");
			printf("%.7lf\n", p);
		}
	}
	return 0;
}

