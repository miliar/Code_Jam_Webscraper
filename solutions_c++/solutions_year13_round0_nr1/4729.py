#include<stdio.h>
#include<string.h>
int X[16][16],O[16][16];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for ( int tt=1;tt<=T;tt++ ){
		printf("Case #%d: ",tt);
		scanf("\n");
		memset(X,0,sizeof X);
		memset(O,0,sizeof O);
		int end = 1;
		for ( int ii = 1;ii <= 4;ii ++ ){
			for ( int jj=1;jj<=4;jj++ ){
				char c;
				scanf("%c",&c);
				if ( c == '.' ) end = 0;
				else if ( c == 'T' ) 
				{
					X[ii][jj] = O[ii][jj] = 1;
					X[ii][0] += 1;
					X[0][jj] += 1;
					O[ii][0]+=1;
					O[0][jj]+=1;
				}
				else if ( c == 'X' )
				{
					X[ii][jj]=1;
					X[ii][0]+=1;
					X[0][jj]+=1;
				}
				else if ( c == 'O')
				{
					O[ii][jj]=1;
					O[ii][0]+=1;
					O[0][jj]+=1;
				} 	
			}
			scanf("\n");
		}
		int xx=0,oo=0;
		for( int i=1;i<=4;i++ ){
			xx|=X[i][0];
			xx|=X[0][i];
			oo|=O[i][0];
			oo|=O[0][i];
		}
		X[0][0]=X[1][1]+X[2][2]+X[3][3]+X[4][4];
		X[0][5]=X[1][4]+X[2][3]+X[3][2]+X[4][1];
		O[0][0]=O[1][1]+O[2][2]+O[3][3]+O[4][4];
		O[0][5]=O[1][4]+O[2][3]+O[3][2]+O[4][1];
		xx |= X[0][0];
		xx |= X[0][5];
		oo |= O[0][0];
		oo |= O[0][5];
		xx >>=2; oo>>=2; 
		if ( xx ) printf("X won\n");
		else if ( oo ) printf("O won\n");
		else if ( !end ) printf("Game has not completed\n");
		else printf("Draw\n");
	}
	return 0;
}
