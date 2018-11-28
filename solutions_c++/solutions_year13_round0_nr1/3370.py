#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <fstream>

using namespace std;

int r;

void check( vector < vector < char > > v, int flag, int number )
{
	char c1 = v[0][0];
	if ( c1 == 'T')
		c1 = v[1][1];
	bool f1 = true;
        for ( int i = 0; c1 != '.' && i < 4; i++ ) {
		if ( v[i][i] == 'T' )
			continue;
		if ( c1 != v[i][i] ) {
			f1 = false;
			break;
		}
	}
	if ( f1 == true && c1 != '.' ) {
                cout << "Case #"<< number << ": " << c1 << " won\n";
		return;
	}

	c1 = v[0][3];
	if ( c1 == 'T' )
		c1 = v[1][2];
	f1 = true;
        for ( int i = 0; c1 != '.' && i < 4; i++ ) {
		if ( v[i][3-i] == 'T' )
			continue;
                if ( c1 != v[i][3-i] ) {
                        f1 = false;
                        break;
                }
        }

        if ( f1 == true && c1 != '.' ) {
                cout << "Case #"<< number << ": " << c1 << " won\n";
                return;
        }

	for( int i = 0; i < 4; i++ ) {
		char c = v[i][0];
		if ( c == 'T' )
			c = v[i][1];
		bool f = true;
		for ( int j = 0; j < 4; j++ ) {
			if ( v[i][j] == 'T' )
				continue;
			if ( c != v[i][j] ) {
				f = false;
				break;
			}
		}
		if ( c!= '.' && f == true ) {
                        cout << "Case #"<< number << ": " << c << " won\n";
			return;
		}
	}

	for ( int j = 0; j < 4; j++ ) {
                char c = v[0][j];
		if ( c == 'T' )
			c = v[1][j];
                bool f = true;
                for ( int i = 0; i < 4; i++ ) {
			if ( v[i][j] == 'T' )
				continue;
                        if ( c != v[i][j] && c != 'T'  ) {
                                f = false;
                                break;
                        }       
                }
                if ( c != '.' && f == true ) {
                        cout << "Case #"<< number << ": " << c << " won\n";
                        return;
                }
        }

		
	if ( flag == 1 )
		cout << "Case #"<< number << ": Game has not completed\n";
	else
		cout << "Case #"<< number << ": Draw\n";
}


int main()
{
	int t;
	int f = 0;
	vector < char > v;
	vector < vector < char > > vov;
	char s[4];
	cin >> t;
	fflush(stdin);

	for ( int i = 0; i < t*4; i++ ) {
		cin >> s;
		                   
		for ( int j = 0; j < 4; j++ ) {
			v.push_back(s[j]);
			if ( s[j] == '.' && f == 0 )
				f = 1;
		}
		vov.push_back(v);
		v.clear();
		if ( i % 4 == 3 ) {
			gets(s);
			check (vov,f, i/4 + 1);
			vov.clear();
			f = 0;
		}
	}
	
	return 0;
}

