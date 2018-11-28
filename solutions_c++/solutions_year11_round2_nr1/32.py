#include<algorithm>
#include<cassert>
#include<complex>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<string>
#include<vector>
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,n) for(int i=0;i<(n);++i)
#define fup FOR
#define fdo FORD
#define VAR(v,i) __typeof(i) v=(i)
#define FORE(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define ALL(x) (x).begin(),(x).end()
#define SIZE(x) ((int)(x).size())
#define siz SIZE
#define CLR memset((x),0,sizeof (x))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define SQR(a) ((a)*(a))

#define DEBUG 1
#define debug(x) {if(DEBUG) cerr << #x << " = " << x << endl;}
#define debugv(x) {if(DEBUG) {cerr << #x << " = "; FORE(it,(x)) cerr << *it << " . "; cerr  <<endl;}}

using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef VI vi;
typedef LL lli;

const int inf = 1000000000;
char C[200][200];
int w[200];
int p[200];
double owp[200];
double oowp[200];

void solve(int tcase) {
    printf("Case #%d:\n", tcase);
    int n;
    scanf("%d", &n);
    char c=0;
    REP(i, n) w[i]=p[i]=0;
    REP(i, n) {
        while(c!='0' && c!='1' && c!='.') c =getchar();
        REP(j, n) {
            C[i][j]=c;
            if (c != '.') ++p[i];
            if (c == '1') ++w[i];
            c=getchar();
        }
        
    }
    REP(i, n) {
        double r = 0;
        REP(j, n) {
            if (C[i][j] != '.') {
                r += double (w[j]-(C[i][j]=='0'))/(p[j]-1);
            }
        }
        owp[i] = r/p[i];
    }
    REP(i, n) {
        double r  = 0;
        REP(j, n) {
            if (C[i][j] != '.') r+=owp[j];
        }
        oowp[i]=r/p[i];
    }
    REP(i, n) {
        printf("%.12lf\n", 0.25*(double)w[i]/p[i]+0.5*owp[i]+0.25*oowp[i]);
    }

}

int main() {
    int t;
    scanf("%d", &t);
    REP(i, t) solve(i+1);
    return 0;
}
