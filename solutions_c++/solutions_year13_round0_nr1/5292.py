#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{
	int t;
	//scanf("%d",&t);
	int k;
	ifstream fil;
	fil.open("input.in");
	fil>>t;
	ofstream file;
	file.open("output.txt");
	for(k=1;k<=t;k++)
	{
		char board[4][4];
		int a=0,b=0,c=0;
		int i,j;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				//cin>>board[i][j];
				fil>>board[i][j];
			}
		}
	/*	for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				//cin>>board[i][j];
				cout<<board[i][j]<<" ";
			}
			cout<<"\n";
		}
		getchar();*/
		for(i=0;i<4;i++)
		{
			int cta=0,ctb=0,cha=0,chb=0;
			for(j=0;j<4;j++)
			{
				if(board[i][j]=='X' || board[i][j]=='T')
				{
				   cta++;
				   //cha=1;
				}
				if(board[i][j]=='O' || board[i][j]=='T')
				{
				   ctb++;
				   //chb=1;
				}
				if(board[i][j]=='.')
				c=1;
			}
			if(cta==4)
			a=1;
			else if(ctb==4)
			b=1;		
		}
		for(j=0;j<4;j++)
		{
			int cta=0,ctb=0,cha=0,chb=0;
			for(i=0;i<4;i++)
			{
				if(board[i][j]=='X' || board[i][j]=='T')
				{
				   cta++;
				   //cha=1;
				}
				if(board[i][j]=='O' || board[i][j]=='T')
				{
				   ctb++;
				   //chb=1;
				}
				if(board[i][j]=='.')
				c=1;
			}
			if(cta==4)
			a=1;
			else if(ctb==4)
			b=1;		
		}
		int cta=0,ctb=0,cha=0,chb=0;
		for(i=0;i<4;i++)
		{		
			if(board[i][i]=='X' || board[i][i]=='T')
			{
			   cta++;
			   //cha=1;
			}
			if(board[i][i]=='O' || board[i][i]=='T')
			{
			   ctb++;
			   //chb=1;
			}
		}
		
		if(cta==4)
		a=1;
		else if(ctb==4)
		b=1;
		
		cta=0,ctb=0,cha=0,chb=0;
		for(i=0;i<4;i++)
		{		
			if(board[i][3-i]=='X' || board[i][3-i]=='T')
			{
			   cta++;
			   //cha=1;
			}
			if(board[i][3-i]=='O' || board[i][3-i]=='T')
			{
			   ctb++;
			   //chb=1;
			}
		}
		
		if(cta==4)
		a=1;
		else if(ctb==4)
		b=1;
		
		if((a==1 && b==1)||(a==0 && b==0))
		{
			if(c==1)
			//printf("Case #%d: Game has not completed",k);
			file<<"Case #"<<k<<": Game has not completed\n";
			else
			//printf("Case #%d: Draw",k);
			file<<"Case #"<<k<<": Draw\n";
		}
		/*else if((a==1 && b==1)||(a==0 && b==0))
		{
			printf("Case #%d: Draw",k);
		}*/
		else if(a==1 && b==0)
		{
			//printf("Case #%d: X won",k);
			file<<"Case #"<<k<<": X won\n";
		}
		else if(a==0 && b==1)
		{
			//printf("Case #%d: O won",k);
			file<<"Case #"<<k<<": O won\n";
		}	 
	}
	return 0;
}
