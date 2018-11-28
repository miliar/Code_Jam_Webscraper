#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const char *phrase = "welcome to code jam";

int DP[1000][21];
char line[1000];

int main() {
	int N, len;
	
	scanf("%d\n", &N);
	
	for(int ni = 1; ni <= N; ni++) {
		fgets(line, sizeof(line), stdin);
		len = strlen(line);
		
		if(line[len-1] == '\n')
			line[--len] = '\0';
		
		memset(DP, 0, sizeof(DP));
		
		DP[0][0] = 1;
		
		for(int i = 0; i < len; i++) {
			memcpy(DP[i+1], DP[i], sizeof(DP[0]));
			
			for(int j = 0; phrase[j]; j++) {
				if(line[i] == phrase[j])
					DP[i+1][j+1] = (DP[i+1][j+1] + DP[i+1][j]) % 1000;
			}
		}
		
		printf("Case #%d: %04d\n", ni, DP[len][19]);
	}
	
	return 0;
}
