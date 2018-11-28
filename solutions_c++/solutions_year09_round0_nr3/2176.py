#include <iostream>
using namespace std;
#define WELCOME_SIZE 19 //welcome to code jam
#define MAX_WORD 502
char welcome[] = "welcome to code jam";

int main()
{
	int DP[WELCOME_SIZE][MAX_WORD];
	
	char str[MAX_WORD];
	int tCase;
	scanf("%d\n", &tCase);
	for(int _case=1; _case <= tCase; ++_case){
		memset(str,0,sizeof(str));
		fgets(str, MAX_WORD, stdin);
		int strLen = (int)strlen(str);
		str[ strLen-1 ] = 0;
		strLen-=1;

		for(int i=0; i < WELCOME_SIZE; ++i)
			memset(DP+i, 0, sizeof(int)*MAX_WORD);

		for(int i=0; i < strLen; ++i)
			if( str[i] == 'w' ) 
				DP[0][i] = 1;

		for(int i=1; i < WELCOME_SIZE; ++i){
			for(int j=1; j < strLen; ++j){
				if( str[j] == welcome[i] ){
					int possible=0;
					for(int k=0; k < j; ++k){
						possible += DP[i-1][k];
						possible = possible > 10000 ? possible-10000 : possible;
					}					
					DP[i][j] = possible;
				}
			}
		}
		int answer=0;
		for(int i=0; i < strLen; ++i){
			answer += DP[18][i];
			answer = answer >= 10000 ? answer-10000 : answer;
		}
		
		char tmp[6];
		sprintf(tmp, "%d", answer);
		printf("Case #%d: ",_case);
		for(int i=0; i < 4-(int)strlen(tmp); ++i) printf("0");
		printf("%d\n", answer);

	}
	return 0;
}
