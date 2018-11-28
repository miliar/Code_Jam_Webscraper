#include <stdio.h>
#include <string.h>

int main() {
	int test , i , j , n , p , s ;
	scanf("%d",&test);
	for( int tc = 1 ;tc <= test ;++tc ) {
		scanf("%d%d%d",&n,&p,&s);
		int res = 0 , x = 0 , y = 0 ,z = 0;
		for( i = 0 ; i < n;i++ ) {
			scanf("%d",&j);
			int aver = j/3;
			if( j%3 == 2 ) {
				if( aver + 2 < s ) x ++;
				else if( aver + 2 == s ) y++;
				else z ++;
			} else if( j%3 == 1 ) {
				if( aver == 0 ) {
					if( aver+1 >= s ) res++;
				} else {
					if( aver + 1 < s ) x ++;
					else z++;
				}
			} else {
				if( aver == 0 ) {
					if( aver >= s ) res++;
				} else {
					if( aver + 1 < s ) x ++;
					else if( aver + 1 == s ) y++;
					else z++;
				}
			}
		}
		if( y >= p ) {
			res += z + p;
		}else {
			res += z + y;
		}
		printf("Case #%d: %d\n",tc,res);
	}
	//while(1);
	return 0;
}
