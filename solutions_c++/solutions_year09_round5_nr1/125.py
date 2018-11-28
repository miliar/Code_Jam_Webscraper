#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <string>
#include <cstdio>
#include <cctype>
#include <vector>
#include <cassert>
#include <iomanip>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
typedef pair<int,int> PI;
#define dbg(x) cout << #x << " -> " << (x) << "\t";
#define dbge(x) cout << #x << " -> " << (x) << "\n";
const int mn = 16;
int R,C;
string grid[mn],ngrid[mn];
int dr[] = { -1 , 0 , 1 , 0 };
int dc[] = { 0 , -1 , 0 , 1 };
int seengoal,seentmp;
inline void place ( vector < string > & V , PI & pos )
{
	if ( V[pos.first][pos.second] == '.' )
		V[pos.first][pos.second] = 'o';
	else if ( V[pos.first][pos.second] == 'x' )
		V[pos.first][pos.second] = 'w' , seengoal ++;
}

int seen[16][16],seenid;

inline void go ( int r, int c , vector < string > & V )
{
	if ( r < 0 || c < 0 || r >= R || c >= C ) return ;

	if (( V[r][c] == 'o' || V[r][c] == 'w') && seen[r][c] != seenid )
	{
		seen[r][c] = seenid;	
		seentmp ++;
		for ( int i=0;i<4;i++ )
			go ( r + dr[i] , c + dc[i] , V );
	}

}

inline bool ok ( int r , int c , vector < string > & V )
{
	if ( r < 0 || r >= R || c < 0 || c >= C )
		return false;
	
	if ( V[r][c] == '.' || V[r][c] == 'x' )
		return true;
	
	return false;
}

int main()
{
	int kase_;
	cin >> kase_;
	for ( int kase=1;kase<=kase_;kase++ )
	{
		cin >> R >> C;
		for ( int i=0;i<R;i++ ) cin >> grid[i];
		
		vector < PI > init;
		
		for ( int i=0;i<R;i++ )
		for ( int j=0;j<C;j++ ) if ( grid[i][j] == 'o' || grid[i][j] == 'w' )
			init.push_back ( PI ( i , j ) );
			
		for ( int i=0;i<R;i++ ) ngrid[i] = grid[i];
		
		
		vector < string > ngrid ( R , string ( C , ' ' ) ) , tgrid , nxtgrid;
		
		for ( int i=0;i<R;i++ )
		for ( int j=0;j<C;j++ ) if ( grid[i][j] == 'o' )
			ngrid[i][j] = '.';
		else if ( grid[i][j] == 'w' )
			ngrid[i][j] = 'x';
		else
			ngrid[i][j] = grid[i][j];
			
		sort ( init.begin() , init.end() );
		queue < vector < PI > > Q;
		map < vector < PI > , int > M;
		Q.push ( init );
		M[init] = 0;
		int result = -1;
		while ( !Q.empty() )
		{
			vector < PI > pres = Q.front() , tmp = pres;
			Q.pop();
			int pdist = M[pres];
			tgrid = ngrid;
			seengoal = 0;
			for ( int i=0;i<pres.size();i++ )
				place ( tgrid , pres[i] );
			if ( seengoal == pres.size() )
			{
				result = M[pres];
				break;
			}

			seentmp = 0;
			seenid ++;
			go ( pres[0].first , pres[0].second , tgrid );
			
			bool danger = (seentmp != pres.size());

			for ( int i=0;i<pres.size();i++ )
			{
				for ( int t=0;t<4;t++ )
				{
					int myr = pres[i].first + dr[t] , myc = pres[i].second + dc[t];
					int mover = pres[i].first - dr[t] , movec = pres[i].second - dc[t];
					if ( ok(myr,myc,tgrid) && ok(mover,movec,tgrid) )
					{
						// move pres[i].first , pres[i].second to mover , movec;
						tmp = pres;
						tmp[i].first = mover , tmp[i].second = movec;
						sort ( tmp.begin() , tmp.end() );
						nxtgrid = ngrid;
						seengoal = 0;				
						for ( int j=0;j<tmp.size();j++ )
							place ( nxtgrid , tmp[j] );
						seentmp = 0;
						seenid ++;
						go ( tmp[0].first , tmp[0].second , nxtgrid );
						
						bool newdanger = (seentmp != tmp.size() );
						if ( danger && newdanger )
							continue;
						if ( M.count ( tmp ) )
						continue;
						else
						{
							M[tmp] = pdist + 1;
							Q.push ( tmp );
						}
					}
				}
			}
		}
		cout <<"Case #" << kase <<": " << result << endl;
	}
	return 0;
}
