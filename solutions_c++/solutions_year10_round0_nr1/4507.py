#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <cstring>

using namespace std;

#define MP make_pair
#define FF first
#define SS second
#define SZ size()
#define PB push_back
#define all(x) (x).begin(), (x).end()
#define FORZ(i, n) for(typeof(n) i = 0 ; i !=n ; i++)
#define FORE(i, a, b) for(typeof(a) i = a ; i <= b ; i++)
#define tr(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define dbg(x) cout << #x << " : " << x << "; " << flush;
#define dbge(x) cout << #x << " : " << x << ";" << endl;
int GI() {int t; scanf("%d", &t); return t;}
typedef long long LL;
typedef pair <int, int> II;
typedef vector <int> VI;


int main () {
    int T = GI();
    FORZ(test, T) {
	int N = GI(), K = GI();
	int bit = 0;
	while(K--) {
	    int next = bit + 1;
	    if(!(next & (next-1))) {
		++bit;
		if(bit >= 1 << N)
		    bit = 0;
	    } else {
		next = ~bit;
		int ind = next & -next;
		bit |= ind;
		--ind;
		bit &= ~ind;
	    }
	}
	printf("Case #%d: %s\n", test+1, (bit+1) == (1 << N) ? "ON" : "OFF");
    }
    return 0;
}
