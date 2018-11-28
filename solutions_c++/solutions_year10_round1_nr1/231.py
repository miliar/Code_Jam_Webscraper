#include<stdio.h>
/*
Google Code Jam 2010
Round 1A
Rotate
*/
char board[60][60],in[60][60];
long n,k;
long dirs[4][2]={{1,0},{1,1},{0,1},{-1,1}};
long check(char c){
	long i,j,pd,l;
	for(i=0;i<n;i++)for(j=0;j<n;j++)if(board[i][j]==c){
		for(pd=0;pd<4;pd++){
			long pi=i+dirs[pd][0],pj=j+dirs[pd][1];
			for(l=1;l<k;l++){
				if(pi<0||pi>=n||pj<0||pj>=n||board[pi][pj]!=c)break;
				pi+=dirs[pd][0];
				pj+=dirs[pd][1];
			}
			if(l>=k)return 1;
		}
	}
	return 0;
}
void rotate(){
	long i,j;
	//rotate
	for(i=0;i<n;i++)for(j=0;j<n;j++){
		board[i][j]=in[n-j-1][i];
	}
	//fall
	for(i=0;i<n;i++){
		long p=n-1;
		for(j=n-1;j>=0;j--)if(board[j][i]!='.'){
			board[p][i]=board[j][i];
			p--;
		}
		for(j=p;j>=0;j--)board[j][i]='.';
	}
}
char ans[4][10]={"Neither","Red","Blue","Both"};
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	long z,zi;
	scanf("%ld",&z);
	for(zi=1;zi<=z;zi++){
		long i;
		scanf("%ld%ld",&n,&k);
		for(i=0;i<n;i++)scanf("%s",in[i]);
		rotate();
		long flag=0;
		if(check('R'))flag|=1;
		if(check('B'))flag|=2;
		printf("Case #%ld: %s\n",zi,ans[flag]);
	}
	return 0;
}
