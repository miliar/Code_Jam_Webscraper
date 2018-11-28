#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>


using namespace std;
const long double eps = 1e-9;
const long double Pi = 3.1415926535897932384626433832795;

int n;
int mx[44];



void Load()
{
	cin >> n;	
	int i, j, k;
	char c;
	for (i = 1; i <= n; i++) {
		k = 0;
		for (j = 1; j <= n; j++) {
			c = getchar();
			while(c != '0' && c != '1') c = getchar();
			if (c == '1') k = j;
		}
		mx[i] = k;
	}
}
void Solve()
{
	int res = 0;
	int i, j, k;
	for (i = 1; i <= n; i++) {
		for (j = i; mx[j] > i; j++);
		res += j - i;
		k = mx[j];
		for (; j > i; j--) {
			mx[j] = mx[j - 1];
		}
		mx[i] = k;
	}
	cout << res << "\n";
}




int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t, nt;
	cin >> nt;
	for (t = 1; t <= nt; t++) {
		Load();
		cout << "Case #" << t << ": ";
		Solve();
	}
	return 0;
}