
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for ( int t=0; t<T; t++ )
	{
		int k;
		cin >> k;

		vector<vector<int> > dia( 2*k-1, vector<int>( 2*k-1, -1 ) );

		for ( int y=0; y<2*k-1; y++ )
		{
			//cout << y << ":" << abs(y-k+1) << "," << 2*k-2-abs(y-k+1) << endl;
			for ( int x=abs(y-k+1); x<=2*k-2-abs(y-k+1); x+=2 )
				cin >> dia[y][x];
		}

		//for ( int y=0; y<2*k-1; y++ )
		//{
		//	for ( int x=0; x<2*k-1; x++ )
		//		cout << dia[y][x];
		//	cout << endl;
		//}

		int ans = 100*k*k;
		int ax = 0;
		int ay = 0;

		for ( int cy=0; cy<2*k-1; cy++ )
		//for ( int cx=abs(cy-k+1); cx<=2*k-2-abs(cy-k+1); cx++ )
		for ( int cx=0; cx<2*k-1; cx++ )
		{
			bool f = true;

			for ( int y=0; y<2*k-1 && f; y++ )
			for ( int x=abs(y-k+1); x<=2*k-2-abs(y-k+1) && f; x+=2 )
			{
				{
				int rx = cx - (x-cx);
				if ( abs(y-k+1) <= rx  &&  rx <=2*k-2-abs(y-k+1)  &&
					 dia[y][rx] != dia[y][x] )
					f = false;
				}
				{
				int ry = cy - (y-cy);
				if ( 0 <= ry  &&  ry < 2*k-1  &&
					 abs(ry-k+1) <= x  &&  x <=2*k-2-abs(ry-k+1)  &&
					 dia[ry][x] != dia[y][x] )
					f = false;
				}
			}

			if ( f )
			{
				int tk = k + abs(cx-k+1) + abs(cy-k+1);
				ans = min( ans, tk*tk-k*k );
				//if ( tk*tk-k*k < ans )
				//	ans = tk*tk-k*k, ax = cx, ay = cy;
			}
		}

		cout << "Case #" << (t+1) << ": " << ans << endl;
		//cout << "Case #" << (t+1) << ": " << ans << "(" << ax << "," << ay << ")" << endl;
	}
}