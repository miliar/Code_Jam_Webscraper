#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

char line[501];
int board[501][501];
typedef long long ll;
ll sumx[501][501],sumy[501][501],sumw[501][501];
int R,C,D;

void sumup(ll ss[][501]){
	for(int i = 1;i<=R;i++)
		for(int j = 1;j<=C;j++)
			ss[i][j] = ss[i - 1][j] + ss[i][j - 1] + ss[i][j] - ss[i - 1][j - 1];
}

inline ll getsum(ll ss[][501],int x1,int y1,int x2,int y2){
	return ss[x2][y2] - ss[x2][y1 - 1] - ss[x1 - 1][y2] + ss[x1 - 1][y1 - 1];
}

ll getblade(ll ss[][501],int x1,int y1,int x2,int y2){
	return getsum(ss,x1,y1,x2,y2) 
		- getsum(ss,x1,y1,x1,y1) - getsum(ss,x1,y2,x1,y2) - getsum(ss,x2,y1,x2,y1) - getsum(ss,x2,y2,x2,y2);
}

int main(){
	int tc;
	scanf("%d",&tc);
	memset(board,0,sizeof(board));
	memset(sumx,0,sizeof(sumx));
	memset(sumy,0,sizeof(sumy));
	memset(sumw,0,sizeof(sumw));
	for(int tt=1 ;tt<=tc;tt++){
		printf("Case #%d: ",tt);
		scanf("%d%d%d",&R,&C,&D);
		for(int i = 1;i<=R;i++){
			scanf("%s",line);
			for(int j = 1;j<=C;j++)
				board[i][j] = line[j - 1] - '0';
		}
		for(int i = 1;i<=R;i++) {
			for(int j = 1;j<=C;j++){
				board[i][j] += D;
				sumx[i][j] = board[i][j] * ((i<<1) + 1);
				sumy[i][j] = board[i][j] * ((j<<1) + 1);
				sumw[i][j] = board[i][j];
			}
		}
		/*for(int i = 1;i<=R;i++){
			for(int j = 1;j<=C;j++)
				printf("%lld ",sumw[i][j]);
			puts("");
		}*/
		sumup(sumx);
		sumup(sumy);
		sumup(sumw);
		/*for(int i = 1;i<=R;i++){
			for(int j = 1;j<=C;j++)
				printf("%lld ",sumx[i][j]);
			puts("");
		}*/
		int maxk = 0;
		ll sx,sy,sw;
		for(int i = 1;i<=R - 2;i++)
			for(int j = 1;j<=C - 2;j++){
				for(int k = max(maxk,3);k<=min(R - i + 1,C - j + 1);k++){
					sx = getblade(sumx,i,j,i + k - 1,j + k - 1);
					sy = getblade(sumy,i,j,i + k - 1,j + k - 1);
					sw = getblade(sumw,i,j,i + k - 1,j + k - 1);
					if((sx % sw!=0) || (sy % sw !=0))continue;
					if(sx / sw != (i<<1) + k || sy / sw != (j<<1) + k)continue;
					maxk = k;
				}
			}
		if(maxk==0)printf("IMPOSSIBLE\n");
		else printf("%d\n",maxk);
	}
	return 0;
}
