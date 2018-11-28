#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <stdio.h>
using namespace std;

#define FORIN(it, col) for(typeof (col).begin() it = (col).begin(); it != (col).end(); it++)
#define RANGE(col) (col).begin(), (col).end()
#define SUBSTR(s, from, to) (s).substr((from), (to)-(from))

typedef long long ll;
typedef vector<int> VInt;
typedef vector<VInt> VVInt;
typedef vector<bool> VBool;
typedef vector<VBool> VVBool;
typedef vector<char> VChar;
typedef vector<VChar> VVChar;
typedef pair<int, int> PInt;
typedef vector<PInt> VPInt;
typedef set<int> SInt;
typedef map<int, int> MIntInt;
typedef vector<double> VDouble;

struct Case {
	int caseNo;
	Case(int caseNo=0) {
		this->caseNo = caseNo;
	}

	VDouble pos;
	int c;
	double d;

	bool possible(double t) {
		double coord = pos[0] - t;
		for(int i = 1; i < pos.size(); i++) {
			coord = max(coord+d, pos[i]-t);
			if(coord>pos[i]+t) return false;
			//fprintf(stderr, "%lf\n", coord);
		}
		//fprintf(stderr, "true\n");
		return true;
	}

	double getAns() {
		if(possible(0)) return 0.0;
		double low=0, high = 1e13;
		while((high-low)>1e-8) {
			double mid = (high + low)/2.0;
			if(possible(mid)) high = mid;
			else low = mid;
		}
		fprintf(stderr, "%lf %lf\n", high, low);
		return (high+low)/2.0;
	}

	void solve() {
		cin >> c >> d;
		for(int i = 0; i < c; i++) {
			int p, v;
			cin >> p >> v;
			while(v--)
				pos.push_back((double)p);
		}
		printf("Case #%d: %.16lf\n", caseNo, getAns());
	}
};

int main()
{
	try {
		int testCount;
		cin >> testCount;
		for(int i = 1; i <= testCount; i++) {
			Case c(i);
			// cerr << "solving " << i << endl;
			c.solve();
		}
	} catch(const char *msg) {
		cerr << "EXCEPTION: " << msg << endl;
		return 1;
	}
	return 0;
}
