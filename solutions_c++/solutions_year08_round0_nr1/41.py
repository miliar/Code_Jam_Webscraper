#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#define MAXSEARCH 105
#define LONG 105
#define MAXQ 1005
#define BIG 1058233

using namespace std;

int dp[MAXSEARCH];

int a,b,c,d,e;
int jmlq;
int jmlsearch;
int jmlcase;

char nama[MAXSEARCH][LONG];
int code[MAXQ];
char hehe[LONG];

int match(void) {
	int aa;
	for (aa = 0;aa < jmlsearch;aa++) {
		if (strcmp(nama[aa],hehe) == 0) return aa;
		}
	return -1;
	}

int main() {
	
	scanf("%d",&jmlcase);
	for (e = 0;e < jmlcase;e++) {
		scanf("%d\n",&jmlsearch);
		for (a = 0;a < jmlsearch;a++) {
			scanf("%[^\n]s",nama[a]);
			getchar();
			//printf("%s\n",nama[a]);
			}
		scanf("%d\n",&jmlq);
		for (a = 0;a < jmlq;a++) {
			scanf("%[^\n]s",hehe);
			getchar();
			code[a] = match();
			//printf("%d %s : %d\n",a,hehe,code[a]);
			}
		
		memset(dp,0,sizeof(dp));
		
		for (a = 0;a < jmlq;a++) {
			c = code[a];
			for (b = 0;b < jmlsearch;b++) {	
				if (b == c) continue;
				dp[b] = min(dp[b],dp[c] + 1);
				}
			dp[c] = BIG;
			}
		
		int answer = BIG;
		for (a = 0;a < jmlsearch;a++) {
			answer = min(answer,dp[a]);
			}
		
		printf("Case #%d: ",e + 1);
		printf("%d\n",answer);
		}
	
	return 0;
	}
