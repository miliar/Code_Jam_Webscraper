#include <iostream>
#include <cmath>

using namespace std;
void swap(int &a, int &b)
{
	int tmp = a;
	a = b;
	b = tmp;
}

int main()
{
	int T, N, S, P;
	int ti, q[100], r[100];
	int ans;
	int i, j, k;

	//freopen("D:\\VC2005\\GoogleCodeJam\\2012\\Q2\\B-large.in","r",stdin);
	//freopen("D:\\VC2005\\GoogleCodeJam\\2012\\Q2\\large.txt","w",stdout);

	scanf("%d\n", &T);
	for (i = 1; i <= T; ++i) {
		scanf("%d %d %d", &N, &S, &P);
		for (j = 0; j < N; ++j) {
			scanf("%d", &ti);
			q[j] = ti/3;
			r[j] = ti%3;
		}
		scanf("\n");

		for (j = 0; j < N; ++j) {
			for (k = j + 1; k < N; ++k) {
				if (q[k] > q[j]) {
					swap(q[k], q[j]);
					swap(r[k], r[j]);
				}
				else if (q[k] == q[j] && r[k] > r[j]) {
					swap(q[k], q[j]);
					swap(r[k], r[j]);
				}
			}
		}
		
		//for (j = 0; j < N; ++j)
		//	printf("%d %d\n", q[j], r[j]);

		ans = 0;
		for (j = 0; j < N; ++j) {
			if (q[j] >= P) {
				++ans;
			}
			else {
				if (r[j] == 0 && q[j] > 0 && S > 0) {
					if (P <= q[j] + 1 && q[j] + 1 <= 10) {
						++ans;
						--S;
					}
				}
				else if (r[j] == 1 && P <= q[j] + 1) {
					++ans;
				}
				else if (r[j] == 2) {
					if (P <= q[j] + 1) {
						++ans;
					}
					else if (S > 0 && P <= q[j] + 2 && q[j] + 2 <= 10) {
						++ans;
						--S;
					}
				}
			}
		}

		printf("Case #%d: %d\n", i, ans);
	}

	//fclose(stdin);
	//fclose(stdout);
}
