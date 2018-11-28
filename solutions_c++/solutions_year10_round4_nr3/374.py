#include <stdio.h>
#include <string.h>

bool a[2][128][128];
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int T,t,R,i,j,k,x1,y1,x2,y2,r,d,f;
	bool hf;
	scanf("%d",&T);
	for (t = 1;t <= T;t++){
		memset(a[0],0,sizeof(a[0]));
		scanf("%d",&R);
		for (i = 0;i < R;i++){
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (j = x1;j <= x2;j++)
				for (k = y1;k <= y2;k++)
					a[0][j][k] = true;
		}
		d = 0,f = 1;
		for (r = 1;;r++){
			memset(a[f],0,sizeof(a[f]));
			hf = false;
			//printf("Round %d : \n",r);
			//for (i = 1;i <= 6;i++){
			//	for (j = 1;j <= 6;j++)
			//		printf("%d",a[d][i][j]);
			//	printf("\n");
			//}getchar();
			for (i = 1;i <= 100;i++)
				for (j = 1;j <= 100;j++)
					if (!a[d][i][j-1] && !a[d][i-1][j])
						a[f][i][j] = false;
					else if ((a[d][i][j-1] && a[d][i-1][j]) || a[d][i][j]){
						a[f][i][j] = true;
						hf = true;
					}
			if (!hf) break;
			d = f,f ^= 1;
		}
		printf("Case #%d: %d\n",t,r);
	}
	fclose(stdout);
}
