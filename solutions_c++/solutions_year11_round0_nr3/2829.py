#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define FOR(i,a,b)  for(int i=(a);i<(b);i++)
#define dbg(e)  cout<<(#e)<<" : "<<e<<endl
#define set(v,i) memset(v,i,sizeof(v))
#define all(x) x.begin(),x.end()
#define sz(x) int((x).size())
#define REP(i,n) FOR(i,0,n)
#define pb  push_back
#define mp make_pair

typedef long long LL;

int n, C[20];

int main() {
    int test; scanf("%d",&test); REP(tt,test) {
        scanf("%d",&n);
        REP(i,n) scanf("%d",&C[i]);
        int sum = 0,best;
        bool ok;
        REP(i,n) sum ^= C[i];
        ok = (sum == 0);
        int add = 0,mini = 10000000;
        REP(i,n) add += C[i], mini = min(mini,C[i]);
        best = add - mini;
        printf("Case #%d: ",tt+1);
        if(ok) printf("%d\n",best);
        else printf("NO\n");
    }
}
