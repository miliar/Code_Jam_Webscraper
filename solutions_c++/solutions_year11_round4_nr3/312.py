#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

const int MAXN = 3000;

int p[MAXN];
int n;

void Load()
{
	cin >> n;
}

int tt;

void Solve()
{
	int i, j;
	p[1] = tt;
	int min, max;
	min = 0;
	max = 1;

	for (i = 2; i <= n; i++) {
		if (p[i] == tt) continue;
		min++;
		for (j = i*i; j <= n; j += i) {
			p[j] = tt;
		}
		j = i;
		while (j <= n) {
			max++;
			j *= i;
		}
	}
	if (n == 1) min = 1;
	cout << max - min << "\n";

}

int main()
{
	int nt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
