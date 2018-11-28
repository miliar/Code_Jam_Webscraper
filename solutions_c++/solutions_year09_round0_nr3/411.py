#include<cstdio>
#include<cstring>

char message[19] = {'w', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'c', 'o', 'd', 'e', ' ', 'j', 'a', 'm'};
char line[3000];

int main(){
	int T, ca=0;
	scanf("%d", &T);
	gets(line);
	while (T--){
		gets(line);
		int L = strlen(line);
		int DP[L+1][19];
		memset(DP, 0, sizeof(DP));
		for (int i = 0 ; i < 19; ++i)
			for (int j = 0 ; j < L; ++j)
				if (line[j] == message[i]){
					if (!i) DP[j][i] = 1;
					else{
						for (int k = 0 ; k < j ; ++k){
							DP[j][i] += DP[k][i-1];
							if (DP[j][i] >= 10000) DP[j][i] %= 10000;
						}
					}
				}
		int ans = 0;
		for (int i = 0 ; i < L; ++i){
			ans += DP[i][18];
			if (ans >= 10000) ans %= 10000;
		}
		printf("Case #%d: %04d\n", ++ca, ans);
	}
	return 0;
}
