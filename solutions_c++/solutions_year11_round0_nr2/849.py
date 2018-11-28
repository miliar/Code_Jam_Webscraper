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

char comb[4];
char opp[3];
char inp[105];
const int ALF=26;

char C[ALF][ALF];
bool O[ALF][ALF];
int res[105];

void solve(int tcase) {
    printf("Case #%d: ", tcase);
    REP(i,ALF) {
        REP(j,ALF) {
            C[i][j]=-1;
            O[i][j]=false;
        }
    }
    int c,d,n;
    scanf("%d",&c);
    REP(i,c) {
        scanf("%s", comb);
        REP(t, 3) comb[t]-='A';
        C[comb[0]][comb[1]] = C[comb[1]][comb[0]] = comb[2];
    } 
    scanf("%d",&d);
    REP(i,d) {
        scanf("%s",opp);
        opp[0]-='A';
        opp[1]-='A';
        O[opp[0]][opp[1]]=O[opp[1]][opp[0]] = true;
    }
    scanf("%d%s", &n, inp);
    int j = 0;
    REP(i, n) {
        inp[i]-='A';
        if (j > 0 && C[inp[i]][res[j-1]] != -1) {
            res[j-1] = C[inp[i]][res[j-1]];
        } else {
            bool done=false;
            REP(t, j) {
                if (O[res[t]][inp[i]]) {
                    j = 0;
                    done = true;
                }
            }
            if (!done) res[j++]=inp[i];
        }
    }
    printf("[");
    REP(i, j) {
        if (i > 0) printf(", ");
        printf("%c", res[i]+'A');
    }
    printf("]\n");


}

int main() {
    int t;
    scanf("%d", &t);
    REP(i, t) solve(i+1);
    return 0;
}
