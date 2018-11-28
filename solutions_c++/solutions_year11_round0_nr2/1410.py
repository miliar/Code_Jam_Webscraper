#include <iostream>

using namespace std;

const int N = 26;
const int M = 101;

int con[N][N];
int opp[N][N];

int main() {

	freopen("B-large.in", "r", stdin);
	freopen("qb-large.out", "w", stdout);

	int Tc;

	scanf("%d", &Tc);

	for (int tc = 1; tc <= Tc; ++tc) {

		int c, d, n;
		char tmp[5], s[M];

		scanf("%d", &c);
		
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				con[i][j] = -1;
				opp[i][j] = -1;
			}
		}

		for (int i = 0; i < c; ++i) {
			scanf("%s", tmp);

			con[tmp[1] - 'A'][tmp[0] - 'A'] = con[tmp[0] - 'A'][tmp[1] - 'A'] = tmp[2] - 'A';
		}

		scanf("%d", &d);

		for (int i = 0; i < d; ++i) {
			scanf("%s", tmp);

			opp[tmp[1] - 'A'][tmp[0] - 'A'] = opp[tmp[0] - 'A'][tmp[1] - 'A'] = -2;
		}

		scanf("%d%s", &n, s);
		
		int arr[M], res[M], top;

		for (int i = 0; i < n; ++i) {
			arr[i] = s[i] - 'A';
		}
		
		top = 0;
		
		res[top] = arr[0];

		for (int i = 1; i < n; ++i) {
			
			if (top >= 0 && con[arr[i]][res[top]] >= 0) {
				res[top] = con[arr[i]][res[top]];
			} else {

				bool mark = false;
				for (int j = 0; j <= top; ++j) {
					if (opp[arr[i]][res[j]] == -2) {
						top = -1;
						mark = true;
					}
				}

				if (false == mark) {
					res[++top] = arr[i];
				}
			}

		//	cout<<"top="<<top<<endl;
			
		}

		printf("Case #%d: [", tc);

		for (int i = 0; i <= top; ++i) {
			printf("%c", res[i] + 'A');
			if (i < top) {
				printf(", ");
			}
		}

		printf("]\n");
	}

	return 0;
}


