#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

const int maxn = 1024;
int prim[513];

void init()
{
	int i, j;
	for (i = 2; i <= 512; i ++) {
		int t = (int)sqrt(i);
		for (j = 2; j <= t; j ++)
			if (i%j == 0) break;
			if (j == t+1) {
			prim[i] = 1;
			}
	}
	return;
}

bool inv(int x, int a, int b)
{
	return (x >= a && x <= b);
}

int main()
{
	init();
	int C, A, B, P, i, j, k, u;
	int flag[maxn];
	freopen("bb.in", "r", stdin);
	freopen("bb.out", "w", stdout);
	cin >> C;
	for (i = 1; i <= C; i ++) {
		cin >> A >> B >> P;
		memset(flag, 0, sizeof(flag));

		int q = 0;
		for (j = P; j <= B/2; j ++) {
			if (prim[j]) {
				vector <int> s;
				int ff = false;
				for (k = 1; j*k <= B; k ++) {
					if (inv(j*k, A, B)) {
						if (flag[j*k] > 0) ff = true;
						s.push_back(j*k);
					}
				}
				if (s.size() > 1) {
					if (!ff) q ++;
					for (u = 0; u < s.size(); u ++) {
						flag[s[u]] = q;
					}
				}
			}
		}
		/*for (j = A; j <= B; j ++)
			cout << flag[j] <<' ';
		cout << endl;*/

		for (j = A; j <= B; j ++) {
			if (flag[j] == 0) q ++;
		}
		cout <<"Case #" << i << ": " << q << endl;
	}
	return 0;
}