// C++0x (GCC 4.6.1 20110325 (prerelease), -std=c++0x option)
#include <iostream>
#include <iomanip>
#include <vector>
#include <array>
#include <unordered_map>
#include <unordered_set>
#include <tuple>
#include <functional>
#include <cassert>
#include <sstream>
#include <algorithm>
using namespace std;


int main() {
	int T; cin >> T;
	for(int K=1;K<=T;K++) {
		int N; cin >> N;
		int NN=0;
		for(int i=1,j;i<=N;i++) {
			cin >> j;
			if(i!=j)
				NN++;
		}
		cout.precision(6);
		cout << fixed << "Case #" << K << ": " << (double)NN << endl;
		cout.flush();
	}
	return 0;
}