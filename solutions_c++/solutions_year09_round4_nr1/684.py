#include "stdio.h"
#include "string"
char maze[50][50];
void swap(char a[],char b[]) {
	char c[50];
	strcpy(c,a);
	strcpy(a,b);
	strcpy(b,c);
}
int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,n;
	scanf("%d",&T);
	for(int cas = 1; cas <= T ; cas ++) {
		scanf("%d",&n);
		for(int i = 0 ; i < n ; i ++) {
			scanf("%s",maze[i]);
		}
		int ans = 0;
		for(int i = 0 ; i < n ; i ++) {
			int idx = 0;
			for(idx = i; idx < n; idx ++) {
				int j;
				for(j = i+1 ; j < n ; j ++) {
					if(maze[idx][j] == '1') {
						break;
					}
				}
				if(j == n) {
					break;
				}
			}
			for(; idx > i ; idx --) {
				swap(maze[idx],maze[idx-1]);
				ans ++;
			}
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}