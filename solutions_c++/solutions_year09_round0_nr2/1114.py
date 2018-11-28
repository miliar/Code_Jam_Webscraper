#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;
const int mn = 128 , inf = 1 << 30;
int R,C,grid[mn][mn] , comp[mn][mn] , ncomps;
char mapping[32];

typedef pair < int , int > PI;
typedef pair < int , PI > node;
int dr[] = {-1,0,0,1};
int dc[] = {0,-1,1,0};
void go ( int pr , int pc ) 
{
	if ( comp[pr][pc] != -1 ) 	
	{
		assert ( comp[pr][pc] == ncomps );
		return;
	}
	comp[pr][pc] = ncomps;
	for ( int t=0;t<4;t++ )
	{
		int nr = pr + dr[t] , nc = pc + dc[t];
		#define ok(y,X) ( ((y)>0) && ((y)<=(X)) )
		if ( ok(nr,R) && ok(nc,C) && comp[nr][nc] == -1 )
		{
			// check if [nr,nc] flows to [pr,pc]
			int minval = grid[nr][nc] , nextr=-1 , nextc=-1;
			for ( int i=0;i<4;i++ )
			{
				if ( ok(nr+dr[i],R) && ok(nc+dc[i],C) )
				{
					if ( minval > grid[nr+dr[i]][nc+dc[i]] )
						minval = grid[nr+dr[i]][nc+dc[i]] , nextr = nr+dr[i] , nextc = nc + dc[i];
				}
			}
			if ( nextr == pr && nextc == pc )
			{
//				cout << "From " << pr <<" "<< pc <<" possible " << nr <<" "<< nc << endl;
				go ( nr , nc );
			}
		}
	}
}

int main()
{
	int T;
	cin >> T;
	for ( int kase=1;kase<=T;kase++ )
	{
		ncomps = 0;
		vector < node > V;
		cin >> R >> C;
		for ( int i=1;i<=R;i++ )
		for ( int j=1;j<=C;j++ ) 
		{
			cin >> grid[i][j] ;
			comp[i][j] = -1;
			V.push_back ( node (grid[i][j] , PI ( i , j ) ) );
		}
		
		sort ( V.begin() , V.end() );
		
		for ( int i=0;i<V.size();i++ ) 
		{
			int pr = V[i].second.first , pc = V[i].second.second;
			if ( comp[pr][pc] == -1 )
			{
				ncomps ++;
				go(pr,pc);
			}
		}
		char nxt = 'a';
		for ( int i=0;i<32;i++ ) mapping[i] = 0;
		
		for ( int i=1;i<=R;i++ )
		for ( int j=1;j<=C;j++ ) if ( mapping[comp[i][j]] == 0 )
			mapping[comp[i][j]] = nxt ++;

			
		cout <<"Case #" << kase <<":" << endl;
		for ( int i=1;i<=R;i++ )
		for ( int j=1;j<=C;j++ ) 
		{
			assert ( comp[i][j] != -1 );
			cout << mapping[comp[i][j]];
			if ( j != C ) cout << " ";
			else cout << endl;
		}
	}
}
