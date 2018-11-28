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

void play()
{
    int n,sum=0,mini=INF,x=0,a;
    scanf("%d", &n);
    while(n--) {
	scanf("%d", &a);
	sum+=a;
	mini=min(mini,a);
	x^=a;
    }
    if(x) printf("NO\n");
    else printf("%d\n", sum-mini);
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
