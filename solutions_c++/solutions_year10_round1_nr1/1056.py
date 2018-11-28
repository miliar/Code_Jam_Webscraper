#include <iostream>
using namespace std;

char matriz[ 50 ][ 50 ];
char rotacionada[ 50 ][ 50 ];
int n, k , t;
char buff;

void rotacionar(){
	for( int j = 0; j < n; ++j ){
		for( int i = 0; i < n; ++i )
			rotacionada[ j ][ n - 1 - i ] = matriz[ i ][ j ];
	}
}

void aplicarGravidade(){
	for( int j = 0; j < n; ++j ){
		int i = n - 2;
		while( i >= 0 ){
			if( i + 1 < n && rotacionada[ i ][ j ] != '.' && rotacionada[ i + 1 ][ j ] == '.' ){
				buff = rotacionada[ i ][ j ];
				rotacionada[ i ][ j ] = '.';
				rotacionada[ i + 1 ][ j ] = buff;
				++i;
			}else
				--i;
		}
	}
}

bool r, b;

int verificar(){
	int rr = 0, rb = 0, colr = 0, colb = 0, digr = 0, digb = 0;
	for( int i = 0; i < n; ++i ){
		for( int j = 0; j < n; ++j ){
			//Verifica a linha
			if( rotacionada[ i ][ j ] == 'R' ){
				++rr;
				rb = 0;
			}else if( rotacionada[ i ][ j ] == 'B' ){
				++rb;
				rr = 0;
			}else{
				rb = 0;
				rr = 0;
			}
			if( rr >= k )
				r = true;
			else if ( rb >= k )
				b = true;
		}
		rr = 0, rb = 0;
	}

	for( int j = 0; j < n; ++j ){
		for( int i = 0; i < n; ++i ){
						//Verifica a coluna
			if( rotacionada[ i ][ j ] == 'R' ){
				++colr;
				colb = 0;
			}else if( rotacionada[ i ][ j ] == 'B' ){
				++colb;
				colr = 0;
			}else{
				colb = 0;
				colr = 0;
			}
			if( colr >= k )
				r = true;
			else if( colb >= k )
				b = true;
		}
		colr = 0, colb = 0;
	}

	for( int i = 0; i < n; ++i ){
		for( int j = 0; j < n; ++j ){
			digr = 0; digb = 0;
			if( i + k - 1 < n && rotacionada[ i ][ j ] == 'B' ){
				digb = 1;
				for( int h = 1; h < k; ++h ){
					if( rotacionada[ i + h ][ j + h ] == 'B' )
						++digb;
					else
						break;
				}
			}else if( i + k - 1 < n && rotacionada[ i ][ j ] == 'R' ){
				digr = 1;
				for( int h = 1; h < k; ++h ){
					if( rotacionada[ i + h ][ j + h ] == 'R' )
						++digr;
					else
						break;
				}
			}
			r = r || ( digr >= k );
			b = b || ( digb >= k );
		}
	}

	for( int i = 0; i < n; ++i ){
		for( int j = 0; j < n; ++j ){
			digr = 0; digb = 0;
			if( j - k + 1 >= 0 && i + k - 1 < n && rotacionada[ i ][ j ] == 'B' ){
				digb = 1;
				for( int h = 1; h < k; ++h ){
					if( rotacionada[ i + h ][ j - h ] == 'B' )
						++digb;
					else
						break;
				}
			}else if( j - k + 1 >= 0 && i + k - 1 < n && rotacionada[ i ][ j ] == 'R' ){
				digr = 1;
				for( int h = 1; h < k; ++h ){
					if( rotacionada[ i + h ][ j - h ] == 'R' )
						++digr;
					else
						break;
				}
			}
			r = r || ( digr >= k );
			b = b || ( digb >= k );
		}
	}
}

int main(){
	freopen( "A-large.in", "r", stdin );
	freopen( "out.txt", "w", stdout );

	cin >> t;

	for( int caso = 1; caso <= t; ++caso ){
		cin >> n >> k;
		b = false;
		r = false;

		for( int i = 0; i < n ; ++i ){
			for( int j = 0; j < n; ++j ){
				cin >> buff;
				matriz[ i ][ j ] = buff;
			}
			cin.ignore();
		}

		rotacionar();
		aplicarGravidade();
		verificar();

		cout << "Case #" << caso << ": ";
		if( b && r )
			cout << "Both";
		else if( b )
			cout << "Blue";
		else if( r )
			cout << "Red";
		else
			cout << "Neither";
		cout << endl;
	}
}
