#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#include <boost/lexical_cast.hpp>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
typedef long long int ll;

ll count_recycled(int x, int a) {
    string x_string = boost::lexical_cast<string>(x);
    int n = x_string.size();
    x_string += x_string;
    set<int> pairs;
    for(int i = 0; i < n; ++i) {
        if(x_string[i] == '0')
            continue;
        int y = boost::lexical_cast<int>(x_string.substr(i, n));
        if(a <= y && y <= x)
            pairs.insert(y);
    }
    return pairs.size() - 1;
}

ll solve(int a, int b) {
    ll ans = 0;
    for(int i = a; i <= b; ++i) {
        ans += count_recycled(i, a);
    }
    return ans;
}

int main() {
    int numberOfCases;
	cin >> numberOfCases;
	for(int testCase = 1; testCase <= numberOfCases; ++testCase) {
        int a, b;
		cin >> a >> b;
		cout << "Case #" << testCase << ": " << solve(a, b) << endl;
	}
}
/*
2
2
 1
2 3
 4
*/
