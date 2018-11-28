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

const int limit = 1000000;
VInt primes;
bool marks[limit];

struct Case {
	int caseNo;
	Case(int caseNo=0) {
		this->caseNo = caseNo;
	}

	void solve() {
        ll n;
        scanf("%Ld", &n);
        int ans = 1;
        for(VInt::iterator p = primes.begin(); p != primes.end() && (*p)*(ll)(*p) <= n; p++) {
            ll cur = (*p)*(ll)(*p);
            while(cur <= n) {
                ans++;
                cur *= (*p);
            }
        }

        if(n==1)ans=0;
        printf("Case #%d: %d\n", caseNo, ans);
	}
};

int main()
{
    fprintf(stderr, "Primes...\n");
    for(int i = 2; i < limit; i++) {
        if(marks[i])continue;
        primes.push_back(i);
        for(int j = 2*i; j < limit; j+=i)
            marks[j] = true;
    }
    fprintf(stderr, "Done primes\n");
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
