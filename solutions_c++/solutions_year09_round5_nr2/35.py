#include <iostream>
#include <fstream>
#include <strstream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <vector>

using namespace std;

ifstream fin("B-small-attempt0.in");
ofstream fout("B-small-attempt0.out");

#define cin fin
#define cout fout

char words[110][64];
int len[110];

int n, k, nowk;
char s[1024];
int lengs;

long ans;

int p[11];

void cal()
{
	int a[26];
	memset(a, 0, sizeof(a));

	for (int i = 0; i < nowk; i++)
		for (int j = 0; j < len[p[i]]; j++)
		{
			a[  words[p[i]][j] - 'a' ]++;
		}

	int sum = 0;
	int sub = 1;
	for (int i = 0; i < lengs; i++)
	{
		if (s[i] >= 'a' && s[i] <= 'z')
		{
			sub = sub * a[s[i]-'a'];
		} else
		{
			sum += sub;
			sum %= 10009;
			sub = 1;
		}
	}
	sum += sub;
	sum %= 10009;

	ans = (ans + sum) % 10009;
}

void dfs(int now)
{
	if (now == nowk)
	{
		cal();
		return;
	}
	for (int i = 0; i < n; i++)
	{
		p[now] = i;
		dfs(now+1);
	}
}

int main()
{
	int cases;
	cin >> cases;

	for (int i = 0; i < cases; i++)
	{
		cin >> s;
		lengs = strlen(s);

		cin >> k;
		cin >> n;
		for (int j = 0; j < n; j++)
		{
			cin >> words[j];
			len[j] = strlen(words[j]);
		}

		cout << "Case #" << i+1 << ":";
		for (int j = 1; j <= k; j++)
		{
			nowk = j;
			ans = 0;
			dfs(0);
			cout << " " << ans;
		}
		cout << endl;
	}

	return 0;
}