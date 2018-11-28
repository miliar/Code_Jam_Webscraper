#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <map>
#include <queue>
#include <set>
#include <vector>


using namespace std;


int main(int argc, char* argv[]){
	int n;
	char s[510];
	char *src = "welcome to code jam";
	int srclen = strlen(src), slen;
	int *dp = (int*)malloc(sizeof(int)*srclen);

	scanf("%d",&n);
	getchar();
	for(int c = 1; c <= n; c++) {
		memset(dp,0,sizeof(int)*srclen);
		fgets(s,510,stdin);
		slen = strlen(s);
		for(int i = 0; i < slen; i++){
			for(int k = 0; k < srclen; k++){
				if(s[i] == src[k])
					dp[k] += k==0? 1:dp[k-1];
				if(dp[k] > 9999) dp[k] %= 10000;
			}
		}
		printf("Case #%d: %04d\n", c, dp[18]);	
	}

	return 0;
}

