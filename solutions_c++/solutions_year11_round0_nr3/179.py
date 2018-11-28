#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <fstream>
using namespace std;

typedef long long ll;

ll xorsum (vector<ll>& v, int i, int j) {
	ll res = 0;
	for (int k = i; k < j; ++k)
		res ^= v[k];
	return res;
}

void main () {
	ifstream f ("input.txt");
	ofstream of ("output.txt");
	int T = 0;
	f >> T;
	for (int i = 0; i < T; ++i) {

		//read input
		int N = 0;
		f >> N;		
		vector<ll> C (N);
		for (int j = 0; j < N; ++j) {
			f >> C[j];
		}

		//sort
		sort (C.begin(), C.end());
		
		ll res = 0;
		for (int j = 0; j < N; ++j)
			res ^= C[j];

		if (res != 0) {
			cout << "Case #" << i+1 << ": NO" << endl;
			of << "Case #" << i+1 << ": NO" << endl;
		} else {
			int j = 1;
			for (j = 1; j < N-1; ++j) {
				if (xorsum(C, 0, j) == xorsum(C, j, N)) break;
			}
			res = 0;
			for (int k = j; k < N; ++k)
				res += C[k];
			cout << "Case #" << i+1 << ": " << res << endl;
			of << "Case #" << i+1 << ": " << res << endl;
		}
	}
	f.close();
	of.close();
	cin.get();
}