#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <numeric>

#include <cstdio>
#include <cmath>
#include <cctype>
#include <cstring>

#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

#define FOREACH(iter, cont) for(__typeof((cont).begin()) iter = (cont).begin(); iter != (cont).end(); iter++)
#define REP(i, end) for(int i = 0; i < (end); i++)
#define CLEAR(arr) memset(arr, 0, sizeof(arr))
#define ALL(cont) (cont).begin(),(cont).end()

int main() {

    vector<long long> prime;
    ifstream fprimes("primes1.txt");
    long long p;
    while (fprimes >> p) {
	prime.push_back(p);
    }

    int cases;
    cin >> cases;
    for (int cs = 1; cs <= cases; cs++) {
	cerr << cs << endl;

	long long n;
	cin >> n;
	long long res = 1;
	if (n == 1)
	    res = 0;
	else {
	    for (int i = 0; ; i++) {
		int a = 0;
		p = prime[i];
		while (p <= n) {
		    a++;
		    p *= prime[i];
		}
		if (a > 1)
		    res += a-1;
		else
		    break;
	    }
	}
	cout << "Case #" << cs << ": " << res << endl;
    }
}
