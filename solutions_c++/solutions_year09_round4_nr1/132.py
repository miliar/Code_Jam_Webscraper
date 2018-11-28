#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


int n;
int b[50][50];
int a[50];


void Load()
{
	cin >> n;
	int i, j, k;
	char c;
	for (i = 1; i <= n; i++)
	{
		k = 0;
		for (j = 1; j <= n; j++)
		{
			cin >> c;
			if (c == '1') k = j;
		}
		a[i] = k;
	}

}

int ans;

void Move(int i, int j)
{
	int k, t;
	for (k = j; k > i; k--)
	{
		ans++;
		t = a[k]; a[k] = a[k-1]; a[k-1] = t;
	}
}

void Solve()
{
	ans = 0;
	int i, j;
	for (i = 1; i <= n; i++)
	{
		if (a[i] <= i) continue;
		for (j = i+1; j <= n; j++)
		{
			if (a[j] <= i) break;
		}
		Move(i, j);
	}
	cout << ans << "\n";
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
