#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector <string> a;
vector <int> b;
int c[100];
int t, n, m, k;
string s;
char ch;

void read_string()
{
	s = "";
	scanf("%c", &ch);
	while (!((ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z') || (ch >= '0' && ch <= '9') || ch == ' '))
		scanf("%c", &ch);
	while (((ch >= 'A' && ch <= 'Z') || (ch >= 'a' && ch <= 'z') || (ch >= '0' && ch <= '9') || ch == ' ') && !feof(stdin))
	{
		s += ch;
		scanf("%c", &ch);
	}
}

int main()
{
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		a.clear();
		b.clear();
		scanf("%d", &n);
		for (int j = 0; j < n; j++)
		{
			read_string();
			a.push_back(s);
		}
		scanf("%d", &m);
		for (int j = 0; j < m; j++)
		{
			read_string();
			for (int u = 0; u < n; u++)
				if (a[u] == s)
				{
					b.push_back(u);
					break;
				}
		}
		memset(c, 0, sizeof(c));
		int mn = 0;
		for (int cc = m - 1; cc >= 0; cc--)
		{
			int mn2 = 10000;
			c[b[cc]] = -1;
			for (int j = 0; j < n; j++)
			{
				if (c[j] == -1 && b[cc] != j)
				{
					c[j] = mn + 1;
					mn2 = min(c[j], mn2);
				}
				else if (c[j] != -1)
				{
					c[j] = min(mn + 1, c[j]);
					mn2 = min(c[j], mn2);
				}
			}
			mn = mn2;
		}
		printf("Case #%d: %d\n", i + 1, mn);
	}
	return 0;
}
