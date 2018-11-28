#include <cstdio>
#include <cstring>
int L, D, N;
char dic[5000][16];
char group[15][27];
int ans;
void input(void){
	char ch;
	scanf("%d %d %d", &L, &D, &N);
	for(int i = 0; i < D; ++i)
		scanf(" %s ", dic[i]);
}
void getPos(void){
	char ch;
	int s = 0, len;
	int gLen = 0;
	while((ch = getchar()) != '\n'){
		if(ch == EOF) break;
		if(ch == '(') s = 1, len = 0;
		else if(ch == ')'){
			s = 0;
			group[gLen][len] = 0;
			++gLen;
		}else{
			if(s == 1)
				group[gLen][len++] = ch;
			else{
				group[gLen][0] = ch;
				group[gLen][1] = 0;
				++gLen;
			}
		}
	}
	ans = 0;
	bool valid;
	for(int i = 0; i < D; ++i){
		for(int j = 0; j < L; ++j){
			int len = strlen(group[j]);
			valid = false;
			for(int k = 0; k < len; ++k){
				if(dic[i][j] == group[j][k]){
					valid = true;
					break;
				}
			}
			if(!valid)	break;
		}
		if(valid) ++ans;
	}
}
int main(void){
	input();
	for(int i = 1; i <= N; ++i){
		getPos();
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}
