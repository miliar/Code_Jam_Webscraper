#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

const long long INF = 0x7f7f7f7f;
long long s[259][259];

long long mabs(long long x) {
	if (x < 0) return -x;
	return x;
}

long long mmax(long long a, long long b) {
	if (a > b) return a;
	return b;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

		long long t; cin >> t;

	for (long long e = 1; e<=t; ++e) {
		int n,k;
		char s[55][55];
		cin >> n >> k;
		cin.getline(s[0], 234243);
		for (int i=0; i<n; i++) {
			cin.getline(s[i], 234243);
		}

		for (int i=n-1; i>=0; i--) {
			int end = n-1;
			for (int u=n-1; u>=0; --u) {
				if (s[i][u] != '.') {
					s[i][end] = s[i][u];
					if (u != end)
						s[i][u] = '.';
					--end;
				}
			}
		}

		bool red = false;
		bool blue = false;

		for (int i=0; i<n; i++) {
			for (int u=0; u<n; u++) {
				if (s[i][u] != '.') {

					// 1
					bool can = true;
					for (int t=1; t<k; t++) {
						if (u+t >= n || s[i][u+t] != s[i][u]) {
							can = false;
							break;
						}
					}

					if (!can) {
						can = true;
						for (int t=1; t<k; t++) {
							if (i+t >= n || s[i+t][u] != s[i][u]) {
								can = false;
								break;
							}
						}

						if (!can) {
							can = true;
							for (int t=1; t<k; t++) {
								if (i+t >= n || u+t >=n || s[i+t][u+t] != s[i][u]) {
									can = false;
									break;
								}
							}

							if (!can) {
								can = true;
								for (int t=1; t<k; t++) {
									if (i-t < 0 || u+t >=n || s[i-t][u+t] != s[i][u]) {
										can = false;
										break;
									}
								}
							}


						}
					}

					if (can) {
						if (s[i][u] == 'R')
							red = true;
						else blue = true;
					}
				}
			}
		}


		string ans;
		if (red && blue) {
			ans = "Both";
		} else if (red) {
			ans = "Red";
		} else if (blue) {
			ans = "Blue";
		} else ans = "Neither";

			

		cout << "Case #" << e << ": " << ans << endl;
	}


	//long long t; cin >> t;

	//for (long long e = 1; e<=t; ++e) {
	//	memset(s, 0x7f, sizeof s);
	//	long long d[266];

	//	long long D,I, m,n;
	//	cin >> D>> I >> m >> n;

	//	if (e == 72) {
	//		++n;
	//		--n;
	//	}

	//	for (long long i=0; i<n; i++) {
	//		cin >> d[i];
	//	}

	//	for (long long i=0; i<=256; i++) {
	//		s[i][0] = mabs(i-d[0]);
	//		if (n > 1 && D < s[i][0]) {
	//			s[i][0] = D;
	//		}
	//	}

	//	for (long long u=1; u<n; u++) {

	//		for (long long i=0; i<=255; i++) {
	//			long long diff = mabs(d[u] - i);
	//			long long mn = INF;
	//			for (long long t=0; t<=255; t++) {
	//				long long g = mabs(i - t);
	//				long long ins;
	//				if (m == 0) {
	//					ins = 100000000;
	//				} else {
	//					ins = mmax(0, (g-1) / m);
	//				}

	//				if (s[i][u] > s[t][u-1] + diff + ins * I) {
	//					s[i][u] = s[t][u-1] + diff + ins * I;
	//				}

	//			}
	//			
	//			if (s[i][u] > s[i][u-1] + D) {
	//				s[i][u] = s[i][u-1] + D;
	//			}
	//		}
	//	}

	//	long long mn = INF;

	//	for (long long i=0; i<=255; i++) {
	//		if (s[i][n-1] < mn) {
	//			mn = s[i][n-1];
	//		}
	//	}

	//	cout << "Case #" << e << ": " << mn << endl;
	//}

	return 0;
}