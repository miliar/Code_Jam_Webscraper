#include <stdio.h>
#include <stack>
using namespace std;

int t[102][102];
int rr, cc, r, c;
int ns;
int a[102][102];
char cs[40];
stack<pair<short, short> > st;

int main() {
	int ntest, test;
	scanf("%d", &ntest);
	for (test = 1; test <= ntest; test++) {
		printf("Case #%d:\n", test);
		scanf("%d%d", &rr, &cc);
		for (r = 0; r < rr+2; r++) for (c = 0; c < cc+2; c++) t[r][c] = 123456, a[r][c] = 0;

		for (r = 1; r <= rr; r++) {
			for (c = 1; c <= cc; c++) {
				scanf("%d", &t[r][c]);
			}
		}
		ns = 0;
		for (r = 1; r <= rr; r++) {
			for (c = 1; c <= cc; c++) {
				if (t[r][c] <= t[r-1][c] && t[r][c] <= t[r+1][c] && t[r][c] <= t[r][c-1] && t[r][c] <= t[r][c+1]) {
					ns++;
					a[r][c] = ns;
					cs[ns] = ' ';
				}
			}
		}

		for (r = 1; r <= rr; r++) {
			for (c = 1; c <= cc; c++) {
				st.push(make_pair(r,c));
				int v = 0;
				while (true) {
					int r,c;
					int m = 1234567;
					r = st.top().first;
					c = st.top().second;
					if (a[r][c] != 0) {
						v = a[r][c];
						break;
					}
					if (t[r][c] > t[r-1][c] && m > t[r-1][c]) m = t[r-1][c];
					if (t[r][c] > t[r][c-1] && m > t[r][c-1]) m = t[r][c-1];
					if (t[r][c] > t[r][c+1] && m > t[r][c+1]) m = t[r][c+1];
					if (t[r][c] > t[r+1][c] && m > t[r+1][c]) m = t[r+1][c];
					if (t[r-1][c] == m) st.push(make_pair(r-1,c));
					else if (t[r][c-1] == m) st.push(make_pair(r,c-1));
					else if (t[r][c+1] == m) st.push(make_pair(r,c+1));
					else if (t[r+1][c] == m) st.push(make_pair(r+1,c));
				}
				while (!st.empty()) {
					int r,c;
					r = st.top().first;
					c = st.top().second;
					st.pop();
					a[r][c] = v;
				}
			}
		}

		char z = 'a';
		for (r = 1; r <= rr; r++) {
			for (c = 1; c <= cc; c++) {
				if (cs[a[r][c]] == ' ') cs[a[r][c]] = z++;
				printf("%c ", cs[a[r][c]]);
			}
			printf("\n");
		}

	}

	return 0;
}
