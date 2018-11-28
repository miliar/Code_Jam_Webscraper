#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		bool over=true;
		int ttt[4][4];
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
			{
				char c;
				scanf("%c",&c);
				if(c=='X')
					ttt[j][k]=1;
				else if(c=='O')
					ttt[j][k]=2;
				else if(c=='.')
					{
						ttt[j][k]=0;
						over=false;
					}
				else if(c=='T')
					ttt[j][k]=3;
				else
					k--;
			}
		int winner=0;
		for(int j=0;j<4;j++)
		{
			int row=0,col=0,dia1=0,dia2=0;
			for(int k=0;k<4;k++)
			{
				if(row>=0&&(ttt[j][k]==3||(row==0||ttt[j][k]==row/k)))
					row+=ttt[j][k]==3?1:ttt[j][k];
				else
					row=-1;
				if(col>=0&&(ttt[k][j]==3||(col==0||ttt[k][j]==col/k)))
					col+=ttt[k][j]==3?1:ttt[k][j];
				else
					col=-1;
				if(dia1>=0&&(ttt[k][k]==3||(dia1==0||ttt[k][k]==dia1/k)))
					dia1+=ttt[k][k]==3?1:ttt[k][k];
				else
					dia1=-1;
				if(dia2>=0&&(ttt[k][3-k]==3||(dia2==0||ttt[k][3-k]==dia2/k)))
					dia2+=ttt[k][3-k]==3?1:ttt[k][3-k];
				else
					dia2=-1;
				
			}
			//printf("%d: %d %d %d %d\n",j,row,col,dia1,dia2);
			if(row%4==0&&row!=0)
			{
				winner=row/4;
				break;
			}
			if(col%4==0&&col!=0)
			{
				winner=col/4;
				break;
			}
			if(dia1%4==0&&dia1!=0)
			{
				winner=dia1/4;
				break;
			}
			if(dia2%4==0&&dia2!=0)
			{
				winner=dia2/4;
				break;
			}
		}
		if(winner==0)
		for(int j=0;j<4;j++)
		{
			int row=0,col=0,dia1=0,dia2=0;
			for(int k=0;k<4;k++)
			{
				if(row>=0&&(ttt[j][k]==3||(row==0||ttt[j][k]==row/k)))
					row+=ttt[j][k]==3?2:ttt[j][k];
				else
					row=-1;
				if(col>=0&&(ttt[k][j]==3||(col==0||ttt[k][j]==col/k)))
					col+=ttt[k][j]==3?2:ttt[k][j];
				else
					col=-1;
				if(dia1>=0&&(ttt[k][k]==3||(dia1==0||ttt[k][k]==dia1/k)))
					dia1+=ttt[k][k]==3?2:ttt[k][k];
				else
					dia1=-1;
				if(dia2>=0&&(ttt[k][3-k]==3||(dia2==0||ttt[k][3-k]==dia2/k)))
					dia2+=ttt[k][3-k]==3?2:ttt[k][3-k];
				else
					dia2=-1;
				
			}
			if(row%4==0&&row!=0)
			{
				winner=row/4;
				break;
			}
			if(col%4==0&&col!=0)
			{
				winner=col/4;
				break;
			}
			if(dia1%4==0&&dia1!=0)
			{
				winner=dia1/4;
				break;
			}
			if(dia2%4==0&&dia2!=0)
			{
				winner=dia2/4;
				break;
			}
		}
		printf("Case #%d: ",i+1);
		if(winner==0&&over)
		{
			printf("Draw\n");
		}
		else if(winner==1)
		{
			printf("X won\n");

		}
		else if(winner==2)
		{
			printf("O won\n");
		}
		else
		{
			printf("Game has not completed\n");
		}

	}
	return 0;
}