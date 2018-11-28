#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>

#define FOR(i,n) for(int i=0; i<(n); i++)
#define REP(i,n) for(int i=1; i<=(n); i++)
#define FORI(it,n) for(typeof((n).begin()) it=(n).begin(); it!=(n).end(); it++)
#define ALL(n) (n).begin(), (n).end()
#define psh push_back
#define mkp make_pair
#define frs first
#define sec second
using namespace std;
typedef pair<int,int> PII;
typedef long long LL;
typedef long double LD;
const int INF=1<<29;
const int xam=100100;

int n,L;
int temp[xam];
double dane[xam]; //dane[i] - odleglosc i-1 -> i
double t;

double dyn[3][xam];

LL play()
{
    int C;
    scanf("%d%lf%d%d", &L, &t,&n,&C);
    FOR(i,C) scanf("%d", &temp[i]);
    REP(i,n) dane[i]=temp[(i-1)%C];
//     REP(i,n) printf("%.0lf ", dane[i]); printf("\n");
    
    FOR(i,L+1) REP(j,n) dyn[i][j]=INF;
    
    FOR(i,n) {
	FOR(j,L) {
	    dyn[j][i+1]=min(dyn[j][i+1],dyn[j][i]+dane[i+1]*2);
	    if(dyn[j][i]>=t) dyn[j+1][i+1]=min(dyn[j+1][i+1],dyn[j][i]+dane[i+1]);
	    else dyn[j+1][i+1]=min(dyn[j+1][i+1],dyn[j][i]+min((t-dyn[j][i]),dane[i+1]*2)+dane[i+1]-double(min((t-dyn[j][i]),dane[i+1]*2))/2);
	}
	dyn[L][i+1]=min(dyn[L][i+1],dyn[L][i]+dane[i+1]*2);
    }
    
    double mini=INF;
    FOR(i,L+1) mini=min(mini,dyn[i][n]);
    
    return mini;
}

int main()
{
    int t;
    scanf("%d", &t);
    REP(i,t) {
	printf("Case #%d: ", i);
	printf("%lld\n", play());
    }
    

    return 0;
}
