#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>


#define debug(x) cout << '>' << #x << ':' << x << '\n';
#define rep(X,Y,Z) for (int X = Y;X < Z;X++)
#define forn(X,Y) for (int X = 0;X < Y;X++)
#define sz(Z) Z.size()
#define all(W) W.begin(), W.end()
#define inf 2123123123LL
#define eps 0.0000001
#define vint vector<int>
#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)
#define mp make_pair
#define I(M) (typeof((M).begin()))
#define pb push_back

#define pipii pair< int, pair<int, pair<int, pair<int,int> > > >

typedef long long ll;
typedef long double ld;

using namespace std;

priority_queue< pipii, vector<pipii>, greater<pipii> > pq;

int dp[70][70][70][70];
int batu[70][70]; //position x,y, brp ke kiri kosong, brp ke kanan kosong
int r,c,f;

void insert(int abc,int def,int ghi,int jkl,int mno) {
	if (def >= r + 1) return;
	if (dp[abc][def][ghi][jkl] <= mno) return;
	dp[abc][def][ghi][jkl] = mno;
	pq.push( mp(mno, mp(abc, mp(def, mp(ghi,jkl)))));
	return;
	}
	

int main() {
	
	int zz;
	scanf("%d",&zz);
	
	forn(z,zz) {
		printf("Case #%d: ",z + 1);
		
		scanf("%d%d%d\n",&r,&c,&f);
		memset(batu,1,sizeof(batu));
		forn(j,r) {
			forn(k,c) {
				char dumi;
				scanf("%c",&dumi);
				if (dumi == '.') batu[k + 1][j + 1] = 0;
				}
			scanf("\n");
			}
		
		forn(i,70) forn(j,70) forn(k,70) forn(l,70) dp[i][j][k][l] = inf;
		
		insert(1,1,0,0,0);
		
		while (!pq.empty()) {
			int a = pq.top().first, b = pq.top().second.first, c = pq.top().second.second.first, 
			d = pq.top().second.second.second.first, e = pq.top().second.second.second.second;
			pq.pop();
			if (dp[b][c][d][e] < a) continue;
			//move
			if (!batu[b - 1][c] || d >= 1) {
				int fall = 0;
				while (!batu[b - 1][c + fall + 1]) fall++;
				if (fall == 0)
				insert(b - 1,c,max(0,d - 1),e + 1,a);
				}
			if (!batu[b + 1][c] || e >= 1) {
				int fall = 0;
				while (!batu[b + 1][c + fall + 1]) fall++;
				if (fall == 0)
				insert(b + 1,c,d + 1,max(0,e - 1),a);
				}
			
			//dig the left, then move right
			int numdig = 0;
			
			int ob = b,oc = c,od = d,oe = e;
			
			while (1) {
				if (batu[b - 1][c] && d <= 0) break;
				
				//try to dig to your left
				if (batu[b - 1][c + 1]) numdig++;
				
				//fall then
				if (numdig != 0 || !batu[b - 1][c + 1]) {
					
					int fall = 1;
					while (!batu[b - 1][c + fall + 1]) fall++;
					
					if (fall == 1) insert(b - 1,c + 1,max(0,numdig - 1),0,a + numdig);
					if (fall > 1 && fall <= f) insert(b - 1,c + fall,0,0,a + numdig);
					}
				
				//try to move to the right now
				if (!batu[b + 1][c + 1] || (batu[b + 1][c] && e == 0)) break; //can't move right
				//OK, now we can move right
				b += 1;
				d += 1;
				e = max(0,e - 1);
				}

				
			//now dig right, move left
			numdig = 0;
			
			b = ob;c = oc;d = od;e = oe;
			
			while (1) {
				if (batu[b + 1][c] && e <= 0) break;
				
				//try to dig to your right
				if (batu[b + 1][c + 1]) numdig++;
				
				//fall then
				if (numdig != 0 || !batu[b + 1][c + 1]) {
					
					int fall = 1;
					while (!batu[b + 1][c + fall + 1]) fall++;
					
					if (fall == 1) insert(b + 1,c + 1,0,max(0,numdig - 1),a + numdig);
					if (fall > 1 && fall <= f) insert(b + 1,c + fall,0,0,a + numdig);
					}
				
				//try to move to the LEFT now
				if (!batu[b - 1][c + 1] || (batu[b - 1][c] && d == 0)) break; //can't move LEFT
				//OK, now we can move right
				b -= 1;
				e += 1;
				d = max(0,d - 1);
				}
			}
		
		int best = inf;
		
		forn(i,70) forn(j,70) forn(k,70) best = min(best,dp[k][r][i][j]);
		
		if (best == inf) printf("No\n"); else printf("Yes %d\n",best);
		}

	
	return 0;
	}

