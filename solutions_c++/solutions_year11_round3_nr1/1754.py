# include <cstdio>
# include <cstdlib>
# include <vector>
# include <set>
# include <map>
# include <deque>
# include <algorithm>
# include <cctype>
# include <iostream>
# include <cstring>
# include <fstream>

# define FR(i, n)           for( int i = 0; i < n; i++)
# define FRin(i, m, n)     for( int i = m; i < n; i++)
# define FRrev(i, n)         for( int i = n; i >= 0; i-- )
# define PF    printf
# define SF    scanf
# define PB    push_back

using namespace std;

int main()
{
	ifstream in ("input.txt", ios::in);
	ofstream out ("output1s.txt",ios::out);
	
	int test;
	int testi = 0;
	
	in >> test;
	
	char tile[50][50];
	
	while ( test -- )
	{
			testi ++;
			int r, c;
			in >> r >> c;
			FR ( i, r )
			{
				FR ( j, c )
				in >> tile [i] [j];
			}
			
			bool done = false;
			bool possible = true;
			
			FR ( i, r )
			{
				FR ( j, c )
				{
					if ( tile [i][j] == '#' )
					{
						if ( j == c-1 || i == r - 1)
						{
							possible = false;
						}
						else
						{
							if ( tile [i][j+1] == '#' && tile [i+1][j] == '#' && tile[i+1][j+1] == '#')
							{
								tile [i][j] = '/';
								tile[i][j+1] = '\\';
								tile [i+1][j] = '\\';
								tile [i+1][j+1] = '/';
							}
							else
							{
								possible = false;
								break;
							}
						}
					}
				}
				if ( !possible )
				break;
			}
			
			out << "Case #" << testi << ":" << endl;
			
			if ( possible )
			{
				FR ( i, r )
				{
					FR ( j, c)
					{
						out << tile [i] [j];
					}
					out << endl;
				}
			}
			else
			{
				out << "Impossible" << endl;
			}
			
	}
	
	in . close();
	out . close ();	
	return 0;
}
