#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <assert.h>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long LL;
typedef vector<LL> VL;
typedef vector<string> VS;
typedef vector<int> VI;
typedef vector< VI > VVI;
typedef stringstream SS;
typedef istringstream ISS;
typedef ostringstream OSS;
#define FOR(i,a,b) for(int i = (a); i < int(b); ++i)
#define SZ(v) ((int)(v).size())
bool small(int i1, int i2) {
    return i1>i2;
}
int getMinStroke(int P, int K, int L,  VI& fres) {
    int ret = -1;
    // if (P*K<L),0
    sort(fres.begin(), fres.end(), small);
    VI cnt(K, 0);
    int curKey = 0;
    int curChar = 0;
    int num = 0;
    while(curChar < L) {
        cnt[curKey]++;
        if (cnt[curKey] > P)
            return -1;
        num += cnt[curKey]*fres[curChar];
        curKey++;
        if (curKey == K)
            curKey = 0;
        curChar ++;
    }
    return num;
}
void main() {
    freopen("A-small-attempt0.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; ++i) {
        int P,K,L,v;
        scanf("%d %d %d", &P, &K, &L);
        VI fres;
        for (int j = 0; j < L; ++j) {
            scanf("%d",&v);
            fres.push_back(v);
        }
        int mn = getMinStroke(P,K,L, fres);
        if (mn == -1)
            printf("Case #%d: Impossible\n", i+1);
        else
            printf("Case #%d: %d\n", i+1,  mn);
    }
}