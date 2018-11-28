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


int n, k;
int h[111][26];
int eq[111][111];
int ls[111][111];
int gr[111][111];
int edg[111][111];



void Load()
{
	cin >> n >> k;
	int i, j, t;
	for (i = 1; i <= n; i++){
		for (j = 1; j <= k; j++) scanf("%d", &h[i][j]);
	}
	memset(gr, 0, sizeof(gr));
	memset(eq, 0, sizeof(eq));
	memset(ls, 0, sizeof(ls));
	memset(edg, 0, sizeof(edg));
}


int was[111];
int b[111];



bool test(int ver)
{
	if (was[ver] == 1) return false;
	was[ver] = 1;
	int i;
	for (i = 1; i <= n; i++) {
		if (edg[ver][i] == 0) continue;
		if (b[i] == 0 || test(b[i])) {
			b[i] = ver;
			return true;
		} 
	}	
	return false;
}



void Solve()
{
	int i, j, t;
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= n; j++) {
			for (t = 1; t <= k; t++) {
				if (h[i][t] > h[j][t]) {
					gr[i][j] = 1;					
				} else
				if (h[i][t] < h[j][t]) {
					ls[i][j] = 1;					
				} else
				eq[i][j] = 1;
			}
		}
	}
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= n; j++) {
			if (eq[i][j]) continue;
			if (ls[i][j]) continue;
			if (gr[i][j]) {
				edg[j][i] = 1;
			}
		}
	}
	int res = 0;
	memset(b, 0, sizeof(b));
	for (i = 1; i <= n; i++) {
		memset(was, 0, sizeof(was));
		if (test(i))res++;
	}
	res = n - res;
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