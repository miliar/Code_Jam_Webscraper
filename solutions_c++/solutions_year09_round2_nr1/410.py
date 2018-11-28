#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
#include <algorithm>
#include <vector>
using namespace std;

int T, n;
int next[1000][10], prev[1000], col[1000];
string s[1000];
string st[1000];
double p[1000];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	scanf("%d\n", &T);

	char c[1000];

	for (int TT = 1; TT <= T; TT++)
	{
		for (int i = 0; i < 500; i++)
			st[i] = "";
		memset(next, 0, sizeof next);
		memset(col, 0, sizeof col);
		memset(prev, 0, sizeof prev);
		memset(p, 0, sizeof p);

		scanf("%d\n", &n);
		for (int i = 1; i <= n; i++)
		{
			gets(c);
			s[i] = string(c) + "&";
		}

		int v = 0;
		int k = 0;

		for (int i = 1; i <= n; i++)
			for (int j = 0; j < s[i].size()-1; j++)
			{
				if (s[i][j] == '(')
				{
					col[v]++;
					k++;
					next[v][col[v]] = k;
					prev[k] = v;
					v = k;
				}
				else if (s[i][j] == ')')
				{
					v = prev[v];
				}
				else if (s[i][j] == '0' || s[i][j] == '1')
				{
					int uk1 = j;
					string s1 = "";
					while (s[i][uk1+1] == '.' || (s[i][uk1+1] >= '0' && s[i][uk1+1] <= '9'))
						uk1++;
					for (int uk2 = j; uk2 <= uk1; uk2++)
					{
							s1 = s1 + s[i][uk2];
					}

					p[v] = s1[0]-'0';
					double des = 0.1;
					for (int tt = 2; tt < s1.size(); tt++)
					{
						p[v] += des*(s1[tt]-'0');
						des /= 10;
					}

					j = uk1;
				}
				else if (s[i][j] == ' ')
				{}
				else
				{
					int uk1 = j;
					string s1 = "";
					while ((s[i][uk1+1] >= 'a' && s[i][uk1+1] <= 'z') || (s[i][uk1+1] >= 'A' && s[i][uk1+1] <= 'Z'))
						uk1++;
					for (int uk2 = j; uk2 <= uk1; uk2++)
						s1 = s1 + s[i][uk2];
					st[v] = s1;
					j = uk1;			
				}
			}

		cout << "Case #" << TT << ":" << endl; 
		
		double res;
		int t;
		
		cin >> t;
		int r;
		for (int i = 0; i < t; i++)
		{
			cin >> s[0] >> r;
			for (int j = 0; j < r; j++)
				cin >> s[j];

			res = p[1];
			v = 1;
			
			while (st[v] != "")
			{
				bool q = false;
				for (int j = 0; j < r; j++)
					if (s[j] == st[v])
						q = true;

				if (q)
				{
					v = next[v][1];
					res *= p[v];
				}
				else
				{
					v = next[v][2];
					res *= p[v];
				}
			}

			printf("%.10f\n", res);
		}
	}

	return 0;
}