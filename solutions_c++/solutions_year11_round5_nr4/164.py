#include <iostream>
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
    int cases;
    cin >> cases;
    for (int cs = 1; cs <= cases; cs++) {
	cerr << cs << endl;
	cout << "Case #" << cs << ": ";

	string s;
	cin >> s;
	vector<int> d;

	long long otaznik = 0;
	long long jednotka = 0;
	REP(i, s.size()) {
	    int j = s.size()-i-1;
	    if (s[i] == '?') 
		otaznik |= (1ll << j);
	    if (s[i] == '1')
		jednotka |= (1ll << j);

	}


	for (long long res = 1; ; res++) {

	    long long sqr = res*res;
	    if (((sqr^jednotka) | otaznik) == otaznik) {

		list<int> r;
		while (sqr) {
		    r.push_front(sqr & 1);
		    sqr >>= 1;
		}
		FOREACH(x, r)
		    cout << *x;
		cout << endl;
		break;
	    }

	}
    }
}
