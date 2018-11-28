#include <string>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <iostream>
#include <sstream>
#include <numeric>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;

#define CLR(x) memset((x),0,sizeof(x))
#define SET(x,y) memset((x),(y),sizeof(x))
#define REP(i,x) for(int i=0;i<(x);i++)
#define FOR(i,x,y) for(int i=(x);i<(y);i++)
#define VI vector<int> 
#define PB(i,x) (i).push_back(x)
#define MP(x,y) make_pair((x),(y))

int T, A1, B1, A2, B2;

int getsg(int a, int b)
{
    if(a<b)swap(a,b);
    if(a==b) return 0;
    else if((a%b)==0) return 1;
    int r=a/b-1, g=getsg(a%b,b);
    if(r<g)return r;
    else return r+1;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);
    scanf("%d", &T);
    FOR(cas,1,T+1){
        scanf("%d %d %d %d", &A1, &A2, &B1, &B2);
        long long ans = 0;
        FOR(i,A1,A2+1) FOR(j,B1,B2+1){
            ans += getsg(i,j)>0;
        }
        printf("Case #%d: %I64d\n", cas, ans);
    }
    return 0;
}
