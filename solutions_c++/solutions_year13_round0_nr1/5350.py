#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
	int t,count,i,status,j,winner,nob,k;
	char fc;
	char mat[6][6];
	char temp[5];
	scanf("%d",&t);
	count=1;
	while(t>0)
	{
		nob=0;
		status=0;
		for(i=1;i<=4;i++)
			scanf("%s",&mat[i]);
		for(i=1;i<=4;i++)
		{
			if(strcmp(mat[i],"XXXT")==0)
			{status=1;  winner=1; break;}
			if(strcmp(mat[i],"TXXX")==0)
			{status=1;  winner=1; break;}
			if(strcmp(mat[i],"OOOT")==0)
			{status=1;  winner=2; break;}
			if(strcmp(mat[i],"TOOO")==0)
			{status=1;  winner=2; break;}
			if(strcmp(mat[i],"XXXX")==0)
			{status=1;  winner=1; break;}
			if(strcmp(mat[i],"OOOO")==0)
			{status=1;  winner=2; break;}
			for(k=0;k<4;k++)
				if(mat[i][k]=='.')nob++;
		}
		while(status==0)
		{
			for(i=1;i<=4;i++)
			{
				temp[0]=mat[1][i-1];
				temp[1]=mat[2][i-1];
				temp[2]=mat[3][i-1];
				temp[3]=mat[4][i-1];
				temp[4]='\0';
				if(strcmp(temp,"XXXT")==0)
				{status=1;  winner=1; break;}
				if(strcmp(temp,"TXXX")==0)
				{status=1;  winner=1; break;}
				if(strcmp(temp,"OOOT")==0)
				{status=1;  winner=2; break;}
				if(strcmp(temp,"TOOO")==0)
				{status=1;  winner=2; break;}
				if(strcmp(temp,"XXXX")==0)
				{status=1;  winner=1; break;}	
				if(strcmp(temp,"OOOO")==0)
				{status=1;  winner=2; break;}
			}
			break;
		}
		while(status==0)
		{
				temp[0]=mat[1][0];
				temp[1]=mat[2][1];
				temp[2]=mat[3][2];
				temp[3]=mat[4][3];
				temp[4]='\0';
				if(strcmp(temp,"XXXT")==0)
				{status=1;  winner=1; break;}
				if(strcmp(temp,"TXXX")==0)
				{status=1;  winner=1; break;}
				if(strcmp(temp,"OOOT")==0)
				{status=1;  winner=2; break;}
				if(strcmp(temp,"TOOO")==0)
				{status=1;  winner=2; break;}
				if(strcmp(temp,"XXXX")==0)
				{status=1;  winner=1; break;}
				if(strcmp(temp,"OOOO")==0)
				{status=1;  winner=2; break;}
				temp[0]=mat[1][3];
				temp[1]=mat[2][2];
				temp[2]=mat[3][1];
				temp[3]=mat[4][0];
				temp[4]='\0';
				if(strcmp(temp,"XXXT")==0)
				{status=1;  winner=1; break;}
				if(strcmp(temp,"TXXX")==0)
				{status=1;  winner=1; break;}
				if(strcmp(temp,"OOOT")==0)
				{status=1;  winner=2; break;}
				if(strcmp(temp,"TOOO")==0)
				{status=1;  winner=2; break;}
				if(strcmp(temp,"XXXX")==0)
				{status=1;  winner=1; break;}
				if(strcmp(temp,"OOOO")==0)
				{status=1;  winner=2; break;}
				break;
		}

		if(status==0)
		{
			if(nob!=0)
				printf("Case #%d: Game has not completed\n",count);
			else
				printf("Case #%d: Draw\n",count);
		}
		else
		{
			if(winner==1)
				printf("Case #%d: X won\n",count);
			else
				printf("Case #%d: O won\n",count);
		}
		count++;
		t--;

	}
	return 0;
}