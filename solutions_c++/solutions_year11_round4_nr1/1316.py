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

pair<LD,LD> dane[xam]; //S //V
int sum;
int X,t,n;
LD T,R,S;

LD ans;

bool cmp(pair<LD,LD> a, pair<LD,LD> b) {
    return a.sec<b.sec;
}

void resolve(pair<LD,LD> a)
{
    if(T>=(a.frs/LD(a.sec+R))) {
	T-=a.frs/LD(a.sec+R);
	ans+=a.frs/LD(a.sec+R);
    }
    else {
	a.frs-=LD(a.sec+R)*T;
	ans+=T;
	T=0;
	ans+=a.frs/LD(a.sec+S);
    }
}
void play()
{
    sum=0; ans=0;
    int b,e,v;
    scanf("%d%llf%llf%d%d", &X,&S,&R,&t,&n);
    T=t;
    FOR(i,n) {
	scanf("%d%d%llf", &b,&e,&dane[i].sec);
	dane[i].frs=e-b;
	sum+=dane[i].frs;
    }
    
    dane[n]=mkp(X-sum,0);
    sort(dane,dane+n+1,cmp);
//     FOR(i,n+1) printf("%llf %llf\n", dane[i].frs,dane[i].sec);
    
    FOR(i,n+1) resolve(dane[i]);
    printf("%.9llf\n", ans);
}

int main()
{
    int tt;
    scanf("%d", &tt);
    REP(i,tt) {
	printf("Case #%d: ", i);
	play();
    }

    return 0;
}
