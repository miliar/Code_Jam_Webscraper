#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
using namespace std;
int comb[27][27], opp[27][27];
int L[1000], r, n;

void init()
{
	memset(comb,0,sizeof(comb));
	memset(opp,0,sizeof(opp));
	string st; int k, x, y, z;
	cin >> k;
	for (int i = 0; i != k; ++i) {
		cin >> st;
		x = st[0] - 'A' + 1;
		y = st[1] - 'A' + 1;
		z = st[2] - 'A' + 1;
		comb[x][y] = comb[y][x] = z;
	}
	cin >> k;
	for (int i = 0; i != k; ++i) {
		cin >> st;
		x = st[0] - 'A' + 1;
		y = st[1] - 'A' + 1;
		opp[x][y] = opp[y][x] = 1;
	}
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);

	string st;
	int TextNum, Num = 0, c;
	cin >> TextNum;
	while (TextNum--) {
		cout << "Case #" << ++Num << ": ";

		init();
		cin >> n;
		cin >> st;
		r = 0;
		for (int i = 0; i != n; ++i) {
			c = st[i] - 'A' + 1;
			L[++r] = c;
			if (r>1) {
				if (comb[L[r]][L[r-1]]) {
					L[r-1] = comb[L[r]][L[r-1]];
					--r;
				}
				for (int j = 1; j < r; ++j)
					if (opp[L[j]][L[r]]==1) {
						r = 0;
						break;
					}
			}
		}
		cout << "[";
		for (int i = 1; i <= r; ++i) {
			char a = 'A' + L[i] - 1;
			cout << a;
			if (i != r) cout << ", ";
		}
		cout << "]" << endl;
	}
	return 0;
}