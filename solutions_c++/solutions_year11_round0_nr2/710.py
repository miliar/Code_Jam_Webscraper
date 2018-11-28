#include <iostream>
#include <cstdio>
using namespace std;

int main() {

freopen("in.txt", "r", stdin);

int C, D, N, R, i, j, k, t, T;
char c[64][4], d[64][4], n[128], r[128];
bool flag;

cin >> T;

for (t=1; t<=T; t++) {

cin >> C;
for (i=0; i<C; i++) {
	cin >> c[i];
}

cin >> D;
for (i=0; i<D; i++) {
	cin >> d[i];
}

cin >> N;
cin >> n;

R = 0;
for (i=0; i<N; i++) {
	if (R == 0) r[R++] = n[i];
	else {
		for (j=0; j<C; j++) {
			if ((c[j][0] == n[i] && c[j][1] == r[R-1]) || (c[j][1] == n[i] && c[j][0] == r[R-1])) {
				r[R-1] = c[j][2];
				break;
			}
		}

		if (j == C) {
			flag = true;
			for (j=0; j<R; j++) {
				for (k=0; k<D; k++) {
					if ((r[j] == d[k][0] && n[i] == d[k][1]) || (r[j] == d[k][1] && n[i] == d[k][0])) {
						R = 0;
						flag = false;
						break;
					}
				}
				if (!flag) break;
			}

			if (flag) r[R++] = n[i];
		}
	}
}

cout << "Case #" << t << ": [";
for (i=0; i<R-1; i++) {
	cout << r[i] << ", ";
}
if (R > 0) cout << r[R-1];
cout << ']' << endl;

}

return 0;
}
