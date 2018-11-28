#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int L;
char str[ 1000000 ];
char buf[ 1000 ];

struct point {
	char str[ 20 ];
	double Weight;
	int index;
}p[ 10000 ];
int T;

vector < int > vec[ 10010 ];
int s[ 10001 ], top;


map < string, int > Map;


double dfs( int key, double Sum ) {

	if( p[key].str[0] == 'X' )
		return Sum;

	string E = p[key].str;
	if( Map[ E ] ) {
		return dfs( vec[key][0], Sum*p[vec[key][0]].Weight);
	}else
		return dfs( vec[key][1], Sum*p[vec[key][1]].Weight);
}

int main() {
	int t;
	int i, j;
	int TT = 1;

	//freopen ( "A-large.in", "r", stdin );
	//freopen ( "A-large.out", "w", stdout );
	scanf("%d", &t);

	while( t-- ) {

		scanf("%d", &L );
		getchar();

		for(i = 0; i < 10010; i++) {
			vec[i].clear();
		}

		T = 1;
		top = 0;
		vec[0].clear();
		p[0].index = 0;
		p[0].Weight = 1;


		s[ top++ ] = 0;

		str[0] = '\0';
		for(i = 0; i < L; i++) {
			gets( buf );
			strcat( str, buf );
		}


		for(j = 0; str[j]; j++) {
			if( str[j] == '(' ) {
				while(1) {
					if( str[j] == '0' || str[j] == '1' )
						break;
					j ++;
				}	
				if( str[j] == '1' ) {
					p[ T ].Weight = 1;
				}else {
					p[ T ].Weight = 0;
				}
				if( str[j+1] == '.' ) {
					j += 2;

					double Q = 0.1;
					for( ; str[j] >= '0' && str[j] <= '9'; j++ ) {
						p[ T ].Weight += (double)(str[j] - '0') * Q ;
						Q /= 10.0;
					}
				}
				p[ T ].index = T;




				while( str[j] != ')' ) {
					if( str[j] >= 'a' && str[j] <= 'z' )
						break;
					j ++;
				}

				if( str[j] != ')' ) {
					int num = 0;
					for( ; str[j] >= 'a' && str[j] <= 'z'; j++ )
						p[ T ].str[ num++ ] = str[j];
					p[ T ].str[ num ] = '\0';
				}else
					p[T].str[0] = 'X';


				vec[ s[ top-1 ] ].push_back( T );

				s[ top++ ] = T;
				vec[T].clear();
				T ++;

				j--;
			}else if( str[j] == ')' ){
				top --;

			}
		}

		/*for(i = 0; i < T; i++) {

			printf("%d (%lf %s):", i, p[i].Weight, p[i].str );
			for(j = 0; j < vec[i].size(); j++) {
				printf("%s, ", p[ vec[i][j] ].str );
			}
			puts("");
		}*/
		
		int m, aa;

		printf("Case #%d:\n", TT++);
		scanf("%d", &m);

		while( m-- ) {
			scanf("%s", buf);
			scanf("%d", &aa);
			Map.clear();
			while( aa-- ) {
				scanf("%s", buf);
				string R = buf;
				Map[ R ] = 1;
			}
			if( T > 1 )
				printf("%.8lf\n", dfs(1, p[1].Weight) );
			else
				printf("%.8lf\n", 1 );
		}
	}
	return 0;
}

/*
2
13
(0.2 furry
  (0.81 fast
    (0.3)
    (0.2)
  )
  (0.1 fishy
    (0.3 freshwater
      (0.01)
      (0.01)
    )
    (0.1)
  )
)
*/