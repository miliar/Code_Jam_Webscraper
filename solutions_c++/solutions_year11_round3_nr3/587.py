#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
#define pb push_back

vi pr;
bool B[10005];


int main() {
	int T;
//	freopen("c:\\in.txt", "r", stdin);
	freopen("c:\\C-small-attempt1 (2).in", "r", stdin);
	freopen("c:\\C-small-attempt1 (2).out", "w", stdout);

	B[0] = B[1] = true;
	for (int i = 2; i * i < 10005; ++i) {
		if (B[i] == true) continue;
		for (int j = i * i; j < 10005; j += i) {
			B[j] = true;
		}
	}
	for (int i = 0; i < 10005; ++i) {
		if (B[i] == false) {
			pr.push_back(i);
		}
	}

	scanf("%d", &T);


	for (int testCase = 1; testCase <= T; ++testCase) {
		int N;
		__int64 L, H;
		scanf("%d%I64d%I64d", &N, &L, &H);

		vector<__int64> nn;
		for (int i = 0; i < N; ++i) {
			__int64 k;
			scanf("%I64d", &k);
			nn.push_back(k);
		}

/*		int arr[10005] = {0, 0, 0};


		vector<__int64> nn;
		for (int i = 0; i < N; ++i) {
			__int64 k;
			scanf("%I64d", &k);
			nn.push_back(k);
			if (k == 1) continue;

			int b[10005] = {0};

			for (int j = 0; j < pr.size() && pr[j] * pr[j] <= k; ++j) {
				while (k % pr[j] == 0) {
					b[pr[j]]++;
					k /= pr[j];
				}
			}
			if (k > 1) {
				b[k]++;
			}
			for (int t = 0; t < 10005; ++t) {
				arr[t] = max(arr[t], b[t]);
			}
		}
		__int64 res = 1;
		for (int i = 0; i < 10005; ++i) {
			if (arr[i] > 0) {
				//for (int j = 0; j < arr[i]; ++j) {
					res *= i;
				//}
			}
		}

		bool ok = true;
		for (int i = 0; i < N; ++i) {
			if (res % nn[i] != 0 && nn[i] % res != 0) {
				ok = false;
				break;
			}
		}*/

		printf("Case #%d: ", testCase);

		__int64 res = -1;
		for (int i = L; i <= H; ++i) {
			bool e = true;
			if (testCase == 40 && i == 2310) {
				testCase = 40;
			}

			for (int j = 0; j < N; ++j) {
				if (nn[j] % i != 0 && i % nn[j] != 0) {
					e = false;
					break;
				}
			}
			if (e) {
				res = i;
				break;
			}
		}

		//printf ("%I64d %I64d %I64d\n", L, H, res);
//		if (!ok || L > res || res > H) {
		if (res == -1) {
			printf ("NO\n");
		} else {
			printf ("%I64d\n", res);
		}
	}

	return 0;
}