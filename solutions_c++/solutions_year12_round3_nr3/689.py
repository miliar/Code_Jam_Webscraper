#include <iostream>
#include <iomanip>
#include <vector>
#include <math.h>
#include <map>
#include <string>

using namespace std;

typedef long long int lli;

typedef pair<lli, int> p;

bool pless(const p &left, const p &right) {
	 return left.second < right.second; 
}

bool ppless(const p &left, const p &right) {
	 return left.first < right.first; 
}

vector<p> shift(vector<p> &v) {
	int n = v.size();
	vector<p> vv(n-1);	
	copy(v.begin()+1, v.end(), vv.begin());
	return vv;
}

vector<p> safe_shift(vector<p> &v) {
	while (v.size() != 0) {
		if (v[0].second == 0) {
			v = shift(v);
		} else {
			break;
		}
	}
	return v;
}

long long int a_case(vector<p> &a, vector<p> &b, long long int sum) {
	a = safe_shift(a);
	b = safe_shift(b);
	if (a.size() == 0 || b.size() == 0) return sum;

	vector<p> aa = shift(a);
	vector<p> bb = shift(b);
	long long int sa, sb;
	if (a[0].second != b[0].second) {
		sa  = a_case(aa, b, sum);
		sb = a_case(a, bb, sum);
		return (sa > sb) ? (sa) : (sb);

	} else {
		long long int d = a[0].first;
		bool flg = (d > (b[0].first));
		if (flg) d = b[0].first;
		a[0].first -= d;
		b[0].first -= d;
		if (flg) {
			sa = a_case(a, bb, sum+d);
			return sa;
		} else {
			sb = a_case(aa, b, sum+d);
			return sb;
		}
	}

}

long long int each_case(vector<p> &a, vector<p> &b) {
	/*
	long long int max = -1;
	int an = a.size();
	for (int i=1; i<2<<an; i++) {
		vector<p> aa;
		if (i&0x01 == 1) {
			aa.push_back(a[0]);
		}
		if (((i>>1)&0x01) == 1 && an > 1) {
			aa.push_back(a[1]);
		}
		if (((i>>2)&0x01) == 1 && an > 2) {
			aa.push_back(a[2]);
		}
		long long int s = a_case(aa, b, 0);
		if (max < s) max = s;
	}
	return max;
	*/
	return a_case(a, b, 0);
}

int main(void) {
	int t;
	cin >> t;

	for (int i=0; i<t; i++) {
		int n, m;
		cin >> n >> m;
		int s = 0;
		vector<p> a, b;
		for (int j=0; j<n; j++) {
			lli a1;
			int a2;	
			cin >> a1 >> a2;
			a.push_back(p(a1, a2));
		}
		for (int j=0; j<m; j++) {
			lli b1;
			int b2;
			cin >> b1 >> b2;
			b.push_back(p(b1, b2));
		}
		cout << "Case #" << (i+1) << ": ";
		cout << each_case(a, b);
		cout << endl;
	}

}
