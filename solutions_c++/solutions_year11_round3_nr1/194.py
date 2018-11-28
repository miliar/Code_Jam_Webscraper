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
#define vi vector< int >
#define vvi vector< vi >
#define PB push_back
#define SZ(x) ((int)x.size())

void runCase()
{
    int R,C;
    scanf("%d%d",&R,&C);
    char pic[51][51];
    setbuf(pic,0);

    REP(i,R) {
        scanf("%s",pic[i]);
    }

    bool can = true;

    REP(i,R) {
        int cnt = 0;
        REP(j,C){
            if(pic[i][j] == '#') {
                cnt++;
            }
            else {
                if(j>0 && pic[i][j-1] == '#') {
                    if(cnt%2) {
                        can = false;
                    }
                    cnt = 0;
                }
            }
        }
        if(cnt%2) {
            can = false;
        }
    }

    REP(j,C) {
        int cnt = 0;
        REP(i,R) {
            if(pic[i][j] == '#') {
                cnt++;
            }
            else {
                if(i>0 && pic[i-1][j] == '#') {
                    if(cnt%2) {
                        can = false;
                    }
                    cnt = 0;
                }
            }
        }
        if(cnt%2) {
            can = false;
        }
    }

    cout << endl;
    if(can) {
        REP(i,R) {
            REP(j,C) {
                if(pic[i][j] == '#') {
                    pic[i][j] = '/';
                    pic[i+1][j] = '\\';
                    pic[i][j+1] = '\\';
                    pic[i+1][j+1] = '/';
                }
            }
        }
        REP(i,R) cout << pic[i] << endl;
    }
    else {
        cout << "Impossible" << endl;
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
