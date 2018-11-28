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
typedef vector<double> VDouble;
typedef pair<int, int> PInt;
typedef vector<PInt> VPInt;
typedef vector<string> VString;
typedef set<int> SInt;
typedef map<int, int> MIntInt;

struct Case {
	int caseNo;
	Case(int caseNo=0) {
		this->caseNo = caseNo;
	}

	void solve() {
		int n;
		cin >> n;
		VString table(n);
		for(int i = 0; i < n; i++)
			cin >> table[i];

		VDouble wc(n, 0), lc(n, 0);
		VDouble wp(n), owp(n), oowp(n);
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < n; j++) {
				if(table[i][j]=='1')wc[i]++;
				if(table[i][j]=='0')lc[i]++;
			}
			wp[i] = wc[i]*1.0/(wc[i] + lc[i]);
		}
		for(int i = 0; i < n; i++) {
			double sum = 0.0;
			for(int j = 0; j<n; j++)
				if(table[i][j]!='.')
					sum += (wc[j] - (table[j][i]-'0'))*1.0/(wc[j]+lc[j]-1);
			owp[i] = sum/(wc[i]+lc[i]);
		}
		for(int i = 0; i < n; i++) {
			double sum = 0.0;
			for(int j = 0; j < n; j++)
				if(table[i][j]!='.')
					sum += owp[j];
			oowp[i] = sum / (wc[i]+lc[i]);
		}

		printf("Case #%d:\n", caseNo);
		for(int i = 0; i < n; i++)
			printf("%.15lf\n", (double)(0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]));
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
