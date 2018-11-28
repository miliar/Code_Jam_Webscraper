#include <iostream>
#include <iterator>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

#include <cmath>

//#include "lib.hpp"

typedef unsigned long long ULL;
typedef long long LL;

using namespace std;

int mymin(int n1, int n2)
{
	if(n1 >= 0 && n2 >= 0) return min(n1, n2);
	else if(n1 < 0) return n2;
	else return n1;
}

int getnum(int type, int v, vector<int> &num, int i)
{
	int res;
	if(type) { // AND
//cerr << "AND";
		if(v) {
			if(num[2*i+1] < 0 || num[2*i+2] < 0) res = -1;
			else res = num[2*i+1]+num[2*i+2];
		} else { // v == 0
			if(num[2*i+1] < 0 && num[2*i+2] < 0) res = -1;
			else res = mymin(num[2*i+1], num[2*i+2]);
		}
	} else { // OR
//cerr << "OR";
		if(v) {
			if(num[2*i+1] < 0 && num[2*i+2] < 0) res = -1;
			else res = mymin(num[2*i+1], num[2*i+2]);
		} else { // v == 0
			if(num[2*i+1] < 0 || num[2*i+2] < 0) res = -1;
			else res = num[2*i+1]+num[2*i+2];
		}
	}
	return res;
}

int main(void)
{
	int n;
	cin >> n;
	for(int nn = 0; nn < n; ++nn) {
		int result = 0;

		int m,v;
		cin >> m >> v;
		vector<int> type(m);
		vector<int> change(m);
		vector<int> value(m);
		vector<int> num(m);
		for(int i=0;i<(m-1)/2;++i) {
			cin >> type[i] >> change[i];
//			cerr << i << ',' << type[i] << ',' << change[i] << endl;
		}
		for(int i=0;i<(m+1)/2;++i) {
			cin >> value[i+(m-1)/2];
			change[i+(m-1)/2] = false;
			if(value[i+(m-1)/2] == v) num[i+(m-1)/2] = 0;
			else num[i+(m-1)/2] = -1;
//			cerr << i+(m-1)/2 << ' ' << value[i+(m-1)/2] << ' ' << num[i+(m-1)/2] << endl;
		}

		for(int i = (m-1)/2-1; i >= 0; --i) {
			if(change[i]) {
				int t = getnum(1-type[i], v, num, i);
				if(t >= 0) ++t;
				num[i] = mymin(getnum(type[i], v, num, i), t);
			} else { // unchange
				num[i] = getnum(type[i], v, num, i);
			}
//			cerr << i << ' ' << num[i] << endl;
		}

		if(num[0] >= 0) {
			cout << "Case #" << nn+1 << ": " << num[0] << endl;
		} else {
			cout << "Case #" << nn+1 << ": IMPOSSIBLE" << endl;
		}
	}
	
	return 0;
}
