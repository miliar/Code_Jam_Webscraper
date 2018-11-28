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

#define NN 1000
void runCase()
{
    int X,S,R,t,N;
    scanf("%d%d%d%d%d",&X,&S,&R,&t,&N);
    int B[NN],E[NN],w[NN];
    REP(i,N) scanf("%d %d %d",&B[i],&E[i],&w[i]);

    double res = 0.0;
    vi ww(N);
    int sum = 0;
    REP(i,N) {
        ww[i] = E[i] - B[i];
        sum += ww[i];
    }

    sum = X-sum;
    if(sum >= R*t) {
        res = t+1.0*(sum-R*t)/S;
        REP(i,N) res+=(1.0*ww[i]/(S+w[i]));
    }
    else {
        res = 1.0*sum/R;
        double lt = t - 1.0*sum/R;

        vi noused(N,1);
        REP(i,N) {
            int mi = 0;
            REP(j,N) if(noused[j]) {mi = j;break;}
            REP(j,N) if(noused[j] && w[j]<w[mi]) mi = j;
            noused[mi] = 0;

            double rt = 1.0*ww[mi]/(R+w[mi]);
            if(lt > rt) {
                lt-=rt;
                res += rt;
            }
            else if(lt>0.0) {
                res += lt;
                res += (ww[mi]-lt*(R+w[mi]))/(S+w[mi]);
                lt = -1.0;
            }
            else {
                res += (1.0*ww[mi]/(S+w[mi]));
            }
        }
    }

    printf("%lf\n",res);
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
