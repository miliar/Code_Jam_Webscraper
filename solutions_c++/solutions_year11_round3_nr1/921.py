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

typedef pair < int, int > pii;
typedef long long LL;

#define MAX 51
int R,C;

void run1(int caso){
	cin >>R>>C;
	char map[MAX][MAX];
	REP(i,R)REP(j,C){
		cin >> map[i][j];
	}
	bool possible = true;
	REP(i,R){
		REP(j,C){
			if(map[i][j]=='#' ){
				if(i+1<R && j+1<C && map[i][j]=='#' && map[i+1][j]=='#' && map[i][j+1]=='#' && map[i+1][j+1]=='#'){
					map[i][j]='/';
					map[i][j+1]='\\';
					map[i+1][j]='\\';
					map[i+1][j+1]='/';
				}else{
					possible = false;
					break;
				}
			}
			if(!possible) break;
		}
	}
	cout << "Case #"<<caso<<": "<<endl;

	if(possible){
		REP(i,R){REP(j,C){
				cout << map[i][j];
			}
		cout << endl;
		}
	}
	else cout << "Impossible"<<endl;
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run1(i);
	return 0;
}
