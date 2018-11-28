#include<fstream>
#include<string>
#include<iostream>
using namespace std ;
#define fo(i, n) for (i=0 ; i < n ; i++)

char comb[200][200] ;
char opp[200][200] ;

void reset()
{
	int i, j ;
	fo(i, 200)
		fo(j, 200)
		comb[i][j] = opp[i][j] = ' ' ;
}
int main()
{
	ifstream cin("input.in") ;
	ofstream cout("output.out") ;
	int T, z, i, j, N, a ;

	cin >> T ;

	string s ;

	fo(z, T)
	{
		reset() ;

		cin >> a ;

		fo(i, a)
		{
			cin >> s ;
			comb[s[0]][s[1]] = comb[s[1]][s[0]] = s[2] ;
		}

		cin >> a ;

		fo(i, a)
		{
			cin >> s ;
			opp[s[0]][s[1]] = opp[s[1]][s[0]] = s[2] ;
		}

		cin >> a ;
		cin >> s ;

		int st=0, e = 1 ;	

		while (e < s.size())
		{
			if (comb[s[e]][s[e-1]]!=' ')
			{
				s[e-1] = comb[s[e]][s[e-1]] ;
				s.erase (s.begin() + e) ;
				continue ;
			}

			for (i = st ; i <= e ; i++)
				if (opp[s[i]][s[e]]!=' ')
				{
					st = e+1 ;
					e++ ;
					break ;
				}

			e++ ;

			
		}

		cout << "Case #" << z+1 << ": [" ;

		for (i=st ; i < s.size() ; i++)
		{
			if (i!=st)
				cout << ", " ;
			cout << s[i] ;
		}
		cout << "]" << endl ;

		
	}
	return 0 ;
}
