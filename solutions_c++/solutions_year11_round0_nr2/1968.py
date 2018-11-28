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
	int i, j, cs, T, C, D, N ;
	char list[MAX_N] ;
	int list_length ;
	char buf[MAX_N] ;
	map<string, char> combine ;
	set<string> oppose ;
	scanf("%d", &T) ;
	for ( cs = 1 ; cs <= T ; cs ++ ){
		combine.clear() ;
		oppose.clear() ;
		list_length = 0 ;

		scanf("%d", &C) ;
		for ( i = 0 ; i < C ; i ++ ){
			scanf("%s", buf) ;	
			char form = buf[2] ;
			buf[2] = '\0' ;
			combine[buf] = form ;
			swap(buf[0], buf[1]) ;
			combine[buf] = form ;
		}

		scanf("%d", &D) ;
		for ( i = 0 ; i < D ; i ++ ){
			scanf("%s", buf) ;
			oppose.insert(buf) ;
			swap(buf[0], buf[1]) ;
			oppose.insert(buf) ;
		}

		scanf("%d %s", &N, buf) ;
		for ( i = 0 ; i < N ; i ++ ){
			list[list_length] = buf[i] ;
			if ( list_length > 0 ) {
				string tmp = "" ;
				tmp += list[list_length - 1] ;
				tmp += list[list_length] ;
				if ( combine.count(tmp) ){
					list[list_length - 1] = combine[tmp] ;
					continue ;
				} else {
					for ( j = 0 ; j < list_length ; j ++ ){
						tmp = "" ;
						tmp += list[j] ;
						tmp += buf[i] ;
						if ( oppose.count(tmp) ){
							list_length = 0 ;
							break ;
						}
					}
					if ( list_length == 0 ) {
						continue ;
					}
				}
			}
			list_length ++ ;
		}

		printf("Case #%d: [", cs) ;
		for ( i = 0 ; i < list_length ; i ++ ){
			if ( i == 0 ){
			} else {
				putchar(',') ;
				putchar(' ') ;
			}
			putchar(list[i]) ;
		}
		putchar(']') ;
		putchar('\n') ;
	}
	return 0 ;
}
