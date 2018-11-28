#include <iostream>
#include <algorithm>
#include <numeric>
#include <limits>
#include <vector>
#include <set>
#include <map>
#include <string>
using namespace std;
#include <stdio.h>

#define forin(it, col) for(typeof (col).begin() it = (col).begin(); it != (col).end(); it++)
#define range(col) (col).begin(), (col).end()
#define substr(s, from, to) (s).substr((from), (to)-(from))

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
typedef vector<VDouble> VVDouble;

struct Triple {
    int b, e, w;
    double tRun;
    Triple(int _b=0, int _e=0, int _w=0): b(_b), e(_e), w(_w), tRun(0.0) {}
    bool operator<(const Triple &other) const {
        return w < other.w;
    }
};

struct Case {
	int caseNo;
	Case(int caseNo=0) {
		this->caseNo = caseNo;
	}

	void solve() {
        int length, s, r, t, n;
        scanf("%d%d%d%d%d", &length, &s, &r, &t, &n);
        vector<Triple> triples(n);
        for(int i = 0; i < n; i++)
            scanf("%d%d%d", &triples[i].b, &triples[i].e, &triples[i].w);

        // get the base time
        vector<Triple> parts;
        int cur = 0;
        for(int i = 0; i <n; i++) {
            parts.push_back(Triple(cur, triples[i].b, 0));
            parts.push_back(triples[i]);
            cur = triples[i].e;
        }
        parts.push_back(Triple(cur, length, 0));
        sort(parts.begin(), parts.end());

        // be greedy
        double ans = 0.0;
        double tLeft = t;
        for(vector<Triple>::iterator it = parts.begin(); it != parts.end(); it++) {
            it->tRun = min(tLeft, (it->e - it->b)*1.0/(it->w + r));
            tLeft -= it->tRun;
            ans += (it->e-it->b)*1.0/(it->w+s) - it->tRun * (r-s)*1.0/(it->w+s);
        }

        printf("Case #%d: %.15lf\n", caseNo, ans);
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
