#include <iostream	>
#include <string>
#include <vector>

#define FOR(i,a,b) for(int i=(a); i<(b); i++)

using namespace std;

int find(vector<int> &v, int val, int a) {
	FOR(i,a,50) {
		if(v[i] <= val) return i;
	}
	return -10000;
}

int main() {
	int T, N;
	cin >> T;
	FOR(q,1,T+1) {
		cin >> N;
		vector<int> v(N);
		FOR(i,0,N) {
			string s;
			cin >> s;
			int c = -1;
			FOR(j,0,N) if(s[j] == '1') c = j;
			v[i] = c;
		}
		int ret = 0;
		FOR(i,0,N) {
			if(v[i] > i) {
				int j = find(v, i, i+1);
				for(int k=j; k>i; k--) { 
					swap(v[k], v[k-1]); 
					ret++; 
				}
			}
		}

		cout << "Case #" << q << ": " << ret << endl;
	}
	return 0;
}