#include <iostream>
using namespace std;
#include <cstdio>

bool f ( char x[], char & a)
{
	if ( (x[0] == 'T' || x[0] == 'X') && (x[1] == 'T' || x[1] == 'X') &&  (x[2] == 'T' || x[2] == 'X') && (x[3] == 'T' || x[3] == 'X')) {
        a = 'X';
		return true;
	}
	if ( (x[0] == 'T' || x[0] == 'O') && (x[1] == 'T' || x[1] == 'O') &&  (x[2] == 'T' || x[2] == 'O') && (x[3] == 'T' || x[3] == 'O')) {
        a = 'O';
		return true;
	}
	return false;

}




void main ()
{
	
freopen("2.in","r",stdin);
freopen("output.txt","w",stdout);
	char **a,  t = '.', m[4];
	int i, j, T, k = -1, r;

	
	
	cin >> T;
	
	a = new char * [4];
	for ( i = 0; i < 4; i++ )
		a[i] = new char [4];
	r = 0;
verj:;
	k++;
	r++;
	while (k < T){
		for ( i = 0; i < 4; i++ )
			for ( j = 0; j < 4; j++ )
				cin >> a[i][j];

		for ( i = 0; i < 4; i++ )
			if ( f(a[i], t) ) {
				cout <<"Case #" << r << ':' << ' ' << t << " won" << endl;
				goto verj;
			}

		for ( i = 0; i < 4; i++ ){
			for ( j = 0; j < 4; j++ ) 
			    m[j] = a[j][i];
				if ( f(m, t) ) {
				cout <<"Case #" << r << ':' << ' ' << t << " won" << endl;
				goto verj;
				}
			}

		for ( i = 0; i < 4; i++ )
			m[i] = a[i][i];
		if ( f(m, t) ) {
				cout <<"Case #" << r << ':' << ' ' << t << " won" << endl;
				goto verj;
				}
		for ( i = 0; i < 4; i++ )
		    m[i] = a[i][4-i-1];
		if ( f(m, t) ) {
				cout <<"Case #" << r << ':' << ' ' << t << " won" << endl;
				goto verj;
				}
		

		for ( i = 0; i < 4; i++ )
			for ( j = 0; j < 4; j++ )
				if ( a[i][j] == '.' ){
					cout << "Case #" << r << ':' << " Game has not completed" << endl;
					goto verj;
				}
				
		      

		cout << "Case #" << r << ": Draw" << endl;
					goto verj;
		
	}


	
}
