#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>

#define FOR(i,a,b) for(int i=(a); i<(b); i++)

using namespace std;

long long licz(vector<int>& v, int m, int M) {
	if(v.size() == 0) return 0;
	int d = min(v[0]-m, M-v[0]);
	int d2 = 0;
	FOR(i,1,v.size()) {
		int dd = min(v[i]-m, M-v[i]);
		if(dd > d) {
			d = dd;
			d2 = i;
		}
	}

	vector<int> v1, v2;
	FOR(i,0,v.size()) {
		if(v[i] < v[d2]) v1.push_back(v[i]);
		if(v[i] > v[d2]) v2.push_back(v[i]);
	}
	return M-m + licz(v1, m, v[d2]-1) + licz(v2, v[d2]+1, M);
}

long long licz2(vector<int>& v, int m, int M) {
	if(v.size() == 0) return 0;
	long long ret = -1;
	FOR(d2,0,v.size()) {
		vector<int> v1, v2;
		FOR(i,0,v.size()) {
			if(v[i] < v[d2]) v1.push_back(v[i]);
			if(v[i] > v[d2]) v2.push_back(v[i]);
		}
		long long cur = M-m + licz2(v1, m, v[d2]-1) + licz2(v2, v[d2]+1, M);
		if(ret == -1 || cur < ret) ret = cur;
	}
	return ret;
}

int main() {
	int T;
	cin >> T;
	FOR(q,1,T+1) {
		int P, Q;
		cin >> P >> Q;
		vector<int> rel(Q);
		FOR(i,0,Q) cin >> rel[i];
		long long ret = 0;
		ret = licz2(rel, 1, P);
		cout << "Case #" << q << ": " << ret << endl;
	}

	return 0;
}
