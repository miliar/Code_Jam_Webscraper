
#include <iostream>
#include <vector>

using namespace std;

struct AREA
{
	int x1, x2, y1, y2;
};

int main()
{
	int C;
	cin >> C;

	for ( int c=0; c<C; c++ )
	{
		int R;
		cin >> R;

		vector<AREA> area(R);
		int w = 0;
		int h = 0;

		for ( int i=0; i<R; i++ )
		{
			cin >> area[i].x1 >> area[i].y1 >> area[i].x2 >> area[i].y2;
			w = max( w, area[i].x2+1 );
			h = max( h, area[i].y2+1 );
		}

		vector<vector<int> > field( w, vector<int>( h, 0 ) );

		for ( int i=0; i<R; i++ )
		{
			for ( int x=area[i].x1; x<=area[i].x2; x++ )
			for ( int y=area[i].y1; y<=area[i].y2; y++ )
				field[x][y] = 1;
		}

		for ( int t=0; ; t++ )
		{
			bool f = true;

			vector<vector<int> > temp = field;

			for ( int x=1; x<w; x++ )
			for ( int y=1; y<h; y++ )
			{
				if ( temp[x][y] == 1 )
					f = false;

				if ( temp[x][y] == 1  &&
					 temp[x-1][y] == 0  &&  temp[x][y-1] == 0 )
					field[x][y] = 0;

				if ( temp[x][y] == 0  &&
					 temp[x-1][y] == 1  &&  temp[x][y-1] == 1 )
					field[x][y] = 1;
			}

			//for ( int x=1; x<w; x++ ){
			//for ( int y=1; y<h; y++ )
			//	cout << field[x][y];
			//cout << endl;}
			//cout << endl;

			if ( f )
			{
				cout << "Case #" << (c+1) << ": " << t << endl;
				break;
			}
		}
	}
}

