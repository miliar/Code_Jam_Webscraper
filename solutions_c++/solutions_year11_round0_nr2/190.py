#include<cstdio>
#include<cstring>
#include<algorithm>
#include<queue>

using namespace std;

char combine[26][26];
bool destroy[26][26];
char stack[1024];
int ss;

int main() {
	int T, N;
	char line[1024];
	
	scanf("%d", &T);
	
	for(int nCase = 1; nCase <= T; nCase++) {
		memset(combine, -1, sizeof(combine));
		memset(destroy, 0, sizeof(destroy));
		
		scanf("%d ", &N);
		for(int i = 0; i < N; i++) {
			scanf("%s", line);
			combine[line[0]-'A'][line[1]-'A'] = combine[line[1]-'A'][line[0]-'A'] = line[2];
		}
		
		scanf("%d ", &N);
		for(int i = 0; i < N; i++) {
			scanf("%s", line);
			destroy[line[0]-'A'][line[1]-'A'] = destroy[line[1]-'A'][line[0]-'A'] = true;
		}
		
		scanf("%d %s", &N, line);
		memset(stack, 0, sizeof(stack));
		ss = 0;
		for(int i = 0; line[i]; i++) {
			stack[ss++] = line[i];
			
			if(ss > 1 && combine[stack[ss-1]-'A'][stack[ss-2]-'A'] != -1) {
				stack[ss-2] = combine[stack[ss-1]-'A'][stack[ss-2]-'A'];
				stack[ss-1] = 0;
				ss--;
				
				continue;
			}
			
			for(int j = 0; j < ss-1; j++) {
				if(destroy[stack[ss-1]-'A'][stack[j]-'A']) {
					memset(stack, 0, sizeof(stack));
					ss = 0;
					break;
				}
			}
		}
		
		printf("Case #%d: [", nCase);
		for(int i = 0; i < ss; i++) {
			if(i) printf(", ");
			printf("%c", stack[i]);
		}
		printf("]\n");
	}
}
