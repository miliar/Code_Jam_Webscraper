#include <cstdio>
#include <cstring>
using namespace std;

const int MAXL = 500+10;
const char aim[] = "welcome to code jam";

char str[MAXL];
int ma[MAXL][20];
int s[MAXL][20];

int main(){
	int t;
	int m = strlen(aim);
	
	scanf("%d", &t);
	fgets(str, MAXL, stdin);
	for(int c=1; c<=t; ++c){
		fgets(str, MAXL, stdin);
		int n = strlen(str);
		memset(ma, 0, sizeof(ma));
		memset(s, 0, sizeof(s));
		
		ma[0][0] = str[0] == aim[0];
		s[0][0] = ma[0][0];
		
		for(int i=1; i<n; ++i){
			if(str[i] == aim[0])
				ma[i][0] = 1;
			s[i][0] = (s[i-1][0] + ma[i][0]) % 10000;
			for(int j=1; j<m; ++j){
				if(str[i] == aim[j]){
					ma[i][j] = s[i-1][j-1];
					ma[i][j] %= 10000;
				}else
					ma[i][j] = 0;
				s[i][j] = (s[i-1][j] + ma[i][j]) % 10000;
			}
		}
		
		printf("Case #%d: %0*d\n", c, 4, s[n-1][m-1]);
	}
}
