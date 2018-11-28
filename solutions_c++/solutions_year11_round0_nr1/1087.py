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
    char ch;
    int n,a;
    scanf("%d", &n);
    int time[2]={0,0},pos[2]={1,1},last=-1;
    while(n--) {
	scanf(" %c%d", &ch, &a);
	if(ch=='O') ch=0;
	else if(ch=='B') ch=1;
	time[ch]=max(time[ch^1]+1,time[ch]+abs(pos[ch]-a)+1);
	pos[ch]=a;
	
    }
    printf("%d\n", max(time[0],time[1]));
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
