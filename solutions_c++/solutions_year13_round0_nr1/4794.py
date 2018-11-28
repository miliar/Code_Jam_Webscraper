#include <iostream>
#include <string>
using namespace std;

const int N = 4 +10;

int ans;
int i;
int n = 4;
int tdnum;

string a[N];

void ri()
{
	int i;
	
	for (i = 0; i < n; i++) cin >> a[i];
}

bool judge44(char ch)
{
	bool pd;
	
	int i;
	int j;
	
	for (i = 0; i < n; i++)
	{
		pd = true;
		for (j = 0; j < n; j++) if (a[i][j] != ch && a[i][j] != 'T') pd = false;
		if (pd) return true;
	}
	for (j = 0; j < n; j++)
	{
		pd = true;
		for (i = 0; i < n; i++) if (a[i][j] != ch && a[i][j] != 'T') pd = false;
		if (pd) return true;
	}
	pd = true;
	for (i = 0; i < n; i++) if (a[i][i] != ch && a[i][i] != 'T') pd = false;
	if (pd) return true;
	pd = true;
	for (i = 0; i < n; i++) if (a[i][n - 1 - i] != ch && a[i][n - 1 - i] != 'T') pd = false;
	if (pd) return true;
	return false;
}

int solve()
{
	int i;
	int j;
	
	if (judge44('X')) return 0;
	if (judge44('O')) return 1;
	for (i = 0; i < n; i++) for (j = 0; j < n; j++) if (a[i][j] == '.') return 3;
	return 2;
}

void print()
{
	cout << "Case #" << i << ": ";
	if (ans == 0) cout << "X won";
	if (ans == 1) cout << "O won";
	if (ans == 2) cout << "Draw";
	if (ans == 3) cout << "Game has not completed";
	cout << "\n";
}

int main()
{
	cin >> tdnum;
	for (i = 1; i <= tdnum; i++)
	{
		ri();
		ans = solve();
		print();
	}
	return 0;
}
