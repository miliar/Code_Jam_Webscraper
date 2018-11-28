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
		vector<int> C(N);
		int x=0;
		int z=2000000;
		int s=0;
		for(int i=0;i<N;i++) {
			int c;
			cin >> c;
			x^=c;
			z=min(z,c);
			s+=c;
		}
		
		if(x!=0)
			cout << "Case #" << K << ": NO" << endl;
		else
			cout << "Case #" << K << ": " << (s-z) << endl;
		cout.flush();
	}
	return 0;
}