#include <iostream>
#include <iomanip>
#include <vector>
#include <math.h>
#include <map>
#include <string>

using namespace std;

typedef pair<int,int> p;

int calc(int idx, vector<int> &v) {
	int s=0;
	for (int j=0; j<20; j++) {
		if((idx>>j)&0x01 == 1) {
			s+= v[j];
		}
	}
	return s;
}

void prt(int idx, vector<int> &v) {
	bool flg = false;
	for (int j=0; j<20; j++) {
		if((idx>>j)&0x01 == 1) {
			if (flg) cout << " ";
			else flg = true;
			cout << v[j];
		}
	}
	cout << endl;
}

void each_case(int n, vector<int> &v) {
	map<int, int> m;
	int mx = 2 << 20;	
	int a;
	for (int i=1;i<mx; i++) {
		int ss = calc(i, v);
		if (m.find(ss) == m.end()) {
			m.insert(map<int, int>::value_type(ss, i));
		} else {
			a = m[ss];
			prt(i, v);
			prt(a, v);
			break;
		}
		
	}
}

int main(void) {
	int t;
	cin >> t;

	for (int i=0; i<t; i++) {
		int n;
		cin >> n;
		vector<int> v;
		for (int j=0; j<n; j++) {
			int tt;
			cin >> tt;
			v.push_back(tt);
			sort(v.begin(), v.end());
		}
		cout << "Case #" << (i+1) << ": " << endl;
		each_case(n, v);
	}

}
