#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <list>

using namespace std;

void solve();
void runCase();

typedef long long LL;
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define REP(i,n) for(int i = 0; i < (n); i++)

#define debug( x ) cerr << "" << x << " "
#define dbg( c ) cerr << " " << c << " ";

#define setbuf(buf,num) memset(buf,num,sizeof(buf))

void runCase()
{
    int n;
    scanf("%d",&n);

    char tb[101][101];
    double fb[101][101];
    double wp[101], owp[101], oowp[101], rpi[101];
    memset(tb,0,sizeof(tb));
    setbuf(fb,0);
    setbuf(wp,0);
    setbuf(owp,0);
    setbuf(oowp,0);
    setbuf(rpi,0);

    REP(i,n){
        scanf("%s",tb[i]);
    }

    REP(team,n) {
        double a = 0.0,b = 0.0;
        REP(i,n) {
            if(tb[team][i] == '1') {
                a += 1.0;
            }
            if(tb[team][i] != '.') {
                b += 1.0;
            }
        }
        REP(i,n) {
            if(tb[team][i] == '1') {
                fb[team][i] = (a-1.0)/(b-1.0);
            }
            if(tb[team][i] == '0') {
                fb[team][i] = (a)/(b-1.0);
            }
        }
        wp[team] = a/b;
    }

    REP(team,n) {
        double a = 0.0,b = 0.0;
        REP(i,n) {
            if(tb[team][i] != '.') {
                a += fb[i][team];
                b += 1.0;
            }
        }
        owp[team] = a/b;
    }

    REP(team,n) {
        double a = 0.0,b = 0.0;
        REP(i,n) {
            if(tb[team][i] != '.') {
                a += owp[i];
                b += 1.0;
            }
        }
        oowp[team] = a/b;
    }

    REP(team,n) {
        rpi[team] = 0.25*wp[team] + 0.5*owp[team] + 0.25*oowp[team];
    }

//    REP(i,n) debug(wp[i]); dbg('\n');
//    REP(i,n) debug(owp[i]); dbg('\n');
//    REP(i,n) debug(oowp[i]); dbg('\n');

    cout << endl;
    REP(i,n) {
        cout << rpi[i] << endl;
    }
}

void solve()
{
	int n;
	scanf("%d",&n);
	getchar();

	for(int i = 0; i < n; i++) {
		printf("Case #%d: ",i+1);
		runCase();
	}
}

int main()
{
	solve();
	return 0;
}
