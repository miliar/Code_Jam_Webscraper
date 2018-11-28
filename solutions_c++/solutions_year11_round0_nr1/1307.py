#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;

int abs( int a){
	if( a < 0 ) return -a;
	else return a;
}


int main() {
	int n , i , j , test , tc = 1;
	freopen("as.in","r",stdin);
	freopen("as.out","w",stdout);
	scanf("%d",&test);
	while( test-- && scanf("%d",&n) != EOF ) {
		int  pa , pb ,tmp;
		pa = pb = 1;
		int ta = 0 ,tb = 0 ,ans = 0;
		char s[100];
		for( i = 0 ; i < n;i++ ){
			scanf("%s%d",s,&tmp);
			if( strcmp( s,"B" ) == 0 ) {
				int dis = abs( tmp - pb );
				dis -= ( ans - tb );
				if( dis < 0 ) dis = 0;
				ans = ans + dis + 1;
				tb = ans;
				pb = tmp;
			}else {
				int dis = abs( tmp - pa );
				dis -= ( ans - ta );
				if( dis < 0 ) dis = 0;
				ans = ans + dis + 1;
				ta = ans;
				pa = tmp;
			}
		}
		printf("Case #%d: %d\n",tc++ ,ans );
	}
	return 0;

}
