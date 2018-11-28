#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int main()
{
	int t;
	char b[4][4],ch;
	freopen("ain.txt","r",stdin);
	freopen("aout.txt","w",stdout);
	scanf("%d",&t);
	ch=fgetc(stdin);
	for(int i=1;i<=t;i++)
	{	
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
				scanf("%c",&b[j][k]);
			ch=fgetc(stdin);
		}
		ch=fgetc(stdin);
		int f=0;
		int complete=1;
		char w;
		for(int j=0;j<4;j++)
		{
			if(b[j][0]=='.' || b[j][1]=='.' || b[j][2]=='.' || b[j][3]=='.')
			{
				complete=0;
				continue;
			}
			if((b[j][0]==b[j][1] || b[j][0]=='T' || b[j][1]=='T') && (b[j][1] == b[j][2] || b[j][1]=='T' || b[j][2]=='T') && (b[j][2]==b[j][3] || b[j][2]=='T' || b[j][3]=='T'))
			{
				f=1;
				if(b[j][0]=='T')
					w=b[j][1];
				else
					w=b[j][0];
				break;
			}
		}
		if(f)
		{
			printf("Case #%d: ",i);
			printf("%c won",w);
			printf("\n");
			continue;
		}
		for(int j=0;j<4;j++)
		{	
			if(b[0][j]=='.' || b[1][j]=='.' || b[2][j]=='.' || b[3][j]=='.')
			{
				complete=0;
				continue;
			}
			if((b[0][j]==b[1][j] || b[0][j]=='T' || b[1][j]=='T') && (b[1][j] == b[2][j] || b[1][j] == 'T' || b[2][j]=='T') && (b[2][j]==b[3][j] || b[2][j]=='T' || b[3][j]=='T'))
			{
				f=1;
				if(b[0][j]=='T')
					w=b[1][j];
				else
					w=b[0][j];
				break;
			}
		}
		if(f && w!='.')
		{
			printf("Case #%d: ",i);
			printf("%c won",w);
			printf("\n");
			continue;
		}
		if(b[0][0]=='.' || b[1][1]=='.' || b[2][2]=='.' || b[3][3]=='.')
		{
			complete=0;
		}
		else if((b[0][0]==b[1][1] || b[0][0]=='T' || b[1][1]=='T') && (b[1][1] == b[2][2] || b[1][1] == 'T' || b[2][2]=='T') && (b[2][2]==b[3][3] || b[2][2]=='T' || b[3][3]=='T'))
		{
			f=1;
			if(b[0][0]=='T')
				w=b[1][1];
			else
				w=b[0][0];
		}
		if(f && w!='.')
		{
			printf("Case #%d: ",i);
			printf("%c won",w);
			printf("\n");
			continue;
		}
		if(b[0][3]=='.' || b[1][2]=='.' || b[2][1]=='.' || b[3][0]=='.')
		{
			complete=0;
		}
		else if((b[0][3]==b[1][2] || b[0][3]=='T' || b[1][2]=='T') && (b[1][2] == b[2][1] || b[1][2] == 'T' || b[2][1]=='T') && (b[2][1]==b[3][0] || b[2][1]=='T' || b[3][0]=='T'))
		{
			f=1;
			if(b[0][3]=='T')
				w=b[1][2];
			else
				w=b[0][3];
		}
		if(f && w!='.')
		{
			printf("Case #%d: ",i);
			printf("%c won",w);
			printf("\n");
			continue;
		}
		if(complete)
		{
			printf("Case #%d: ",i);
			printf("Draw");
			printf("\n");
		}
		else
		{
			printf("Case #%d: ",i);
			printf("Game has not completed");
			printf("\n");
		}
	}
	return 0;
}