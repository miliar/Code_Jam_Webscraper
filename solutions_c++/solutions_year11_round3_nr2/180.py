#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long int datum;

int main(void)
{
	int Tcase; cin >> Tcase;
	for(int t = 0; t < Tcase; ++t) {
		datum L, T, N, C; cin >> L >> T >> N >> C;
		vector<int> A;
		for(int c = 0; c < C; ++c) {
			int a; cin >> a;
			A.push_back(a);
		}
		datum ellp = 0L;

		vector<int> mali;
		for(int i = 0; i < N; ++i) {
			datum dist = A[i%C];
			datum begin = ellp;
			datum end = ellp + dist*2;

			datum mal = 0L;
			if(T <= begin) {
				// booster 100%
				mal = -dist;
			}
			else if(begin <= T && T <= end) {
				// booster [0%, 100%]
				mal = -(dist - (T-begin)/2);
			}
			mali.push_back(mal);
			ellp = end;
		}

		datum soln = ellp;
		sort(mali.begin(), mali.end());
		for(int i = 0; i < L; ++i) {
			soln += mali[i];
		}
		cout << "Case #" << (t+1) << ": " << soln << endl;
	}
	return 0;
}
