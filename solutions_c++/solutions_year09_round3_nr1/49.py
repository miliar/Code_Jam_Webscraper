#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>

using namespace std;

void solve(void)
{
	char c;
	scanf("%c", &c);
	char s[70];
	scanf("%s", s);
	int len = strlen(s);
	if (len == 1)
	{
		cout << 1;
		return;
	}
	int i;
	int a[300];
	for (i = 0; i < 300; i++)
		a[i] = 0;
	for (i = 0; i < len; i++)
		a[s[i]]++;
	int bas = 0;
	for (i = 0; i < 300; i++)
		if (a[i])
			bas++;
	if (bas == 1)
		bas = 2;
	int b[300];
	for (i = 0; i < 300; i++)
		b[i] = i;
	swap(b[0], b[1]);
	for (i = 0; i < 300; i++)
		a[i] = -1;
	int jj = 0;
	for (i = 0; i < len; i++)
	{
		if (a[s[i]] == -1)
		{
			a[s[i]] = b[jj];
			jj++;
		}
	}
	unsigned long long res = 0;
	for (i = 0; i < len; i++)
	{
		res = res * bas + a[s[i]];
	}
	cout << res;
}

int main (void) 
{
	//freopen("input1.txt", "r", stdin);
	//freopen("A-small-attempt2.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("output1.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
}