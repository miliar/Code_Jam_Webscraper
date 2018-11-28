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
#include <sstream>
#include <numeric>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
typedef pair<int,int> PI;
#define dbg(x) cerr << #x << " -> " << (x) << "\t";
#define dbge(x) cerr << #x << " -> " << (x) << "\n";
const int mn=300;
int Grid[mn][mn], nGrid[mn][mn];

int main()
{
	int kase_;
	cin >> kase_;
	for ( int kase=1;kase<=kase_;kase++ )
	{
		dbge(kase);
		int cnt;
		cnt = 0;
		int k;
		cin >> k;
		memset ( Grid , 0 , sizeof ( Grid ) );
		memset ( nGrid , 0 , sizeof ( nGrid ) );
		for ( int i=0;i<k;i++ )
		{
			int x1,x2,y1,y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for ( int i=x1;i<=x2;i++ )
			for ( int j=y1;j<=y2;j++ )
			{
				Grid[j][i] = 1;
				cnt ++;
			}
		}
		
		int cur = 1;
		int result = 0;
		while ( cnt > 0 )
		{
			memcpy ( nGrid,  Grid , sizeof ( Grid ) );
			result ++;
			for ( int i=1;i<mn;i++ )
			for ( int j=1;j<mn;j++ ) if ( Grid[i][j] == 0 )
				if ( Grid[i-1][j] == 1 && Grid[i][j-1] == 1 )
					nGrid[i][j] = 3;

			for ( int i=1;i<mn;i++ )
			for ( int j=1;j<mn;j++ ) if ( Grid[i][j] == 1 )
				if ( Grid[i-1][j] != 1 && Grid[i][j-1] != 1 )
					nGrid[i][j] = 4;

			cnt = 0;
			for ( int i=0;i<mn;i++ )
			for ( int j=0;j<mn;j++ ) 
			{
				if ( nGrid[i][j] <= 1 ) Grid[i][j] = nGrid[i][j] , cnt += Grid[i][j];
				if ( nGrid[i][j] == 3 ) cnt ++ , Grid[i][j] = 1;
				if ( nGrid[i][j] == 4 ) Grid[i][j] = 0;
			}
		}
		
		
		cout <<"Case #" << kase <<": " << result << endl;
//		assert ( 0 );
	}
	return 0;
}
