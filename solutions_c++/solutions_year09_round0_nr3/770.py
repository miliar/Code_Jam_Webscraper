#include <iostream> 
using namespace std;

int dp[510][20];
int main(){
	int i, j, t, n, len, tmp;
	char str[510];
	const char pat[20]= "welcome to code jam";
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&n);
	getchar();
	for( t= 1; t<= n; t++ ){
		gets(str);
		len= strlen(str);
		for( i= 0, j= 0; i< len; i++ ){
			if( str[i]=='w' )	j++;
			dp[i][0]= j;
		}
		for( j= 1; j<= 18; j++ ){
			for( i= 1, tmp= 0; i< len; i++ ){
				if( str[i]==pat[j] )
					tmp= ( dp[i-1][j]+ dp[i][j-1] )%10000;
				dp[i][j]= tmp;
			}
		}
		printf("Case #%d: %04d\n",t,dp[len-1][18]);
	}
	return 0;
}