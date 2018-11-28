#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <vector>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.txt");

#define cin fin
#define cout fout


char s[128];
int len;
int n, m;

int done[10000];
int son[10000];
int bro[10000];

int total;

char name[10000][200];
int ans;

bool same(char *sub, int a, int b)
{
	for (int i = a; i < b; i++)
		if (sub[i-a] != s[i]) return false;
	if (sub[b-a] != 0) return false;

	return true;
}

void work(int cur, int p, int mark)
{
	if (p >= len) return;

	int next = p+1;
	while (next < len && s[next] != '/') next++;

	int back = cur;

	cur = son[cur];
	while (cur >= 0)
	{
		if (same(name[cur], p, next) == true)
		{
			work(cur, next, mark);
			return;
		}
		cur = bro[cur];
	}

	int temp = son[back];
	son[back] = total;
	bro[total] = temp;

	done[total] = mark;
	for (int i = p; i < next; i++)		
		name[total][i-p] = s[i];

	total++;

	if (total > 9000)
	{
		cerr << "Warning" << endl;
	}

	work(total-1, next, mark);
}

int main()
{
	int testcases;

	cin >> testcases;
	for (int i = 0; i < testcases; i++)
	{
		total = 1;
		memset(done, 0, sizeof(done));
		memset(name, 0, sizeof(name));
		memset(son, 0xff, sizeof(son));
		memset(bro, 0xff, sizeof(son));

		cin >> n >> m;
		for (int j = 0; j < n; j++)
		{
			memset(s, 0, sizeof(s));
			cin >> s;

			len = strlen(s);

			work(0, 0, 1);
		}

		for (int j = 0; j < m; j++)
		{
			memset(s, 0, sizeof(s));
			cin >> s;
			len = strlen(s);

			work(0, 0, 0);
		}

		ans = 0;
		for (int j = 1; j < total; j++)
			if (done[j] == 0) ans++;


		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}