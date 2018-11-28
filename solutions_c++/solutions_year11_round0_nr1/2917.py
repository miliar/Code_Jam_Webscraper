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
	int test;
	SF ( "%d", &test);
	
	ofstream out ( "out1b.txt", ios::out );
	FRin ( testi, 1, test + 1)
	{
		int n;
		int oprev = 1;
		int otime = 0;
		int bprev = 1;
		int btime = 0;
		int ttime = 0;
		
		SF ( "%d", &n);
		FR ( i, n )
		{
			char r;
			int p;
			do 
			{
				SF ( "%c" , &r );
			}while ( r == ' ');
			SF ( "%d", &p);
			if ( 'O' == r )
			{
				int one = abs(p - oprev);
				int two = ( ttime - otime );
				if ( one <= two )
				{
					ttime += 1;
					oprev = p;
					otime = ttime;
				}
				else
				{
					ttime += one - two + 1;
					oprev = p;
					otime = ttime;
				}
				// cout << "ttime after n = "<< i << " in o is : " << ttime << " for r and p as " << r << "   " << p << endl;
			}
			else
			{
				int one = abs(p - bprev);
				int two = ( ttime - btime );
				if ( one <= two )
				{
					ttime += 1;
					bprev = p;
					btime = ttime;
				}
				else
				{
					ttime += one - two + 1;
					bprev = p;
					btime = ttime;
				}
				// cout << "ttime after n = "<< i << " in b is : " << ttime  << " for r and p as " << r << "   " << p << endl;
			}
		}
		
		PF ( "Case #%d: %d\n", testi, ttime );
		out << "Case #" << testi << ": " << ttime << endl;
	}
	out . close();
	return 0;
}

