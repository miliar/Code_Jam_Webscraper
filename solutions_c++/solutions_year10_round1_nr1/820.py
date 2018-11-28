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

#define MAX 50
void run1(int caso){
	int N,K;
	cin >>N>>K;

	char A[MAX][MAX]={0};

	REP(i,N) REP(j,N){
		cin >> A[j][N-i-1];
	}

	for(int fil = N-2; fil>=0; fil--){
		REP(col,N){
			if(A[fil][col]!='.'){
				int i = fil;
				while(i< N && A[i+1][col]=='.'){
					A[i+1][col]=A[i][col];
					A[i][col]='.';
					i++;
				}
			}
		}
	}
	bool b=false,r=false;
	int dir[8][2]={{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};

	REP(i,N) REP(j,N){
		if(A[i][j]=='.') continue;
		REP(d,8){
			int cont = 1, id=d;
			int fil = i, col = j;
			while(cont<K && fil+dir[id][0]>=0 && fil+dir[id][0]<N&& col+dir[id][1]>=0 && col+dir[id][1]<N && 
				A[fil+dir[id][0]][col+dir[id][1]]==A[i][j]){ 
					cont++;
					fil = fil+dir[id][0];
					col = col+dir[id][1];
			}

			if(cont==K){
				if(A[i][j]=='R') r = true;
				if(A[i][j]=='B') b = true;
			}
		}
	}
	cout << "Case #"<<caso<<": ";
	if(!b && !r) cout << "Neither";
	else if(!b && r) cout << "Red";
	else if(b && !r) cout << "Blue";
	else if(b && r) cout << "Both";

	cout << endl;
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run1(i);
	return 0;
}