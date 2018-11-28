#include<cstdio>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<map>
#include<set>
using namespace std;
#define INF (1<<29)
#define min(x,y) (((x)<(y))?(x):(y))
#define max(x,y) (((x)>(y))?(x):(y))
#define FOR(i,x,y) for(int i=(x);i<(y);++i)
#define FOE(i,x,y) for(int i=(x);i<=(y);++i)
#define CLR(i) memset(i,0,sizeof(i))

int T, row[10][5],col[10][5],diag[5][5], empty;
char s[10][10],tmp[10];

int main(){
	scanf("%d",&T);
	FOE(t,1,T){
		empty = 0;
		CLR(row); CLR(col); CLR(diag);

		gets(tmp);
		FOR(i,0,4) gets(s[i]);

		FOR(i,0,4){
			FOR(j,0,4){
				if (s[i][j] == 'X'){
					++row[i][0], ++col[j][0];
					if (i==j) ++diag[0][0];
					if (i+j == 3) ++diag[1][0];
				}
				else if (s[i][j] == 'O'){
					++row[i][1], ++col[j][1];
					if (i==j) ++diag[0][1];
					if (i+j == 3) ++diag[1][1];
				}
				else if (s[i][j] == 'T'){
					++row[i][2], ++col[j][2];
					if (i==j) ++diag[0][2];
					if (i+j == 3) ++diag[1][2];
				}
				else ++empty;
			}
		}

		bool xwon, owon;
		xwon = owon = 0;
		FOR(i,0,4){
			//printf("%d: %d %d %d!\n",i,row[i][0],row[i][1],row[i][2]);
			//printf("%d: %d %d %d!\n",i,col[i][0],col[i][1],col[i][2]);
			if ((row[i][0] >= 3) && (row[i][0] + row[i][2] >= 4)) xwon = 1;
			if ((row[i][1] >= 3) && (row[i][1] + row[i][2] >= 4)) owon = 1;
			if ((col[i][0] >= 3) && (col[i][0] + col[i][2] >= 4)) xwon = 1;
			if ((col[i][1] >= 3) && (col[i][1] + col[i][2] >= 4)) owon = 1;
		}
		//printf("%d: %d %d %d!\n",0,diag[0][0],diag[0][1],diag[0][2]);
		//printf("%d: %d %d %d!\n",1,diag[1][0],diag[1][1],diag[1][2]);
		if ((diag[0][0] >= 3) && (diag[0][0] + diag[0][2] >= 4)) xwon = 1;
		if ((diag[0][1] >= 3) && (diag[0][1] + diag[0][2] >= 4)) owon = 1;
		if ((diag[1][0] >= 3) && (diag[1][0] + diag[1][2] >= 4)) xwon = 1;
		if ((diag[1][1] >= 3) && (diag[1][1] + diag[1][2] >= 4)) owon = 1;

		if (xwon && !owon) printf("Case #%d: X won\n",t);
		if (!xwon && owon) printf("Case #%d: O won\n",t);
		if (!xwon && !owon){
			if (empty == 0) printf("Case #%d: Draw\n",t);
			else printf("Case #%d: Game has not completed\n",t);
		}
	}
	return 0;
}
