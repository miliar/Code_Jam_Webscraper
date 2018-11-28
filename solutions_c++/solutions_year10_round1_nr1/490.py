#include <cstdio>
#include <iostream>

using namespace std;

template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }


char  B[50][50];


int main()
{
	int  ncase;

	cin >> ncase;
	for(int nc=0; nc<ncase; nc++)
	{
		int  N, K;
		cin >> N >> K;

		for(int i=0; i<N; i++)
			for(int j=0; j<N; j++)
				cin >> B[i][j];

		for(int r=0; r<N; r++)
		{
			int to_c = N-1;
			for(int c=N-1; c>=0; c--)
				if ( B[r][c] != '.' )
				{   
					if ( to_c != c )
					{
						// move
						B[r][to_c] = B[r][c];
						B[r][c] = '.';
					}
					to_c--;
				}
		}

		int  blue_maxlen = 0;
		int  red_maxlen = 0;
		// row
		for(int r=0; r<N; r++)
		{
			char last = '.';
			int  len = 0;
			for(int c=0; c<N; c++)
			{
				char curr = B[r][c];
				if ( curr == last ) {
					len ++;
				} else if ( curr != last ) {
					if ( last == 'R' ) {
						red_maxlen += int(len >= K) ;
					} else if ( last == 'B' ) {
						blue_maxlen += int(len >= K);
					}
					len = 1;
				}	
				last = curr;
			}
			if ( last == 'R' ) {
				red_maxlen += int(len >= K) ;
			} else if ( last == 'B' ) {
				blue_maxlen += int(len >= K);
			}
		}

		// col
		for(int c=0; c<N; c++)
		{
			char last = '.';
			int  len = 0;
			for(int r=0; r<N; r++)
			{
				char curr = B[r][c];
				if ( curr == last ) {
					len ++;
				} else if ( curr != last ) {
					if ( last == 'R' ) {
						red_maxlen += int(len >= K) ;
					} else if ( last == 'B' ) {
						blue_maxlen += int(len >= K);
					}
					len = 1;
				}	
				last = curr;
			}
			if ( last == 'R' ) {
				red_maxlen += int(len >= K) ;
			} else if ( last == 'B' ) {
				blue_maxlen += int(len >= K);
			}
		}

		// diag /
		for(int i=0; i<N; i++)
		{
			char last = '.';
			int  len = 0;
			for(int j=0; j<i+1; j++)
			{
				char curr = B[i-j][j];
				if ( curr == last ) {
					len ++;
				} else if ( curr != last ) {
					if ( last == 'R' ) {
						red_maxlen += int(len >= K) ;
					} else if ( last == 'B' ) {
						blue_maxlen += int(len >= K);
					}
					len = 1;
				}	
				last = curr;
			}
			if ( last == 'R' ) {
				red_maxlen += int(len >= K) ;
			} else if ( last == 'B' ) {
				blue_maxlen += int(len >= K);
			}
		}

		// diag /
		for(int i=0; i<N-1; i++)
		{
			char last = '.';
			int  len = 0;
			for(int j=0; j<i+1; j++)
			{
				char curr = B[N-1-j][N-1-i+j];
				if ( curr == last ) {
					len ++;
				} else if ( curr != last ) {
					if ( last == 'R' ) {
						red_maxlen += int(len >= K) ;
					} else if ( last == 'B' ) {
						blue_maxlen += int(len >= K);
					}
					len = 1;
				}	
				last = curr;
			}
			if ( last == 'R' ) {
				red_maxlen += int(len >= K) ;
			} else if ( last == 'B' ) {
				blue_maxlen += int(len >= K);
			}
		}

		// diag 
		for(int i=0; i<N; i++)
		{
			char last = '.';
			int  len = 0;
			for(int j=0; j<i+1; j++)
			{
				char curr = B[i-j][N-1-j];
				if ( curr == last ) {
					len ++;
				} else if ( curr != last ) {
					if ( last == 'R' ) {
						red_maxlen += int(len >= K) ;
					} else if ( last == 'B' ) {
						blue_maxlen += int(len >= K);
					}
					len = 1;
				}	
				last = curr;
			}
			if ( last == 'R' ) {
				red_maxlen += int(len >= K) ;
			} else if ( last == 'B' ) {
				blue_maxlen += int(len >= K);
			}
		}

		// diag 
		for(int i=0; i<N-1; i++)
		{
			char last = '.';
			int  len = 0;
			for(int j=0; j<i+1; j++)
			{
				char curr = B[N-1-j][i-j];
				if ( curr == last ) {
					len ++;
				} else if ( curr != last ) {
					if ( last == 'R' ) {
						red_maxlen += int(len >= K) ;
					} else if ( last == 'B' ) {
						blue_maxlen += int(len >= K);
					}
					len = 1;
				}	
				last = curr;
			}
			if ( last == 'R' ) {
				red_maxlen += int(len >= K) ;
			} else if ( last == 'B' ) {
				blue_maxlen += int(len >= K);
			}
		}

		cout << "Case #" << nc+1 << ": ";

		bool  blue_ok = blue_maxlen >= 1;
		bool  red_ok = red_maxlen >= 1;

		if ( blue_ok && red_ok )
			cout << "Both" << endl;
		else if ( blue_ok && !red_ok )
			cout << "Blue" << endl;
		else if ( !blue_ok && red_ok )
			cout << "Red" << endl;
		else if ( !blue_ok && !red_ok )
			cout << "Neither" << endl;

/*
		for(int i=0; i<N; i++)
		{
			for(int j=0; j<N; j++)
				cout << B[i][j];
			cout << endl;
		}
*/
	}
}
