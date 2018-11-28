#include <cstdlib>
#include <cstring>
#include <memory>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <climits>
#include <cfloat>
using namespace std;

#define DEBUG_FLAG 1
#if DEBUG_FLAG
#define dbg(...) cerr << #__VA_ARGS__ << ": " << __VA_ARGS__ << endl
#define cdbg(...) cerr << __VA_ARGS__ << endl
#else
#define debug(r)
#define dbg(...)
#endif

const int S1=1001;
const int S2=3001;
typedef long long LL;

int gcd(int x, int y) {
    if (y==0) return x;
    return gcd(y, x%y);
}

bool judge(int a, int b) {
    if(a==b) return false;
    if(a<b) {
        int tmp=a;
        a=b;
        b=tmp;
    }
    int m=a%b;
    int g=gcd(a,b);
    if(m==0) {
        return true;
    }
    if (m==g && a/b > 1) {
        return true;
    }
    if((b-m) == g && m != g) {
        return true;
    }
    bool j=judge(b,a%b);
    bool h=true;
    if(a-b>b) h=judge(a%b+b,b);
    if(j==false || h==false) {
        return true;
    } else {
        return false;
    }
}

int main() {
	string fname = "C-small-attempt3";
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	int T;
    
	scanf("%d", &T);
	for (int c = 1; c <= T; ++c) {
		int a1,a2,b1,b2;
        
		scanf("%d %d %d %d", &a1,&a2,&b1,&b2);
        
        int a,b;
        LL count = 0;
        a=a1;
        b=b1;
        cerr << "Case ++++++++++++++++++" << c << endl;
        for (a=a1; a<=a2; a++) {
            for (b=b1; b<=b2; b++) {
                if (judge(a,b)) {
                    count++;
                    dbg(a);
                    dbg(b);
                }
            }
        }
        
        printf("Case #%d: %lld\n", c, count);
	}
    
	return 0;
}

