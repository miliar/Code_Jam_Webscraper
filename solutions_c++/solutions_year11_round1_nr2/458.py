#include<cstdio>
#include<cstring>
#include<algorithm>
#include<set>

using namespace std;

bool has[100][26];
bool valid[100];
char word[100][20];
int  len[100];
char letters[100];
char ans[100];

int T, N, M, worse;

int solve(int idx) {
	int score = 0;
	int remaining = N;
	int l = len[idx];
	char sofar[100];
	
	memset(sofar, -1, sizeof(sofar));

	for(int i = 0; i < N; i++) {
		if(!(valid[i] = (len[i] == l))) {
			remaining--;
		}
	}
	
	for(int i = 0; remaining > 1 && i < 26; i++) {
		bool tries = false;
		
		for(int it = 0; it < N; it++) {
			if(!valid[it]) continue;
			
			if(tries = has[it][letters[i] - 'a']) {
				break;
			}
		}
		
		if(!tries) continue;
		
		if(!has[idx][letters[i] - 'a']) {
			score++;
		} else {
			for(int k = 0; k < l; k++) {
				if(word[idx][k] == letters[i]) {
					sofar[k] = letters[i];
				}
			}
		}
		
		for(int it = 0; it < N; it++) {
			if(!valid[it]) continue;
			
			for(int k = 0; k < l; k++) {
				if((sofar[k] != -1 && word[it][k] != sofar[k]) || (sofar[k] == -1 && word[it][k] == letters[i])) {
					valid[it] = false;
					remaining--;
					break;
				}
			}
		}
	}
	
	return score;
}

int main() {
	scanf("%d\n", &T);
	
	for(int nCase = 1; nCase <= T; nCase++) {
		scanf("%d %d\n", &N, &M);
		
		memset(has, 0, sizeof(has));
		
		for(int i = 0; i < N; i++) {
			scanf("%s\n", word[i]);
			len[i] = strlen(word[i]);
			
			for(int k = 0; k < len[i]; k++) {
				has[i][word[i][k] - 'a'] = true;
			}
		}
		
		printf("Case #%d:", nCase);
		
		for(int i = 0; i < M; i++) {
			scanf("%s\n", letters);
		
			worse = -1;
			strcpy(ans, "");
			for(int j = 0; j < N; j++) {
				int tmp = solve(j);
				//printf("\t%s %d\n", word[j], tmp);
				if(worse < tmp) {
					worse = tmp;
				
					strcpy(ans, word[j]);
				}
			}
			
			printf(" %s", ans);
		}
		printf("\n");
	}
}

