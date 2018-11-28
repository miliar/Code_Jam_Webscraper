#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cfloat>
#include <cctype>
#include <algorithm>
#include <sstream>
#include <bitset>

#define REP(i,a) for(i=0;i<a;++i)
#define FOR(i,a,b) for(i=a;i<=b;++i)
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define sz(x) (int)(x).size()
using namespace std;

int gcd(int a,int b){
    if(a % b == 0){
        return b;
    }

    return gcd(b,a%b);
}



void main() {
	int T;
	cin >> T;

	int i;
	REP(i,T) {
		long long n;
		int pd,gd;
		cin >> n >> pd >> gd;

		if (gd == 100 && pd != 100) {
			cout << "Case #" << i+1 << ": Broken" << endl;
			continue;
		} else if (pd == 0 && gd < 100) {
			cout << "Case #" << i+1 << ": Possible" << endl;
			continue;
		} else if (pd != 0 && gd == 0) {
			cout << "Case #" << i+1 << ": Broken" << endl;
			continue;
		}

		int gcdpd = gcd(100, pd);

		int pd2 = 100 / gcdpd;

		if (pd2 <= n) {
			cout << "Case #" << i+1 << ": Possible" << endl;
		} else {
			cout << "Case #" << i+1 << ": Broken" << endl;
		}
	}
}