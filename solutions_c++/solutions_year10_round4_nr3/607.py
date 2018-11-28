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
int R,n;
#define MAX 300
int m[MAX][MAX];

int sim(){
	int t = 0;
	while(n>0){
		t++;
		n=0;
		int other[MAX][MAX]={0};
		REP(fil,MAX) REP(col,MAX){
			if(fil>0 && m[fil-1][col] && m[fil][col]){
				other[fil][col]=1;
				n++;
			}
			else if(col>0 && m[fil][col-1] && m[fil][col]){
				other[fil][col]=1;
				n++;
			} else if (fil>0 && col>0 && m[fil][col-1] && m[fil-1][col] && !m[fil][col]){
				n++;
				other[fil][col]=1;
			}
		}
		REP(fil,MAX) REP(col,MAX) m[fil][col] = other[fil][col];
	}
	return t;
}

void run1(int caso){
	cin >> R;
	CLEAR(m);
	REP(i,R){
		int x1,y1,x2,y2;
		cin >>x1>>y1>>x2>>y2;
		FORE(x,x1-1,x2-1){
			FORE(y,y1-1,y2-1){
				if(!m[x][y]) n++;
				m[x][y]=1;
			}	
		}
	}
	int sol=sim();
	cout << "Case #"<<caso<<": "<< sol<<endl;
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run1(i);
	return 0;
}