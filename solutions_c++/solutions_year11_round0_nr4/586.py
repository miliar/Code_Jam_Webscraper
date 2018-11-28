#include <iostream>
#include <fstream>
#include <vector>    

using namespace std;


int n;
int a[1111];
int w[1111];

void Load()
{
	cin >> n;
	for (int i = 1; i <= n; i++)
		cin >> a[i];

}

void Solve()
{
	int i;
	int ans = 0;
	memset(w, 0, sizeof(w));
	for (i = 1; i <= n; i++) {
		int cur = 0;
		if (w[i] == 0) {
			int j = i;
			while (w[j] == 0) {
				w[j] = 1;
				cur++;
				j = a[j];
			}
			if (cur > 1) ans += cur;
		}
	}
	cout << ans << ".000000\n";
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
