#include<set>
#include<map>
#include<cmath>
#include<cstdio>
#include<vector>
#include<string>
#include<iostream>
#include<sstream>
#include<algorithm>
using namespace std;
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)
#define FORE(i,a) for(typeof(a.begin()) i = a.begin(); i!= a.end(); ++i)
#define SET(x,v) memset(x,v,sizeof(x))
#define cs c_str()
#define sz size()
#define mp make_pair
#define pb push_back

typedef long long i64;
vector<int> x, y;
int main() {
    freopen("A.in","r",stdin);
    FILE *fp=fopen("A.out","w");
    int e = 0, T, n;
    scanf("%d",&T);
    while (T--) {
        scanf("%d",&n);
        x.resize(n);
        y.resize(n);
        FOR(i,0,n) scanf("%d",&x[i]);
        FOR(i,0,n) {
            scanf("%d",&y[i]);
            y[i]=-y[i];
        }
        sort(x.begin(), x.end());
        sort(y.begin(), y.end());
        i64 sum = 0;
        FOR(i,0,n) {
            i64 X = x[i];
            i64 Y = -y[i];
            sum += X*Y;
        }
	++e;
        printf("Case #%d: %lld\n",e, sum);
	fprintf(fp,"Case #%d: %lld\n",e, sum);
    }
    fclose(fp);
    return 0;
}

