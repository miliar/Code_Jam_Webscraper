
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set>
#include<queue>
#include<cstring>
#include<stack>
#include<sstream>
#include<complex>
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define DEBU true
#define debug(x) { if (DEBU) cerr << #x << " = " << x << "\n"; }
#define debugv(x) { if (DEBU) { cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n"; } }
#define fup(i,a,b) for(int i=(a);i<=(b);i++)
#define fdo(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset((x),0,sizeof (x))
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) ((int)a.size())
#define inf 1000000000
#define SQR(a) ((a)*(a))

using namespace std;
typedef long long lli;
typedef double ld;

string base = "QWERASDF";
int ile[200];
char t[200][200];
bool bad[200][200];
vector<char> odp;

int main() {
    int cas;
    cin >> cas;
    fup(ca, 1, cas) {
        CLR(t);
        CLR(bad);

        int n;
        cin >> n;
        fup(i, 1, n) { char a, b, c; cin >> a >> b >> c; t[a][b] = t[b][a] = c; }
        cin >> n;
        fup(i, 1, n) { char a, b; cin >> a >> b; bad[a][b] = bad[b][a] = 1; }
        cin >> n;
        string s;
        cin >> s;
        CLR(ile); 
        odp.clear();
        fup(i, 0, siz(s) - 1) {
            char c = s[i];
            if (odp.empty()) {
                odp.push_back(c); 
                ile[c]++;
                continue;
            } 
            char e = odp.back();
            if (t[e][c]) {
                ile[e]--;
                odp.pop_back();
                odp.push_back(t[e][c]);
            } else {
                bool dupa = 0;
                FORE(d, base) {
                    if (ile[*d] > 0 && bad[*d][c]) { dupa = 1; break; }
                }
                if (dupa) {
                    odp.clear();
                    FORE(d, base) { ile[*d] = 0; }
                } else {
                    odp.push_back(c);
                    ile[c]++;
                }
            }
        }

        printf("Case #%d: [", ca);
        fup(i, 0, siz(odp) - 1) {
            if (i) printf(", ");
            printf("%c", odp[i]);
        }
        printf("]\n");



    }

	return 0;
}


