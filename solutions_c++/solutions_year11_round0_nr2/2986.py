#include <algorithm>
#include <iostream>
#include <vector>
#include <cstdio>
#include <deque>

using namespace std;

const int MAXN = 'Z' + 1;

char adj[MAXN][MAXN];
bool kill[MAXN][MAXN];
int cnt[MAXN];
char res[1000];
char s[1000];

void Solve()
{
	int nadj;
	cin >> nadj;

	fill(&adj[0][0], &adj[0][0] + MAXN * MAXN, 0);
	fill(&kill[0][0], &kill[0][0] + MAXN * MAXN, false);
	fill(cnt, cnt + MAXN, 0);

	for (int i = 0; i < nadj; ++ i)
	{
		cin >> s;
		adj[s[0]][s[1]] = s[2];
		adj[s[1]][s[0]] = s[2];
	}

	int nkill;
	cin >> nkill;
	for (int i = 0; i < nkill; ++ i)
	{
		cin >> s;
		kill[s[0]][s[1]] = kill[s[1]][s[0]] = 1;
	}

	int n;
	cin >> n;

	int size = 0;
	res[size ++] = ' ';

	char c, next;
	for (int i = 0; i < n; ++ i)
	{
		cin >> c;
		res[size ++] = c;
		++ cnt[c];
		
		while (next = adj[res[size - 2]][res[size - 1]])
		{
			-- cnt[res[-- size]];
			-- cnt[res[-- size]];
			++ cnt[res[size ++] = next];
		}

		for (int j = 1; j < size - 1; ++ j)
		{
			if (kill[res[size - 1]][res[j]])
			{
				size = 1;
				break;
			}
		}		
	}

	cout << "[";
	for (int i = 1; i < size - 1; ++ i)
	{
		cout << res[i] << ", ";
	}

	if (size > 1)
	{
		cout << res[size - 1];
	}

	cout << "]" << endl;


}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int ntest;
	cin >> ntest;

	for (int test = 1; test <= ntest; ++ test)
	{
		cout << "Case #" << test << ": ";
		Solve();
	}



	return 0;
}