#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <set>
#include <map>
#include <iostream>
#include <cmath>
#include <vector>
#include <list>
#include <ctype.h>
#include <stack>
#include <string>
#include <algorithm>
#include <sstream>
#include <queue>
using namespace std;
#define PB		push_back
#define ALL(v)		(v).begin() , (v).end()
#define SZ(v)		( (int) v.size() )
#define Set(v,x)	memset(  v , x , sizeof(v))
#define two(n)		( 1 << (n) )
#define contain(Set,i)  ( (Set) & two(i) )

char str[] = "welcome to code jam";
int dp[610][22];
char s[1000];

int main() {
	int i , j , t ,k, nt, lenstr = strlen(str);

	//printf("|%s|  %d, %d\n", str, lenstr, str[lenstr]);
	scanf("%d\n", &nt);
	for (t = 1 ; t <= nt ; t++) {
		fgets( s , 1000 , stdin);

		Set( dp , 0 );
		int len = strlen(s); 

		dp[len][lenstr] = 1;
		
		for ( i = len -1 ; i >= 0 ; i--) {
			for (j = 0 ; j < lenstr; j++) {
				if ( s[i] == str[j]) {
					for (k = i+1 ; k <= len ; k++) {
						if (s[k] == str[j+1]) {
							//printf("%d, soma %d    %d\n", k, j+1 , dp[k][j+1]);
							dp[i][j] = (dp[i][j] + dp[k][j+1]) % 10000;
						}
					}
				}
			}
		}
		//printf("s: %s  %d\n", s , len);
		j = 0;
		for (i = 0 ; i < len ; i++)
			j = (j+dp[i][0]) % 10000;
		printf("Case #%d: %04d\n", t , j);
	}
	return 0;
}

