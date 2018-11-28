#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <stack>
#include <queue>
#include <cmath>

using namespace std;

// Input
#define s(n)					scanf("%d",&n)
#define sc(n)                   scanf("%c",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)

// Constants
#define INF						(int)1e9
#define LINF					(long long)1e18
#define EPS						1e-9

// Functions
#define maX(a,b)                ( (a) > (b) ? (a) : (b))
#define miN(a,b)                ( (a) < (b) ? (a) : (b))
#define abS(x)					( (x) < 0 ? -(x) : (x))
#define checkbit(n,b)           ( (n >> b) & 1)
#define DREP(a)                 sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)          (lower_bound(all(arr),ind)-arr.begin())

// Traversal
#define FOR(i,a,b)				for(int i=a;i<b;i++)
#define REP(i,n)				FOR(i,0,n)
#define foreach(v,c)			for(typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)

// Container
#define fill(a,v) 				memset(a,v,sizeof a)
#define all(x)					x.begin(),x.end()
#define SZ(v)					((int)(v.size()))
#define mp						make_pair
#define FF						first
#define SS						second
#define tri(a,b,c)				mp(a,mp(b,c))
#define XX						first
#define YY						second.first
#define ZZ						second.second
#define pb						push_back

// Debugger
#define debug(args...)			{dbg,args; cerr<<endl;}
#define dline					cerr<<endl

struct debugger{
	template<typename T> debugger& operator , (const T& v){	
		cerr<<v<<" ";
		return *this;
	}
} dbg;

// Typedef
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef pair<int,PII> TRI;

typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<PII> VII;
typedef vector<PLL> VLL;

int main(){
	int tc, pcount, tcount;
	char board[4][4], t[4][4], c;
	bool incomplete, win;

	s(tc);

	REP(case_no,tc){
		
		incomplete = false;

		scanf("%c", &c);
		REP(i,4){
			REP(j,4){
				scanf("%c", &board[i][j]);
				if(board[i][j] == '.')
					incomplete = true;
			}
			scanf("%c", &c);
		}

		// Set t to board
		REP(i,4) REP(j,4) t[i][j] = board[i][j];

		// BEGIN CHECK X
		// Check
		// Horizontal
		win = false;
		REP(i,4){
			pcount = tcount = 0;
			REP(j,4){
				if(board[i][j] == 'X') pcount++;
				if(board[i][j] == 'T') tcount++;
			}
			if(pcount == 4 || (pcount == 3 && tcount == 1)){
				win = true;
			}
		}
		if(win){
			printf("Case #%d: X won\n", case_no+1); continue;
		}

		// Vertical
		win = false;
		REP(i,4){
			pcount = tcount = 0;
			REP(j,4){
				if(board[j][i] == 'X') pcount++;
				if(board[j][i] == 'T') tcount++;
			}
			if(pcount == 4 || (pcount == 3 && tcount == 1)){
				win = true;
			}
		}
		if(win){
			printf("Case #%d: X won\n", case_no+1); continue;
		}

		// Diagonals
		pcount = tcount = 0;
		REP(i,4){
			if(board[i][i] == 'X') pcount++;
			if(board[i][i] == 'T') tcount++;
		}
		if(pcount == 4 || (pcount == 3 && tcount == 1)){
			printf("Case #%d: X won\n", case_no+1); continue;
		}

		pcount = tcount = 0;
		REP(i,4){
			if(board[3-i][i] == 'X') pcount++;
			if(board[3-i][i] == 'T') tcount++;
		}
		if(pcount == 4 || (pcount == 3 && tcount == 1)){
			printf("Case #%d: X won\n", case_no+1); continue;
		}

		// BEGIN CHECK Y
		// Check
		// Horizontal
		win = false;
		REP(i,4){
			pcount = tcount = 0;
			REP(j,4){
				if(board[i][j] == 'O') pcount++;
				if(board[i][j] == 'T') tcount++;
			}
			if(pcount == 4 || (pcount == 3 && tcount == 1)){
				win = true;
			}
		}
		if(win){
			printf("Case #%d: O won\n", case_no+1); continue;
		}

		// Vertical
		win = false;
		REP(i,4){
			pcount = tcount = 0;
			REP(j,4){
				if(board[j][i] == 'O') pcount++;
				if(board[j][i] == 'T') tcount++;
			}
			if(pcount == 4 || (pcount == 3 && tcount == 1)){
				win = true;
			}
		}
		if(win){
			printf("Case #%d: O won\n", case_no+1); continue;
		}

		// Diagonals
		pcount = tcount = 0;
		REP(i,4){
			if(board[i][i] == 'O') pcount++;
			if(board[i][i] == 'T') tcount++;
		}
		if(pcount == 4 || (pcount == 3 && tcount == 1)){
			printf("Case #%d: O won\n", case_no+1); continue;
		}

		pcount = tcount = 0;
		REP(i,4){
			if(board[3-i][i] == 'O') pcount++;
			if(board[3-i][i] == 'T') tcount++;
		}
		if(pcount == 4 || (pcount == 3 && tcount == 1)){
			printf("Case #%d: O won\n", case_no+1); continue;
		}

		// NO WIN STATES
		// Checking for incomplete game
		if(incomplete){
			printf("Case #%d: Game has not completed\n", case_no+1); continue;
		} else{
			printf("Case #%d: Draw\n", case_no+1); continue;
		}

	}
	return 0;
}
