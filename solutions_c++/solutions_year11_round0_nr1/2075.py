#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <map>
#include <string>
#include <set>
#include <vector>

using namespace std ;

const int MAX_N = 110 ;

int main(){
	int T ,cs = 0 ;
	int N , i;
	scanf("%d", &T) ;
	vector<int> O, B ;
	vector<char> order ;
	for (cs = 1 ; cs <= T ; cs ++ ){
		scanf("%d", &N) ;
		O.clear() ;
		B.clear() ;
		order.clear() ;
		char robot ;
		int position ;
		//putchar('\n') ;
		for ( i = 0 ; i < N ; i ++ ){
			scanf(" %c %d", &robot, &position) ;			
			if ( robot == 'O' ){
				O.push_back(position) ;
				order.push_back('O') ;
			} else {
				B.push_back(position) ;
				order.push_back('B') ;
			}
			//printf(" %c %d", robot, position) ;			
		}	
		//putchar('\n') ;
		//for (vector<char>::iterator it = order.begin() ;
		//		it != order.end() ; ++ it){
		//	printf("%c ", *it) ;
		//}
		//putchar('\n') ;
		O.push_back(1) ;
		B.push_back(1) ;
		int pos_O = 1 ;
		int pos_B = 1 ;
		int ans = 0 ;
		vector<int>::iterator it_O = O.begin() ;
		vector<int>::iterator it_B = B.begin() ;

		for (vector<char>::iterator it = order.begin() ;
				it != order.end() ; ++ it){
			if (*it == 'O' ){
				int t = abs(pos_O - *it_O) + 1 ;
				ans += t ;
				pos_O = *it_O ;
				if ( pos_B < *it_B ) {
					pos_B += t ;
					if ( pos_B > *it_B ){
						pos_B = *it_B ;
					}
				} else {
					pos_B -= t ;
					if ( pos_B < *it_B ){
						pos_B = *it_B ;
					}
				}
				++ it_O ;
				//printf("([O]O%d,B%d,%d) ", pos_O, pos_B, t) ;
			} else {
				int t = abs(pos_B - *it_B) + 1 ;
				ans += t ;
				pos_B = *it_B ;
				if ( pos_O < *it_O ) {
					pos_O += t ;
					if ( pos_O > *it_O ){
						pos_O = *it_O ;
					}
				} else {
					pos_O -= t ;
					if ( pos_O < *it_O ){
						pos_O = *it_O ;
					}
				}
				++ it_B ;
				//printf("([B]O%d,B%d,%d) ", pos_O, pos_B, t) ;
			}
		}
		//putchar('\n') ;

		printf("Case #%d: %d\n", cs, ans) ;
	}
	return 0 ;
}
