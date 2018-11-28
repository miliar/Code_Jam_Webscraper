#include<iostream>
#include<fstream>
using namespace std ;
#define fo(i, n) for (i=0 ; i < n ; i++)

int main()
{
	ifstream cin("input.in") ;
	ofstream cout("output.out") ;

	int N, z, stall, i, T, butt ;
	char c, cur ;

	cin >> T ;

	fo(z, T)
	{
		int opos = 1, bpos = 1 ;
		stall = 0 ;
		cur = 'S' ;

		cin >> N ;

		int ret = 0 ;

		fo(i, N)
		{
			cin >> c >> butt ;

			if (c=='B')
			{
				ret+= abs(bpos - butt) + 1 ;

				if (cur==c)
					stall+= abs(bpos - butt) + 1 ;
				else
				{
					ret -= min (stall, abs(bpos-butt)) ;
					stall = (abs(bpos - butt) + 1) - min (stall, abs(bpos-butt)) ;
					cur = c ;
				}
				bpos = butt ;
			}
			else
			{
				ret+= abs(opos - butt) + 1 ;

				if (cur==c)
					stall+= abs(opos - butt) + 1 ;
				else
				{
					ret -= min (stall, abs(opos-butt)) ;
					stall = (abs(opos - butt) + 1) - min (stall, abs(opos-butt)) ;
					cur = c ;
				}
				opos = butt ;
			}
		}

		cout << "Case #" << z+1 << ": " << ret << endl ;
	}

	return 0 ;
}