#include <stdio.h>
#include <string.h>

int visit[20][30];
char word[5009][20];
char mess[600];
int len;
int d;
int n;

void input() {
	int i;
	scanf("%d %d %d",&len,&d,&n);
	for(i = 0; i < d; i++) {
		scanf("%s",word[i]);
	}
}

void solve() {
	int i,j,ii,jj;
	int cur,curWord,count;
	int rank = 0;
	int x,y;
	int test;
	
	for(i = 0; i < n; i++) {
		scanf("%s",mess);
	/*	for(ii = 0 ; ii <= len; ii++ ) {
			for(jj = 0; jj <= 26; jj++ ) {
				visit[ii][jj] = false;
			}
		}*/
		memset(visit, 0, sizeof(visit));
		int kk = 0;
		for(j = 0,cur = 0; mess[j] != '\0'; j++ ) {
			if (mess[j] >= 'a' && mess[j] <= 'z') {
				visit[kk++][mess[j] - 'a'] = true;
			} else {
				int k;
				for (k = j + 1; mess[k] != ')'; ++k)
					visit[kk][mess[k] - 'a'] = true;
				++kk;
				j = k;
			}
		}
		count = 0;
		for(x = 0; x < d; x++ ) {
			//count = 0;
			for(y = 0; y < len; y++) {
				curWord = word[x][y] - 'a';
				if(!visit[y][curWord])
					break;
				//else if(visit[y][curWord])
				//	continue;
			}
			if(y == len)
				++count;
		}
//		for(cur = 0; cur <= len; cur++) {
//			for(test = 0; test < 26; test++) {
//				printf("cur = %d test = %d = %d\n",cur,test,visit[cur][test]);
//			}
//		}
		printf("Case #%d: %d\n",++rank,count);
	}
}

int main() {
	freopen("D:\\A-large.in", "r", stdin);
	freopen("D:\\A-large.out","w", stdout);
	input();
	solve();
	return 0;
}


