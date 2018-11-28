#include <iostream>
#include <algorithm>
using namespace std ;

double wox[600][600], woy[600][600], wx[600][600], wy[600][600], wt[600][600], wto[600][600];
char w ;
int t, r, c, i, j, k, d ;

const double eps = 1e-9 ;

double calc( double w[600][600], double wo[600][600], int x1, int x2, int y1, int y2 ) 
{
	return w[x2][y2] - w[x1-1][y2] - w[x2][y1-1] + w[x1-1][y1-1] 
		   -wo[x1][y1] - wo[x2][y2] - wo[x1][y2] - wo[x2][y1] ; 
}

int main()
{
	freopen("B-small-attempt1(1).in","r",stdin);
	freopen("B.out","w",stdout) ;
	cin >> t ;
	for ( int tests = 1 ; tests <= t ; ++tests )
	{
		cin >> r >> c >> d ;
		for ( i = 1 ; i <= r ; ++i ) 
			for ( j = 1 ; j <= c ; ++j ) 
			{
				cin >> w ;
				wox[i][j] = (d+w-48) * (i-0.5);
				woy[i][j] = (d+w-48) * (j-0.5);
				wto[i][j] = d+w-48 ;
				wx[i][j] = wx[i-1][j] + wx[i][j-1] - wx[i-1][j-1] + wto[i][j] * (i-0.5) ;
				wy[i][j] = wy[i-1][j] + wy[i][j-1] - wy[i-1][j-1] + wto[i][j] * (j-0.5) ; 
				wt[i][j] = wt[i-1][j] + wt[i][j-1] - wt[i-1][j-1] + wto[i][j] ;
			}
		int res = -1 ;
		for ( i = 1 ; i <= r ; ++i ) 
			for ( j = 1 ; j <= c ; ++j ) 
				for ( k = 3 ; ; ++k ) if ( k > res ) 
				{
					int x1 = i, x2 = i+k-1, y1 = j, y2 = j+k-1 ;
					if ( x1<=0 || x2>r || y1<=0 || y2>c ) break ;
					double cx = i + double(k)/2 - 1 ;
					double cy = j + double(k)/2 - 1 ; 
					if ( fabs( calc(wx, wox, x1, x2, y1, y2) / calc(wt,wto,x1,x2,y1,y2) - cx ) < eps 
					  && fabs( calc(wy, woy, x1, x2, y1, y2) / calc(wt,wto,x1,x2,y1,y2) - cy ) < eps )
						res = k ;
				}
		cout << "Case #" << tests << ": " ;

		if ( res==-1 ) cout << "IMPOSSIBLE" << endl ;
		else cout << res << endl ;
	}
}