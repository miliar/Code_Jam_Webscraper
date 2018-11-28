#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;

#define pii pair<int,int>
#define mp make_pair

int dx[] = { -1 , 0 , 1 , 0 };
int dy[] = { 0 , 1 , 0 , -1 };
int rv[] = { 2 , 3 , 0 , 1 };

struct Cmp {
	bool operator () ( pii a , pii b ) {
		return a.second > b.second;
	}
};

const int MAXN = 1 << 4;

int n , m;
char a[MAXN][MAXN];
pii b[MAXN][MAXN][4];

int used[MAXN * MAXN * MAXN * MAXN * 4 * 4];
priority_queue < pii , vector < pii > , Cmp > q;

void read() {
	int i;
	
	scanf ("%d%d",&n,&m);
	for (i=0;i<n;i++)
		scanf ("%s",a[i]);
}

int ok ( int x , int y ) {
	return x >= 0 && y >= 0 && x < n && y < m;
}

int code ( int x , int y , int x2 , int y2 , int side ) {
	++ x2; ++ y2;
	return x | (y << 4) | (x2 << 8) | (y2 << 13) | (side << 18);
}

int decode ( int &x , int &y , int &x2 , int &y2 , int &side , int c ) {
	x = c & 15; c >>= 4;
	y = c & 15; c >>= 4;
	x2 = c & 31; c >>= 5;
	y2 = c & 31; c >>= 5;
	side = c;
	-- x2; -- y2;
}

void psh ( int x , int y ) {
	if ( !used[x] || used[x] > y ) {
		q.push ( mp ( x , y ) );
		used[x] = y;
	}
}

void solve() {
	memset ( used , 0 , sizeof used );
	while ( !q.empty() ) q.pop();
	int i , j , k;
	int x , y;
	int x1 , y1 , x2 , y2 , side;
	int qq , w;

	for (i=0;i<n;i++)
		for (j=0;j<m;j++)
			if ( a[i][j] != '#' )
				for (k=0;k<4;k++) {
					x = i;			y = j;
					while ( 1 ) {
						if ( !ok ( x , y ) || a[x][y] == '#' )
							break;
						x += dx[k];
						y += dy[k];
					}		
					
					b[i][j][k] = mp ( x , y );
				}
				
	for (i=0;i<n;i++)
		for (j=0;j<m;j++)
			if ( a[i][j] == 'O' ) {
				x = code ( i , j , i , j , 0 );
				psh ( x , 1 );
			}

	while ( !q.empty() ) {
		pii t = q.top(); q.pop();
		x = t.first;
		decode ( x1 , y1 , x2 , y2 , side , x );
		
		if ( used[x] < t.second ) continue;
		
		if ( a[x1][y1] == 'X' ) {
			printf ("%d\n",used[x] - 1 );
			return ;
		}
		
		for (i=0;i<4;i++) {
			qq = x1 + dx[i];
			w = y1 + dy[i];
			
			if ( ok ( qq , w ) && a[qq][w] != '#' ) {
				if ( x1 == x2 && y1 == y2 ) 
					y = code ( qq , w , qq , w , side );
				else
					y = code ( qq , w , x2 , y2 , side );
				psh ( y , used[x] + 1 );
			} else {
				if ( x1 == x2 && y1 == y2 ) continue;
				
				y = code ( x2 + dx[ side ] , y2 + dy[ side ] , qq , w , rv[i] ); 
				psh ( y , used[x] + 1 );
			}
		}
		
		for (i=0;i<4;i++) {
			y = code ( x1 , y1 , b[x1][y1][i].first , b[x1][y1][i].second , rv[i] );
			
			psh ( y , used[x] );
		}
	}
	
	printf ("THE CAKE IS A LIE\n");
}

int main() {
	int i , k;
	
	scanf ("%d",&k);
	
	for (i=1;i<=k;i++) {
		read();
		printf ("Case #%d: ",i);
		solve();	
	}
	
	return 0;
}
