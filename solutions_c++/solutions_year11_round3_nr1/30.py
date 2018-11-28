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
const int xam=100;

int n,m;
char tab[xam][xam];

bool change(int a, int b)
{
    if(a+1==n) return 0;
    if(b+1==m) return 0;
    FOR(i,2) FOR(j,2) if(tab[a+i][b+j]=='.') return 0;
    tab[a][b]='/';
    tab[a][b+1]='\\';
    tab[a+1][b]='\\';
    tab[a+1][b+1]='/';
    return 1;
}
bool play()
{
    scanf("%d%d", &n,&m);
    FOR(i,n) {
	FOR(j,m) scanf(" %c", &tab[i][j]);
    }
    FOR(i,n) FOR(j,m) {
	if(tab[i][j]=='#') if(!change(i,j)) return 0;
    }
    FOR(i,n) {
	FOR(j,m) printf("%c", tab[i][j]);
	printf("\n");
    }
    return 1;
}

int main()
{
    int t;
    scanf("%d", &t);
    REP(i,t) {
	printf("Case #%d:\n", i);
	if(!play()) printf("Impossible\n");
    }
    

    return 0;
}
