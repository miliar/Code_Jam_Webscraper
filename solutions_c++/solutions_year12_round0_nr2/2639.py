#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

typedef vector <   int  > vi;
typedef vector <   vi   > vvi;
typedef vector < double > vd;
typedef vector <   vd   > vvd;
typedef vector < string > vs;

int main () {
	int T; cin >> T;

	vector<int> up (31,1);
	up[0] = 0;
	up[1] = 0;
	up[4] = 0;
	up[10] = 0;
	up[13] = 0;
	up[16] = 0;
	up[19] = 0;
	up[22] = 0;
	up[25] = 0;
	up[28] = 0;
	up[29] = 0;
	up[30] = 0;

	for (int t = 1; t <= T; t++) {
		int N, S, p, x, ans = 0, sum = 0; cin >> N >> S >> p;
		
		vector<int> T (N,0);
		for (int i = 0; i < N; i++) {
			cin >> x;
			T[i] = (int) ceil(x/3.);
			
			//cout << x << " " << T[i] << endl;

			if (T[i] >= p)
				ans++;
			if ((T[i] == p - 1) && (up[ x ] == 1))
				sum++;
		}

		ans += min (sum, S);
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
