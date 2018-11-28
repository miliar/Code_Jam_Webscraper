#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int n;
int a[10000];


void Load()
{
	

}

void Solve()
{
	int xr = 0;
	int mn = 1 << 30;
	int sum = 0;
    
    cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
		xr ^= a[i];
		if (a[i] < mn) mn = a[i];
		sum += a[i];
	}

	if (xr != 0) cout << "NO\n";
	else cout << sum - mn << "\n";
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
