
#include <cstdio>
//#define MAX_C 1
//#define MAX_D 1
//#define MAX_N 10
#define MAX_C 36
#define MAX_D 28
#define MAX_N 100
#define NUMBER_ELEMENTS 3

int main( void ){

	int T, cases=1 ;
	int C, D, N ;
	char combine[MAX_C][NUMBER_ELEMENTS+1] ;
	char opposed[MAX_D][NUMBER_ELEMENTS+1] ;
	char invoke[MAX_N+1] ;
	char list[MAX_N+1], *in, *out ;

	scanf("%d", &T );
	while( T-- ){
		scanf("%d", &C );
		for(int i=0; i<C ; ++i ){
			scanf("%s", &combine[i][0] ) ;
		}
		scanf("%d", &D );
		for(int i=0; i<D ; ++i ){
			scanf("%s", &opposed[i][0] ) ;
		}
		scanf("%d", &N ) ;
		scanf("%s", invoke ) ;

		out = list ;
		in = invoke ;
		char first, second ;
		first = *in ;
		while( *in++ != '\0' ){
			second = *in ;
			for(int i=0; i<D ; ++i ){
				if( first == opposed[i][0] ){
					char *aux ;
					for( aux=list ; aux<out ; ++aux ){
						if( *aux == opposed[i][1] ){
							out = list ;
							goto continuE ;
						}
					}
				}
				if( first == opposed[i][1] ){
					char *aux ;
					for( aux=list ; aux<out ; ++aux ){
						if( *aux == opposed[i][0] ){
							out = list ;
							goto continuE ;
						}
					}
				}
			}
			for(int i=0; i<C ; ++i ){
				if( first == combine[i][0] && second == combine[i][1] ){
					*out++ = combine[i][2] ;
					++in ;
					goto continuE ;
				}
				if( second == combine[i][0] && first == combine[i][1] ){
					*out++ = combine[i][2] ;
					++in ;
					goto continuE ;
				}
			}
			if( second == '\0' ){
				*out++ = first ;
				break ;
			}
			*out++ = first ;
continuE :
			first = *in ;
		}
		*out = '\0' ;
		if( list[0] == '\0' )
			printf("Case #%d: []\n", cases++ ) ;
		else{
			printf("Case #%d: [%c", cases++, list[0] ) ;
			out = &list[1] ;
			for( ; *out != '\0' ; ++out ){
				printf(", %c", *out ) ;
			}
			printf("]\n" ) ;
		}  //// */
	
	}

	return 0 ;
}


