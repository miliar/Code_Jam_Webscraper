#include <cstdio>
#include <cstring>

#include <algorithm>
#include <map>
#include <queue>

using namespace std;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int R, C, numBoxes;
int board[12][12];

int am[12][12];

struct state {
	int boxes[5];
	bool is_danger;
	
	state() { memset(boxes, -1, sizeof(boxes)); is_danger = false; }
	
	void canonicalize() {
		for( int i = 0; i < numBoxes; ++i )
			for( int j = i+1; j < numBoxes; ++j )
				if( boxes[i] > boxes[j] ) swap(boxes[i], boxes[j]);
		
		bool used[5]; memset(used, false, sizeof(used));
		queue<int> Q;
		
		used[0] = true;
		Q.push(0);
		
		while( !Q.empty() ) {
			int x = Q.front();
			Q.pop();
			
			for( int y = 0; y < 5; ++y ) {
				if( used[y] ) continue;
				
				if( abs(boxes[x]/C-boxes[y]/C) + abs(boxes[x]%C-boxes[y]%C) == 1 ) {
					used[y] = true;
					Q.push(y);
				}
			}
		}
		
		is_danger = false;		
		for( int i = 0; i < numBoxes; ++i )
			if( !used[i] ) { is_danger = true; break; }
	}
	
	void dump() {
		for( int i = 0; i < numBoxes; ++i )
			printf( "%d %d\n", boxes[i]/C, boxes[i]%C );
		printf( "%d\n", is_danger );
	}
	
	bool operator< ( const state& b ) const {
		for( int i = 0; i < numBoxes; ++i )
			if( boxes[i] != b.boxes[i] ) return boxes[i] < b.boxes[i];
		return false;
	}
} initial, final;
int initialp, finalp;

map<state, int> dist;
state Q[10000000];
int front, back;

void addnode( state next, int d )
{
	if( dist.find(next) == dist.end() ) {
		Q[back++] = next;
		dist[next] = d;
	}
}

int main( void )
{
	freopen( "A.in", "r", stdin );
	freopen( "A-small.out", "w", stdout );
	
	int T; scanf( "%d", &T );
	
	for( int counter = 0; counter < T; ++counter ) {
		scanf( "%d %d", &R, &C );
		numBoxes = initialp = finalp = 0;
		
		for( int i = 0; i < R; ++i )
			for( int j = 0; j < C; ++j ) {
				char ch; scanf( " %c", &ch );
				
				if( ch == '.' ) {
					board[i][j] = 0;
				} else if( ch == '#' ) {
					board[i][j] = -1;
				} else if( ch == 'x' ) {
					board[i][j] = 0;
					final.boxes[finalp++] = i*C + j;
				} else if( ch == 'o' ) {
					board[i][j] = 0;
					initial.boxes[initialp++] = i*C + j;
				} else {
					board[i][j] = 0;
					initial.boxes[initialp++] = i*C + j;
					final.boxes[finalp++] = i*C + j;
				}
			}
		numBoxes = finalp;
		
		initial.canonicalize();
		final.canonicalize();	
		
		dist.clear();
		front = back = 0;
		addnode(initial, 0);
		
		int at = -1;
		memset(am, -1, sizeof(am));	

		while( front < back && dist.find(final) == dist.end() ) {
			state curr = Q[front++];
			int d = dist[curr];
			
			++at;
			for( int i = 0; i < numBoxes; ++i )	am[curr.boxes[i]/C][curr.boxes[i]%C] = at;
			
			for( int i = 0; i < numBoxes; ++i ) {
				int x = curr.boxes[i]/C;
				int y = curr.boxes[i]%C;
				
				for( int j = 0; j < 4; ++j ) {
					if( x+dx[j] < 0 || y+dy[j] < 0 || x+dx[j] >= R || y+dy[j] >= C ) continue;
					if( am[x+dx[j]][y+dy[j]] == at || board[x+dx[j]][y+dy[j]] < 0 ) continue;
					if( x-dx[j] < 0 || y-dy[j] < 0 || x-dx[j] >= R || y-dy[j] >= C ) continue;
					if( am[x-dx[j]][y-dy[j]] == at || board[x-dx[j]][y-dy[j]] < 0 ) continue;
					
					state next = curr;
					next.boxes[i] = (x+dx[j])*C + (y+dy[j]);
					next.canonicalize();
					
					if( curr.is_danger && next.is_danger ) continue;
					addnode(next, d + 1);
				}
			}
		}
		
		int ret = dist.find(final) == dist.end() ? -1 : dist[final];
		printf( "Case #%d: %d\n", counter+1, ret );
	}
	
	return 0;	
}
