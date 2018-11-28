#include <iostream>
#include <vector>
using namespace std;

const int maxs = 128;

__int64 x[maxs], y[maxs];

int main()
{
	int N, n, i, j, k, u;
	__int64 A, B, C, D, M;
	freopen("aa.in", "r", stdin);
	freopen("aa.out", "w", stdout);
	cin >> N;
	for (i = 1; i <= N; i ++)
	{
		cin >> n;
		scanf("%I64u%I64u%I64u%I64u%I64u%I64u%I64u",&A,&B,&C,&D,&x[0],&y[0],&M);

		for (j = 1; j < n; j ++) {
			x[j] = (A*x[j-1] + B) % M;
			y[j] = (C*y[j-1] + D) % M;
			// printf("%I64u %I64u\n", x[j], y[j]); 
		}

		int ans = 0;
		for (j = 0; j < n; j ++) {
			for (k = j+1; k < n; k ++) {
				for (u = k+1; u < n; u ++) {
					if ((x[j]+x[k]+x[u])%3 == 0 && (y[j]+y[k]+y[u])%3 == 0) {
						//cout << x[j]+x[k]+x[u] << ' ' << y[j]+y[k]+y[u] << endl;
						ans ++;
					}
				}
			}
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}
