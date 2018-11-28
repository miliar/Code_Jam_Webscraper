#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdlib>

using namespace std;

int triple(int n)
{
	if(n < 3) return 0;
	return n * (n-1) * (n-2) / 6;
}

int main(void)
{
	int N;
	cin >> N;
	for(int nn = 0; nn < N; ++nn) {
		int result = 0;
		long long X, Y;
		long long n, x0, y0, A, B, C, D, M;
		int count[11];

		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

		X = x0;
		Y = y0;

		for(int i = 0; i < sizeof(count)/sizeof(count[0]); ++i) count[i] = 0;
		for(int i = 0; i < n; ++i) {
//			cerr << X << ':' << Y << endl;

			++count[(X % 3) * 3 + (Y % 3) + 1];

			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
		}

//		for(int i = 1; i <= 9; ++i) cerr << i << ':' << count[i] << endl;

		for(int i = 1; i <= 9; ++i) {
			for(int j = i; j <= 9; ++j) {
				for(int k = j; k <= 9; ++k) {
					if((((i-1)/3 + (j-1)/3 + (k-1)/3) % 3) == 0 && (((i-1)%3 + (j-1)%3 + (k-1)%3) % 3) == 0) {
//						cerr << i << ':' << j << ':' << k << endl;
						if(i == j && j == k) {
							result += triple(count[i]);
						} else {
							result += count[i]*count[j]*count[k];
						}
					}
				}
			}
		}

		cout << "Case #" << nn+1 << ": " << result << endl;
	}
	return 0;
}
