#include <cstdio>
#include <algorithm>
#include <cctype>
#include <cstring>
#include <cmath>
#include <list>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <climits>

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define FORQ(i,a,b) for (int i=(a);i<=(b);++i)
#define FORD(i,a,b) for (int i=(a)-1;i>=(b);--i)
#define FORDQ(i,a,b) for (int i=(a);i>=(b);--i)
#define FORE(i,x) for (__typeof__((x).begin()) i=(x).begin();i!=(x).end();++i)
#define MP make_pair
#define F first
#define S second
#define PB push_back

using namespace std;

typedef long long LL;

vector<int> R;
bool tabW[1000];

bool isW(int a,int b) {
    R.clear();
    while (a!=b) {
        if (a>b) swap(a,b);
        R.PB((b%a == 0) ? b/a - 1 : b/a);
        if (b%a == 0) {
            b = a;
        } else
            b = b%a;
    }
    R.PB(1);
    reverse(R.begin(), R.end());
    tabW[0] = false;
    FOR(i,1,R.size()) {
        if (tabW[i-1] == false)
            tabW[i] = true;
        else {
            if (R[i] == 1)
                tabW[i] = false;
            else
                tabW[i] = true;
        }
    }
    return tabW[R.size()-1];
}

int main() {
    int lw;
    scanf("%d",&lw);
    FORQ(l,1,lw) {
        int a1,a2,b1,b2;
        scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
        int res = 0;
        FORQ(a,a1,a2)
            FORQ(b,b1,b2) 
                res += isW(a,b) ? 1 : 0;
        printf("Case #%d: %d\n",l,res);
    }
    return 0;
}
