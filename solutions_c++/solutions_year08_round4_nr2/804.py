#include <iostream>

using namespace std;

typedef int Int;

struct Triple
{
Int d, x, y;
Triple( Int q, Int w, Int e ) : d( q ), x( w ), y( e ) {}
};

Triple egcd( Int a, Int b )
{
	if( !b ) return Triple( a, Int( 1 ), Int( 0 ) );
	Triple q = egcd( b, a % b );
	return Triple( q.d, q.y, q.x - a / b * q.y );
}


template< class Int >
Triple ldioph( Int a, Int b, Int c )
{
	Triple t = egcd( a, b );
	if( c % t.d ) return Triple( 0, 0, 0 );
	t.x *= c / t.d; t.y *= c / t.d;
	return t;
}

int main()
{
	int t, A;
	int AA, BB, CC;
	int N, M;
	bool find;
	
	cin >> t;
	
	for(int _case = 1; _case <= t; _case++) {
		
		scanf("%d%d%d", &N, &M, &A);
		cout << "Case #" << _case << ": ";
		find = false;
		
		int i, j, ii, jj;	
		
		for(i = 0; i <= N; i++)
			for(j = 0; j <= M; j++)
				for(ii = 0; ii <= N; ii++)
					for(jj = 0; jj <= M; jj++) {
						if((i == ii) && (j == jj)) continue;
						AA = j-jj;
						BB = ii-i;
						CC = A - i*jj + ii*j;
						Triple t = ldioph(AA, BB, CC);
						if(!t.d) continue;
						if(t.x >= 0 && t.x <= N && t.y >= 0 && t.y <= M &&
							!(t.x == i && t.y == j) && !(t.x == ii && t.y == jj)) {
							cout << i << " " << j << " " << ii << " " << jj << " " << t.x << " " << t.y << endl;
							find = true;
							goto end;
						}
					}
		end:				
		if(!find) cout << "IMPOSSIBLE" << endl;
	}
	
	return 0;
}
