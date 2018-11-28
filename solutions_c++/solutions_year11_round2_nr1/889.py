using namespace std;
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <sstream>
#include <memory.h>
#include <iostream>
#include <algorithm>
#define FOR(i,n) for(__typeof(n) i=0;i<(n);i++)
#define FORab(i,a,n) for(__typeof(n) i=(a);i<=(n);i++)
#define FOR1(i,n) FORab(i,1,n)
#define pb push_back
#define ms(n,p) memset(n, (p), sizeof(n))
#define ms0(n) ms(n, 0)
#define sz(a) a.size()
#define all(a) a.begin(), a.end()
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long ll;

int played[110][110];
int win[110][110];
double wp[110];
double owp[110];
double oowp[110];
char mmap[110][110];

int main() {
    //freopen("A-small-attempt0.in" , "r", stdin);
    //freopen("A-small-attempt0.out" , "w", stdout);
    freopen("A-large.in" , "r", stdin);
    freopen("A-large.out" , "w", stdout);
    int t;cin>>t;
    FOR1(cno, t) {
        int n; cin>>n;
        FOR(i, n) FOR(j, n) { cin>>mmap[i][j]; }

        ms0(played);
        ms0(win);
        FOR(k, n+1) FOR(i, n) {
            if(i == k) continue;
            FOR(j, n) {
                if(j == k) continue;
                char a = mmap[i][j];
                if(a == '.') continue;
                played[k][i]++;
                if(a == '1') win[k][i]++;
            }
        }
        FOR(i, n) {
            wp[i] = win[n][i]/double(played[n][i]);

            owp[i] = 0;
            int cc=0;
            //cout<<"Counting owp of "<<i<<endl;
            FOR(j, n) {
                if(i == j) continue;
                if(mmap[i][j] == '.') continue;
                owp[i] += win[i][j]/double(played[i][j]);
                cc++;
                //cout<<j<<"'s w="<<win[i][j]<<", pl="<<played[i][j]<<"owp = "<<win[i][j]/double(played[i][j])<<endl;
            }
            owp[i]/=double(cc);
        }
        FOR(i, n) {
            oowp[i] = 0;
            int cc=0;
            FOR(j, n) {
                if(i == j) continue;
                if(mmap[i][j] == '.') continue;
                oowp[i] += owp[j];
                cc++;
            }
            oowp[i]/=double(cc);
        }
        printf("Case #%d:\n", cno);
        FOR(i, n) {
            printf("%.7lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
        }
    }
    return 0;
}
