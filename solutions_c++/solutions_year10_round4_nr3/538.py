#include <stdio.h>
#include <algorithm>
using namespace std;

int main()
{
	int c;
	scanf("%d", &c);
	for (int ca=1; ca<=c; ca++) {
		int r;
		scanf("%d", &r);
		
		int board[200][200] = {0};
		
		int live = 0;
		while (r--) {
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			x1--; y1--; x2--; y2--;
			for (int i=x1; i<=x2; i++)
				for (int j=y1; j<=y2; j++) {
					if (!board[j][i]) {
						board[j][i] = 1;
						live++;
					}
				}
		}
		
#define dump() do{ for (int i=0; i<20; i++) {for (int j=0; j<20; j++) printf("%d", board[i][j]); putchar(10); }printf("---\n");}while(0)

		int ans = 0;
		while (live) {
//			dump();
			ans++;
			live = 0;
			int b2[200][200] = {0};
			for (int i=0; i<200; i++)
				for (int j=0; j<200; j++)
					if (board[i][j]) {
						if ((i>0 && board[i-1][j]) || (j>0 && board[i][j-1])) {
							b2[i][j] = 1;
							live++;
						}
					}
					else {
						if (i>0 && j>0 && board[i-1][j] && board[i][j-1]) {
							b2[i][j] = 1;
							live++;
						}
					}
			memcpy(board, b2, sizeof(b2));
		}
		
		printf("Case #%d: %d\n", ca, ans);
	}
}
