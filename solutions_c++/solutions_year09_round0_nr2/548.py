#include <stdio.h>

#define UP 0
#define DOWN 1
#define LEFT 2
#define RIGHT 3

int m, n, cid;
int dir[105][105];
int w[105][105];
int a[105][105];

void fill(int i,int j){
	w[i][j] = cid;
	if(i>0 && dir[i-1][j]==DOWN)
		fill(i-1, j);
	if(i<m-1 && dir[i+1][j]==UP)
		fill(i+1, j);
	if(j>0 && dir[i][j-1]==RIGHT)
		fill(i, j-1);
	if(j<n-1 && dir[i][j+1]==LEFT)
		fill(i, j+1);
}

int main(void)
{
	int T, cs=0, i,j ;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&m,&n);
		for(i=0;i<m;i++)
			for(j=0;j<n;j++)
				scanf("%d",&a[i][j]);
		for(i=0;i<m;i++){
			for(j=0;j<n;j++){
				int bst=a[i][j],bd=-1;
				if(i>0 && bst>a[i-1][j])
					bd=UP, bst=a[i-1][j];
				if(j>0 && bst>a[i][j-1]){
					bd=LEFT, bst=a[i][j-1];
//					printf("i=%d, j=%d, bst=%d\n",i,j,bst);
				}
				if(j<n-1 && bst>a[i][j+1])
					bd=RIGHT, bst=a[i][j+1];
				if(i<m-1 && bst>a[i+1][j])
					bd=DOWN, bst=a[i+1][j];
				dir[i][j] = bd;
			}
		}
		cid=0;
		for(i=0;i<m;i++)
			for(j=0;j<n;j++)
				if(dir[i][j]==-1){
					++cid;
					fill(i,j);
				}
		/*for(i=0;i<m;i++,printf("\n"))
			for(j=0;j<n;j++)
				printf("%d ",dir[i][j]);*/
		char used[100]={0}, cx='a';
		printf("Case #%d:\n",++cs);
		for(i=0;i<m;i++)
			for(j=0;j<n;j++){
				if(!used[w[i][j]]){
					used[w[i][j]] = cx;
					cx++;	
				}
				printf("%c%c",used[w[i][j]], (j==n-1)? '\n':' ');
			}
	}
	return 0;
}
