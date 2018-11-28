#include <cstdio>
#include <iostream>
#include <string>

using namespace std;
int const N = 50;

char const* ret[] = {
	  "Neither"
	, "Red"
	, "Blue"
	, "Both"
};

string a[N];
string b[N];

int const dy[] = { -1, -1, -1, 0, 1, 1, 1, 0 };
int const dx[] = { -1, 0, 1, 1, 1, 0, -1, -1 };

int main()
{
	int T;
	cin >> T;
	for( int C = 1; C <= T; ++C )
	{
		int n, K;
		cin >> n >> K;
		for( int i = 0; i != n; ++i )
		{
			cin >> a[i];
			b[i].resize(n);
		}
		
		// Rotate
		for( int i = 0; i != n; ++i )
		for( int j = 0; j != n; ++j )
			b[j][n-i-1] = a[i][j];
		
		/*cout << "Rotate:\n";
		for( int i = 0; i != n; ++i )
			cout << b[i] << endl;
		*/	
		for( int j = 0; j != n; ++j )
		{
			int k = n-1;
			for( int i = n-1; i >= 0; --i )
				if( b[i][j] != '.' )
					b[k--][j] = b[i][j];
			while( k >= 0 )
				b[k--][j] = '.';
		}
		
		/*cout << "Gravity:\n";
		for( int i = 0; i != n; ++i )
			cout << b[i] << endl;
		*/
		int rv = 0;
		
		for( int i = 0; i != n; ++i )
		for( int j = 0; j != n; ++j )
			if( b[i][j] != '.' )
			{
				bool ok;
				for( int k = 0; k != 8; ++k )
				{
					ok = true;
					for( int l = 0; l < K; ++l )
					{
						int y = i + l * dy[k];
						int x = j + l * dx[k];
						if( y < 0 || y >= n || x < 0 || x >= n || b[y][x] != b[i][j] )
						{
							ok = false;
							break;
						}
					}
					if( ok )
						break;
				}
				if( ok )
					rv |= (1<<(b[i][j]=='B'));
			}
			
		cout << "Case #" << C << ": " << ret[rv] << '\n';
	}
	return 0;
}