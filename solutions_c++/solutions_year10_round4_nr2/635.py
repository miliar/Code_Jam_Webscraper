#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<cmath>
#include<string>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<vector>
#include<bitset>
#include<queue>
#include<stack>
#include<utility>
#include<list>
#include<set>
#include<map>
 
using namespace std;

#define eps 1e-9
#define INF INT_MAX
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).end(),(v).begin()
#define mp make_pair
#define pb push_back

#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v))
#define CLEAR(t) memset((t),0,sizeof(t))
#define MAX 10000
typedef pair < int, int > pii;
typedef long long LL;
int P;
int M[1<<11]; 
int games[MAX];
int valor;
void go(int ini, int fin, int i, int mostplay, int game ){
	if(mostplay == 1){
		games[game] = 1;
		return;
	}
	games[game] = 1;
	int mid = (ini + fin) / 2;
	if(i <= mid) 
		go( ini, mid, i, mostplay - 1, game * 2 + 1);
	else 
		go(mid + 1, fin, i, mostplay -1 , game * 2 + 2);
}

void run1(int caso){
	cin >> P;
	CLEAR(M);
	CLEAR(games);
	REP(i,(1 << P)) cin >> M[i];

	int fase = (1 << P)/2;
	while(fase >= 1){
		REP(i,fase) cin >> valor;
		fase/=2;
	}

	REP(i,(1<<P)){
		if(P - M[i] != 0)
			go( 0, (1 << P) - 1, i, P - M[i], 0);
	}		
	int sol = 0;
	REP(i,MAX) sol += games[i];

	cout << "Case #"<<caso<<": "<< sol<<endl;
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run1(i);
	return 0;
}