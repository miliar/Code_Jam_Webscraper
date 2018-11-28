#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
const int INF = 1000000000;
typedef long long int LL;

int main() {
    ios_base::sync_with_stdio(false);
    int t;
	cin >> t;
	for(int testCase = 1; testCase <= t; ++testCase) {
	    int n;
	    cin >> n;
	    int x = 0;
	    int min_elem = INF;
	    int sum = 0;
	    for(int i = 0; i < n; ++i) {
	        int e;
	        cin >> e;
	        sum += e;
	        x ^= e;
	        min_elem = min(min_elem, e);
	    }
        cout << "Case #" << testCase << ": ";
        if(x == 0)
            cout << sum - min_elem;
        else
            cout << "NO";
        cout << endl;
    }
}
