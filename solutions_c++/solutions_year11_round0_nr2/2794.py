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
	ofstream out ( "out2s.txt", ios::out );
	ifstream in ( "input.txt", ios::in);
	
	// SF ( "%d", &test);
	 in >> test;
	
	
	FRin ( testi, 1, test + 1)
	{
		int c;
		
		
		// SF ( "%d", &c );
		 in >> c;
		
		vector < string > comb [26];
		
		FR ( i, c )
		{
			char carr[4];
			
			// SF ( "%3s" , carr );
			 in >> carr;
			
			 cout << "We got a combinator: " << carr << " for i: " << i<< endl;
			 string s = carr;
			 comb [ ( s[0] - 'A' ) ] . PB ( s );
			 if ( s[1] != s[0] )
			 {
			 	char temp = s[0];
			 	s[0] = s[1];
			 	s[1] = temp;
			 	comb [ ( s[0] - 'A' ) ] . PB ( s );
			 }
		}
		
		int d;
		
		
		// SF ( "%d", &d );
		 in >> d;
		
		vector < string > red [26];
		
		FR ( i, d )
		{
			char carr[4];
			
			
			// SF ( "%2s" , carr );
			in >> carr;
			
			 cout << "We got a reducer: " << carr << " for i: " << i<< endl;
			 string s = carr;
			 red [ ( s[0] - 'A' ) ] . PB ( s );
			 if ( s[1] != s[0] )
			 {
			 	char temp = s[0];
			 	s[0] = s[1];
			 	s[1] = temp;
			 	red [ ( s[0] - 'A' ) ] . PB ( s );
			 }
		}
		
		int n;
		// SF ( "%d", &n);
		in >> n;
		
		char ch;
		
		do
		{
			// SF ( "%c" , &ch );
			in >> ch;
		}while ( ch == ' ');
		
		int nored [26];
		memset ( nored, 0, 26 * sizeof(int));
		vector < char > curr;
		curr . PB ( ch );
		nored [ ch - 'A' ] ++;
		int currsize = 0; // actually size minus 1
		FR ( i, n - 1)
		{
			// SF ( "%c" , &ch );
			in >> ch;
			if ( currsize == -1 )
			{
				curr . PB ( ch );
				currsize ++;
				nored [ch - 'A']++;
						cout << "curr size minus 1: " << " for ch "<< ch << endl;
			}
			else
			{
				char prev = curr [ currsize ];
				int previ = prev - 'A';
				int combsize = comb [ previ ] . size() ;
				vector < string > currco = comb [ previ ];
				bool done = false;
				FR ( j,  combsize)
				{
					if ( currco [ j ] [ 1 ] == ch )
					{
						nored [ curr [ currsize ] - 'A']--;
						curr [ currsize ] = currco [ j ] [ 2 ];
						cout << "combination done with prev element and produced: " << curr [ currsize ] << " for ch "<< ch << "AND CURRSIZE  "<< currsize<< endl;
						done = true;
						break;
					}
				}
				if ( !done ) // search for reducing elements
				{
					cout << "entered with curr size:" << currsize << endl;
					vector <string> currred = red [ ch - 'A' ];
					int redsize = currred . size();
					FR ( j, redsize )
					{
						char currcred = currred [j] [1];
						int redi = currcred - 'A';
						if ( nored [ redi ] != 0 )
						{
							curr . clear ();
							cout << "reduction done with prev element and produced: " << " for ch "<< ch << "AND CURRSIZE  "<< currsize<< endl;
							currsize = -1;
							memset ( nored, 0, 26 * sizeof ( int ) );
							
							done = true;
							break;
						}
					}
				}
				
				if ( !done ) // just add the current element
				{
					cout << "appended with prev element and produced: " << curr [ currsize ] << " for ch "<< ch << endl;
					curr . PB ( ch );
					currsize ++;
					nored [ ch - 'A'] ++;
						
				}
			}
		}
		
		PF ( "Case #%d: [" , testi);
		out << "Case #" << testi << ": [";
		FR ( i, currsize )
		{
			PF ( "%c, ", curr [i] );
			out << curr[i] << ", ";
		}
		if ( currsize >= 0 )
		{
			PF ( "%c", curr [ currsize ] );
			out << curr [ currsize ];
		}
		PF ( "]\n");
		out << "]" << endl;
	}
	return 0;
	out . close ();
	in . close ();
}

