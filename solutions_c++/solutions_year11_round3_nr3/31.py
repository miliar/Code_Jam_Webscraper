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
const LL INF=1ll<<62;
const int xam=10100;

int n;
LL L,H;
LL dane[xam];
LL NWD[xam],NWW[xam]; //(1,i) idzie do NWW

LL ans;

LL nwd(LL a, LL b)
{
    if(b==0) return a;
    return nwd(b,a%b);
}
LL nww(LL a, LL b)
{
    a/=nwd(a,b);
    if(INF/a<b) return INF;
    return a*b;
}
LL inf(LL a, LL b)
{
    if((INF/a)<b) return INF;
    return a*b;
}
void set_nww_nwd()
{
    NWW[0]=dane[0];
    for(int i=1; i<n; i++) NWW[i]=nww(NWW[i-1],dane[i]);
    NWD[n-1]=dane[n-1];
    for(int i=n-2; i>=0; i--) NWD[i]=nwd(NWD[i+1],dane[i]);
}

void play()
{
    scanf("%d%lld%lld", &n, &L,&H);
    FOR(i,n) scanf("%lld", &dane[i]);
    sort(dane,dane+n);
    LL *p=unique(dane,dane+n);
    n=p-dane;
    set_nww_nwd();
    /*
    FOR(i,n) printf("%lld ", dane[i]); printf("\n");
    FOR(i,n) printf("%lld ", NWD[i]); printf("\n");
    FOR(i,n) printf("%lld ", NWW[i]); printf("\n");
    */
    ans=INF;
   
    
    LL a,b,c,d;
    vector<LL> V;
    FOR(i,n-1) {
	if(NWD[i+1]%NWW[i]) continue;
	c=NWD[i+1]/NWW[i];
// 	printf("%lld %lld %lld\n", NWD[i+1],NWW[i],c);
	
	for(LL j=1; j<=sqrt(c); j++) {
	    if(c%j==0) {
		a=inf(NWW[i],j);
		
		if(a>=L && a<=H) {
		    ans=min(ans,a);
		    break;
		}
		a=inf(NWW[i],c/j);
		if(a>=L && a<=H) {
		    ans=min(ans,a);
		}
	    }
	}
    }
    
    a=(L+NWW[n-1]-1)/NWW[n-1];
    b=H/NWW[n-1];
    if(b-a>=0) ans=min(ans,NWW[n-1]*a);
    
    c=NWD[0];
    for(LL j=1; j<=sqrt(c); j++) {
	if(c%j==0) {
	    a=j;
	    if(a>=L && a<=H) {
		ans=min(ans,a);
		break;
	    }
	    a=c/j;
	    if(a>=L && a<=H) {
		ans=min(ans,a);
	    }
	}
    }
    
    if(ans==INF) printf("NO\n");
    else printf("%lld\n", ans);
}

int main()
{
    int t;
    scanf("%d", &t);
    REP(i,t) {
	printf("Case #%d: ", i);
	play();
    }
    

    return 0;
}
