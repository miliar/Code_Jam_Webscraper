#include <iostream>
#include <stdio.h>
using namespace std;
char g[4][4];
int main()
{
	freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
	int T,cas=0;
	scanf("%d",&T);
	while(T--)
	{
		cas++;
		int i,j;
		printf("Case #%d: ",cas);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++) cin>>g[i][j];
		}
		int X=0,O=0,num_p=0;
		for(i=0;i<4;i++)
		{
			if((g[i][0]=='X'||g[i][0]=='T')+(g[i][1]=='X'||g[i][1]=='T')+(g[i][2]=='X'||g[i][2]=='T')+(g[i][3]=='X'||g[i][3]=='T')>=4) X=1; 
			if((g[i][0]=='O'||g[i][0]=='T')+(g[i][1]=='O'||g[i][1]=='T')+(g[i][2]=='O'||g[i][2]=='T')+(g[i][3]=='O'||g[i][3]=='T')>=4) O=1; 
		}
		for(j=0;j<4;j++)
		{
			if((g[0][j]=='X'||g[0][j]=='T')+(g[1][j]=='X'||g[1][j]=='T')+(g[2][j]=='X'||g[2][j]=='T')+(g[3][j]=='X'||g[3][j]=='T')>=4) X=1; 
			if((g[0][j]=='O'||g[0][j]=='T')+(g[1][j]=='O'||g[1][j]=='T')+(g[2][j]=='O'||g[2][j]=='T')+(g[3][j]=='O'||g[3][j]=='T')>=4) O=1; 
		}
		if((g[0][0]=='X'||g[0][0]=='T')+(g[1][1]=='X'||g[1][1]=='T')+(g[2][2]=='X'||g[2][2]=='T')+(g[3][3]=='X'||g[3][3]=='T')>=4) X=1; 
		if((g[0][3]=='X'||g[0][3]=='T')+(g[1][2]=='X'||g[1][2]=='T')+(g[2][1]=='X'||g[2][1]=='T')+(g[3][0]=='X'||g[3][0]=='T')>=4) X=1;
		if((g[0][0]=='O'||g[0][0]=='T')+(g[1][1]=='O'||g[1][1]=='T')+(g[2][2]=='O'||g[2][2]=='T')+(g[3][3]=='O'||g[3][3]=='T')>=4) O=1;
		if((g[0][3]=='O'||g[0][3]=='T')+(g[1][2]=='O'||g[1][2]=='T')+(g[2][1]=='O'||g[2][1]=='T')+(g[3][0]=='O'||g[3][0]=='T')>=4) O=1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(g[i][j]=='.') num_p++; 
			} 
		} 
		if(X==1) printf("X won\n"); 
		else if(O==1) printf("O won\n"); 
		else if(num_p==0) printf("Draw\n");
		else printf("Game has not completed\n"); 
	}
	return 0;
}
