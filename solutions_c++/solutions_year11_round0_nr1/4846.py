#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;

int main() {
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		int N, O_pos = 1, B_pos = 1;
		pair<char, int> sequence[100];
		int result = 0;
		scanf("%d", &N);
		for( int i = 0; i < N; ++i ){
			scanf(" %c %d", &sequence[i].first, &sequence[i].second);
		}
		int div = 0;
		bool isOrange = false;
		for( int i = 0; i < N; ++i ){
			int O_num = 1000, B_num = 1000;
			for( int j = i; j < N; ++j ){
				if( O_num == 1000 && sequence[j].first == 'O'  ){
					O_num = j;
				}
				if( B_num == 1000 && sequence[j].first == 'B' ){
					B_num = j;
				}
				if( O_num != 1000 && B_num != 1000 ){
					break;
				}
			}
			if( O_num < B_num ){
				div = result;
				result += abs(sequence[O_num].second-O_pos)+1;
				div = result - div;
				O_pos = sequence[O_num].second;
				if( sequence[B_num].second < B_pos ){
					B_pos += (B_pos-div<sequence[B_num].second?sequence[B_num].second-B_pos:-div);
				}
				else{
					B_pos += (B_pos+div>sequence[B_num].second?sequence[B_num].second-B_pos:div);
				}
			}
			else if( B_num < O_num ){
				div = result;
				result += abs(sequence[B_num].second-B_pos)+1;
				div = result - div;
				B_pos = sequence[B_num].second;
				if( sequence[O_num].second < O_pos ){
					O_pos += (O_pos-div<sequence[O_num].second?sequence[O_num].second-O_pos:-div);
				}
				else{
					O_pos += (O_pos+div>sequence[O_num].second?sequence[O_num].second-O_pos:div);
				}
			}
		}
		
		// for( int i = 0; i < N; ++i ){
		// 	int O_num = -1, B_num = -1;
		// 	for( int j = i; j < N; ++j ){
		// 		if( O_num == -1 && sequence[j].first == 'O' ){
		// 			O_num = j;
		// 		}
		// 		if( B_num == -1 && sequence[j].first == 'B' ){
		// 			B_num = j;
		// 		}
		// 		if( O_num != -1 && B_num != -1 ){
		// 			break;
		// 		}
		// 	}
		// 	// printf("%d %d\n", O_num, B_num);
		// 	// fflush(stdout);
		// 	while(1){
		// 		++result;
		// 		// printf("Time:%d\n", result);
		// 		// printf("%d %d\n", O_pos, sequence[O_num].second);
		// 		// printf("%d %d\n", B_pos, sequence[B_num].second);
		// 		// fflush(stdout);
		// 		// getchar();
		// 		if( O_num != -1 ){
		// 			if( sequence[i].first == 'O' && O_pos == sequence[O_num].second ){
		// 				if( B_pos != sequence[B_num].second ){
		// 					B_pos += (B_pos>sequence[B_num].second?-1:1);
		// 				}
		// 				break;
		// 			}
		// 			if( O_pos != sequence[O_num].second ){
		// 				O_pos += (O_pos>sequence[O_num].second?-1:1);
		// 			}
		// 		}
		// 		if( B_num != -1 ){
		// 			if( sequence[i].first == 'B' && B_pos == sequence[B_num].second ){	
		// 				if( O_pos != sequence[O_num].second ){
		// 					O_pos += (O_pos>sequence[O_num].second?-1:1);
		// 				}
		// 				break;
		// 			}
		// 			if( B_pos != sequence[B_num].second ){
		// 				B_pos += (B_pos>sequence[B_num].second?-1:1);
		// 			}
		// 		}
		// 	}
		// }
		
		printf("Case #%d: %d\n", Ti, result);
//		fflush(stdout);
	}
	return 0;
}
