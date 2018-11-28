#include<cstdio>
#include<algorithm>
#include<vector>

#define FOR(i,n) for(int i=0; i<n; i++)
#define REP(i,n) for(int i=1; i<=n; i++)
#define FORI(it,n) for(typeof(n.begin()) it=n.begin(); it!=n.end(); it++)
#define ALL(n) n.begin, n.end()
#define frs first
#define sec second
#define mkp make_pair
#define psh push_back
using namespace std;
typedef pair<int,int> PII;
typedef long long LL;
const int INF=1<<30;
const int MAX=10100;

void play(int t)
{
	printf("Case #%d: ", t);
	int n,k;
	scanf("%d%d", &n,&k);
	if((k&((1<<n)-1))==(1<<n)-1) printf("ON\n");
	else printf("OFF\n");
}

int main()
{
	int t;
	scanf("%d", &t);
	REP(i,t) {
		play(i);
	}
		
	return 0;
}
