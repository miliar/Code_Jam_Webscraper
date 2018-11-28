
#include <iostream>
//#include <conio.h>
#include <vector>
#include <string>
#include <list>
#include<cstdio>
#include <numeric>
#include <cstring>
#include <set>
#include <queue>
#include <stack>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <time.h>
#include <bitset>
#include <algorithm>

using namespace std;

#define FOR(i, a, b) for(i=(a); i<(b); i++)
#define IFOR(i, a, b) for(i=(a); i>=(b); i--)
#define FORD(i, a, b, c) for(i=(a); i<(b); i+=(c))
#define REP(i, n) for(i=0; i<(n); i++)
#define MAX(a, b) ((a)>(b)?(a):(b))
#define MIN(a, b) ((a)<(b)?(a):(b))
#define P printf
#define S scanf
#define SZ(x) ((int)x.size())
#define PB(x) push_back(x)
#define INF 1000000000
#define V vector
typedef V<int> VI;
typedef V<string> VS;
typedef long long LL;
typedef pair<int, int> PII;
int aa[2000], bb[2000];
main()
{
    freopen("my.in","r", stdin);
    freopen("out.txt","w", stdout);
    int k, t,a, b,i, j, ans,n;
    cin>>t;
    REP(k, t){
        cin>>n;
        ans=0;
        REP(i, n){
            cin>>a>>b;
            REP(j, i){
               if(aa[j]>a && bb[j]<b || aa[j]<a && bb[j]>b) ans++;
            }
            aa[i]=a;
            bb[i]=b;
        }
        P("Case #%d: %d\n", k+1, ans);
    }
}


