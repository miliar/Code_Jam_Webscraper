#include <stdio.h>
#include <string.h>

#define MAX 100

char board[MAX][MAX];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		int n,m;
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;++i)
			scanf("%s",&board[i]);
		bool bad=false;
		for(int i=0;i<n && !bad;++i) {
			for(int j=0;j<m && !bad;++j) {
				if(board[i][j]=='#') {
					if(j+1<m && board[i][j+1]=='#' &&
					   i+1<n && board[i+1][j]=='#' && board[i+1][j+1]=='#') {
						board[i][j]='/';
						board[i][j+1]='\\';
						board[i+1][j]='\\';
						board[i+1][j+1]='/';
					}
					else bad=true;
				}
			}
		}
		printf("Case #%d:\n",test);
		if(bad)
			printf("Impossible\n");
		else
			for(int i=0;i<n;++i)
				printf("%s\n",board[i]);
	}
	return 0;
}
