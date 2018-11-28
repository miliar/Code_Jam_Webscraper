#include<string.h>
#include<stdio.h>

char board[55][55];
int t,n,k;
int dir[8][2]={{0,1},{1,0},{0,-1},{-1,0},{1,1},{1,-1},{-1,-1},{-1,1}};

void rotate(){
	for(int i=0;i<n;i++)
		for(int l=0;l<n;l++)
			for(int j=n-1;j>0;j--)
				if(board[i][j]=='.'){
					board[i][j]=board[i][j-1];
					board[i][j-1]='.';
				}
}

char what(int i,int j){
	if(i<0)return '.';
	if(j<0)return '.';
	if(i>=n)return '.';
	if(j>=n)return '.';
	return board[i][j];
}

int main()
{
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++){
		scanf("%d%d",&n,&k);
		for(int i=0;i<n;i++){
			scanf("%s",&board[i]);
		}
		rotate();
		bool red=0,blue=0;
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++){
				for(int d=0;d<8;d++){
					bool ored=1,oblue=1;
					for(int l=0;l<k;l++){
						if(what(i+l*dir[d][0],j+l*dir[d][1])!='R')
							ored=0;
						if(what(i+l*dir[d][0],j+l*dir[d][1])!='B')
							oblue=0;
					}
					if(ored)red=1;
					if(oblue)blue=1;
				}
			}
		printf("Case #%d: ",tt);
		if(red&&blue)printf("Both\n");
		else if(red)printf("Red\n");
		else if(blue)printf("Blue\n");
		else printf("Neither\n");
	}
	return 0;
}
