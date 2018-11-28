
#include <cstdio>
//#define MAX_T 20
#define MAX_N 10
//#define MAX_T 100
//#define MAX_N 100
#define MAX_Pi 100
#define INFINITO 10*MAX_Pi
#define INICIO 1

int main( void ){

	int T, cases=1 ;
	int N ;
	int robot_O[MAX_N], robot_B[MAX_N] ;
	int *goal_O, *goal_B ;
	int sequence_P[MAX_N] ;
	char sequence_R[MAX_N] ;
	int seconds ;

	scanf("%d", &T ) ;
	while( T-- ){
		scanf("%d", &N ) ;

		goal_O = robot_O ;
		goal_B = robot_B ;
		char letter ;
		int number ;
		for(int i=0 ; i<N ; ++i){
			scanf(" %c%d", &letter, &number ) ;
			sequence_R[i] = letter ;
			sequence_P[i] = number ;
			if( letter == 'O' )
				*goal_O++ = number ;
			else
				*goal_B++ = number ;
		}
		*goal_O = INFINITO ;
		*goal_B = INFINITO ;

		seconds = 0 ;
		int O, B ;
		O = B = INICIO ;
		goal_O = robot_O ;
		goal_B = robot_B ;
		for(int i=0 ; i<N ; ++i){
			char robot ;
			int position ;
			robot = sequence_R[i] ;
			position = sequence_P[i] ;
			for( ;; ){
				if( robot == 'O' ){
					if( O == position ){
						if( B < *goal_B ){
							++B ;
						}else if( B > *goal_B ){
							--B ;
						}
						++seconds ;
						break ;
					}
				}else{
					if( B == position ){
						if( O < *goal_O ){
							++O ;
						}else if( O > *goal_O ){
							--O ;
						}
						++seconds ;
						break ;
					}
				}
				if( O < *goal_O ){
					++O ;
				}else if( O > *goal_O ){
					--O ;
				}
				if( B < *goal_B ){
					++B ;
				}else if( B > *goal_B ){
					--B ;
				}
				++seconds ;
			}
			if( robot == 'O' ){
				if( *(goal_O+1) != INFINITO )
					++goal_O ;
			}else if( *(goal_B+1) != INFINITO ){
				++goal_B ;
			}
		}
		printf("Case #%d: %d\n", cases++, seconds ) ;
	}

	return 0 ;
}
