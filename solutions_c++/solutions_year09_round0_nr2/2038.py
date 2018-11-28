#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int xdir[] = {-1,0,0,1};
int ydir[] = {0,-1,1,0};

int mat[100][100];
char ch[101][101];
int h,w,t;

bool is_valid(int x,int y)
{
	return !(x < 0 || x >= h || y < 0 || y >= w);
}

int main()
{
	freopen("2.in","rt",stdin);
	freopen("2.out","w",stdout);
	cin >> t;

	for( int tt = 0 ; tt < t ; tt++ )
	{
		cin >> h >> w;

		for( int i = 0 ; i < h ; i++ )
			for( int j = 0 ; j < w ; j++ )
				cin >> mat[i][j];

		for( int i = 0 ; i < h ; i++ )
			fill(ch[i],ch[i]+w,'~');

		char c = 'a';

		for( int i = 0 ; i < h ; i++ )
		{
			for( int j = 0 ; j < w ; j++ )
			{
				int x = i,y = j,nx,ny;
				vector<pair<int,int> > v;
				char mc = ch[i][j];

				while( true )
				{
					v.push_back(make_pair(x,y));

					int bestx = x,besty = y;

					for( int d = 0 ; d < 4 ; d++ )
					{
						nx = x + xdir[d];
						ny = y + ydir[d];

						if( !is_valid(nx,ny) )
							continue;

						if( mat[nx][ny] < mat[bestx][besty] )
						{
							bestx = nx;
							besty = ny;
						}
					}

					if( bestx == x && besty == y )
						break;

					x = bestx;
					y = besty;
					mc = min(mc,ch[x][y]);
				}

				if( ch[i][j] == '~' && mc == '~' )
					ch[i][j] = mc = c++;

				for( int k = 0 ; k < v.size() ; k++ )
					ch[v[k].first][v[k].second] = mc;
			}
		}

		cout << "Case #" << tt+1 << ":\n";

		for( int i = 0 ; i < h ; i++ )
		{
			for( int j = 0 ; j < w ; j++ )
			{
				if( j )
					cout << " ";

				cout << ch[i][j];
			}

			cout << endl;
		}
	}

	return 0;
}
