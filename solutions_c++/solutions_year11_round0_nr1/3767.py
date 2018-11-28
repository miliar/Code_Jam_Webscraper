// MS Visual C++ 2008
#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int tk = 1; tk <= t; tk++) {
		int n;
		scanf("%d", &n);
		vector <char> r(n);
		vector <int> _O, _B;
		for (int i = 0; i < n; i++) {
			int p;
			scanf(" %c %d", &r[i], &p);
			if (r[i] == 'O') _O.push_back(p);
			else _B.push_back(p);
		}
		
		_O.push_back(0);
		_B.push_back(0);

		int op = 1, bp = 1, c = 0, ok = 0, bk = 0, tm = 0;
		while (c < n) {
			if (r[c] == 'O') {
				if (op < _O[ok]) op++;
				else if (op > _O[ok]) op--;
				else {
					ok++;
					c++;
				}
				if (bp < _B[bk]) bp++;
				else if (bp > _B[bk]) bp--;
			}
			else {
				if (bp < _B[bk]) bp++;
				else if (bp > _B[bk]) bp--;
				else {
					bk++;
					c++;
				}
				if (op < _O[ok]) op++;
				else if (op > _O[ok]) op--;
			}
			tm++;
		}
		cout << "Case #" << tk << ": " << tm << endl;
	}
	return 0;
}