#include <stdio.h>


int main()
{
	int T,C=1;
	int i,j,a[4][4],b[4][4];
	bool possiblemove;
	char tmp;
	scanf("%d",&T);
	getchar();
	while(T--)
	{
		possiblemove=false;
		tmp='a';
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				a[i][j]=getchar();
				if(a[i][j]=='.') {possiblemove=true;a[i][j]=b[i][j]=tmp++;}
				else if(a[i][j]=='X') {b[i][j]=tmp++;a[i][j]='X';}
				else if(a[i][j]=='O') {a[i][j]=tmp++;b[i][j]='O';}
				else if(a[i][j]=='T') {a[i][j]='X';b[i][j]='O';}
			}
			getchar();
		}
		/*for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				putchar(a[i][j]);
			}
			putchar('\n');
		}*/
		printf("Case #%d: ",C++);
		if(a[0][0]==a[1][0] && a[1][0]==a[2][0] && a[1][0]==a[3][0]) printf("X won\n");
		else if(a[0][1]==a[1][1] && a[1][1]==a[2][1] && a[1][1]==a[3][1]) printf("X won\n");
		else if(a[0][2]==a[1][2] && a[1][2]==a[2][2] && a[1][2]==a[3][2]) printf("X won\n");
		else if(a[0][3]==a[1][3] && a[1][3]==a[2][3] && a[1][3]==a[3][3]) printf("X won\n");
		
		else if(a[0][0]==a[0][1] && a[0][1]==a[0][2] && a[0][1]==a[0][3]) printf("X won\n");
		else if(a[1][0]==a[1][1] && a[1][1]==a[1][2] && a[1][1]==a[1][3]) printf("X won\n");
		else if(a[2][0]==a[2][1] && a[2][1]==a[2][2] && a[2][1]==a[2][3]) printf("X won\n");
		else if(a[3][0]==a[3][1] && a[3][1]==a[3][2] && a[3][1]==a[3][3]) printf("X won\n");
		
		else if(a[0][0]==a[1][1] && a[1][1]==a[2][2] && a[1][1]==a[3][3]) printf("X won\n");
		else if(a[0][3]==a[1][2] && a[1][2]==a[2][1] && a[1][2]==a[3][0]) printf("X won\n");
		
		else if(b[0][0]==b[1][0] && b[1][0]==b[2][0] && b[1][0]==b[3][0]) printf("O won\n");
		else if(b[0][1]==b[1][1] && b[1][1]==b[2][1] && b[1][1]==b[3][1]) printf("O won\n");
		else if(b[0][2]==b[1][2] && b[1][2]==b[2][2] && b[1][2]==b[3][2]) printf("O won\n");
		else if(b[0][3]==b[1][3] && b[1][3]==b[2][3] && b[1][3]==b[3][3]) printf("O won\n");
		
		else if(b[0][0]==b[0][1] && b[0][1]==b[0][2] && b[0][1]==b[0][3]) printf("O won\n");
		else if(b[1][0]==b[1][1] && b[1][1]==b[1][2] && b[1][1]==b[1][3]) printf("O won\n");
		else if(b[2][0]==b[2][1] && b[2][1]==b[2][2] && b[2][1]==b[2][3]) printf("O won\n");
		else if(b[3][0]==b[3][1] && b[3][1]==b[3][2] && b[3][1]==b[3][3]) printf("O won\n");
		
		else if(b[0][0]==b[1][1] && b[1][1]==b[2][2] && b[1][1]==b[3][3]) printf("O won\n");
		else if(b[0][3]==b[1][2] && b[1][2]==b[2][1] && b[1][2]==b[3][0]) printf("O won\n");
		
		else if(possiblemove) printf("Game has not completed\n");
		else printf("Draw\n");

		getchar();
	}
	return 0;
}
