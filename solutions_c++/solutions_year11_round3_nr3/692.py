#include <iostream>
#include <array>
#include <vector>
#include <cassert>
#include <cmath>
#include <string>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <iomanip>
#include <list>
#include <set>
#include <map>

using namespace std;

int64_t Solve(int64_t L,int64_t H,const vector<int64_t> & ai) {
	for (int64_t i = L;i <= H;++i) {
		bool state = true;
		for (int j=0;j < ai.size();++j)
			if (! (i%ai[j] == 0 || ai[j] % i ==0)) state = false;
		if (state) return i;
	}
	return -1;
}

int main(int argc, char **argv) {
	cout << fixed << setprecision(12);
	int T;
	cin >> T;

	for(int i=0;i < T;++i) {
		int64_t N,L,H;
		cin >> N >> L >> H;
		vector<int64_t> ai(N);
				
		for (int j=0;j < N;++j) {
			cin >> ai[j];
		}
		
		int64_t ans = Solve(L,H,ai);
		cout << "Case #" << i+1 << ": ";
		if (ans == -1) cout << "NO" << endl;
		else cout << ans << endl;
	}
	
    return 0;
}
