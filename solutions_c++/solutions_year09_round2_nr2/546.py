#include <iostream>
#include <algorithm>
using namespace std;

char str[ 1000 ];
char R[ 1000 ];

int i, j;
int Min, u ;

int main() {

	int t;
	int ty;

	freopen ( "B-large.in", "r", stdin );
	freopen ( "B-large.out", "w", stdout );

	scanf("%d", &t);
	ty = t;

	while( t-- ) {

		scanf("%s", str);
		strcpy( R, str );

		printf("Case #%d: ", ty - t );
		int len = strlen( str );
		if( len == 1 ) {
			printf("%s0\n", str);
			continue;
		}

		int flag = 0;
		for(i = len - 2; i >= 0; i--) {
			Min = 1000000;
			u = -1;

			for(j = i+1; j < len; j++) {
				if( str[j] > str[i] ) {
					if( str[j] < Min ) {
						Min = str[j];
						u = j;
					}
				}
			}

			if( Min != 1000000 ) {
				char temp = str[i];
				str[i] = str[u];
				str[u] = temp;
				sort( str+i+1, str+len );
				puts( str );
				flag = 1;
				break;
			}
		}

		if( !flag ) {
			sort( R, R + len );

			for(i = 0; i < len; i++) {
				if( R[i] != '0' ) {
					printf("%c", R[i]);
					break;
				}
			}
			for( j = 0; j <= i; j++) {
				printf("0");
			}

			for( j = i + 1; j < len; j++) {
				printf("%c", R[j]);
			}
			puts("");
		}
	}
	return 0; 
}
