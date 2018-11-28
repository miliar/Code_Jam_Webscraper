#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <deque>
#include <complex>
#include <sstream>
#include <iomanip>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)
#define ll long long
#define F first
#define S second
#define PB push_back
#define MP make_pair
using namespace std;

const double PI = acos(-1.0);

int a[1011];

int main() {
    freopen("C1.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ntest; scanf("%d", &ntest);
    FOR(test,1,ntest) {
        if (test%10==0) cerr << test << endl;
        int n; scanf("%d", &n);
        FOR(i,1,n) scanf("%d", &a[i]);
        sort(a+1, a+n+1);
        
        int sum = 0, sum2 = 0;
        FOR(i,1,n) {
            sum = sum ^ a[i];
            sum2 += a[i];
        }
        
        cout << "Case #" << test << ": ";
        if (sum) puts("NO");
        else cout << sum2 - a[1] << endl;
    }
    return 0;
}
