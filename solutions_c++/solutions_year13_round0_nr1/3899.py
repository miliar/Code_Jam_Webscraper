#include<iostream>
#include<string.h>

using namespace std;

int main()
{
	int run=1,status=-1,t,i,j,ans[1001];
	char tictac[4][4],string[20];

	cin>>t;
	while(run<=t)
	{
		status=-1;	
		for(i=0;i<4;i++)	
			cin>>tictac[i];

		if(status==-1)
		{
			for(i=0;i<4;i++)
			{
				if( (tictac[i][0]=='X' or tictac[i][0]=='T') and 
					(tictac[i][1]=='X' or tictac[i][1]=='T') and 
					(tictac[i][2]=='X' or tictac[i][2]=='T') and 
					(tictac[i][3]=='X' or tictac[i][3]=='T') )
				{
					status = 1;
					break;
				}	
				else if( (tictac[0][i]=='X' or tictac[0][i]=='T') and 
					(tictac[1][i]=='X' or tictac[1][i]=='T') and 
					(tictac[2][i]=='X' or tictac[2][i]=='T') and 
					(tictac[3][i]=='X' or tictac[3][i]=='T') )
				{
					status=1;
					break;
				}
			}
		}
		if(status==-1)
		 	{
		 		if( (tictac[0][0]=='X' or tictac[0][0]=='T') and 
					(tictac[1][1]=='X' or tictac[1][1]=='T') and 
					(tictac[2][2]=='X' or tictac[2][2]=='T') and 
					(tictac[3][3]=='X' or tictac[3][3]=='T') )
						status=1;
				if( (tictac[0][3]=='X' or tictac[0][3]=='T') and 
					(tictac[1][2]=='X' or tictac[1][2]=='T') and 
					(tictac[2][1]=='X' or tictac[2][1]=='T') and 
					(tictac[3][0]=='X' or tictac[3][0]=='T') )
						status=1;
			}

		if(status==-1)
		{
			for(i=0;i<4;i++)
			{
				if( (tictac[i][0]=='O' or tictac[i][0]=='T') and 
					(tictac[i][1]=='O' or tictac[i][1]=='T') and 
					(tictac[i][2]=='O' or tictac[i][2]=='T') and 
					(tictac[i][3]=='O' or tictac[i][3]=='T') )
				{
					status = 2;
					break;
				}	
				else if( (tictac[0][i]=='O' or tictac[0][i]=='T') and 
						(tictac[1][i]=='O' or tictac[1][i]=='T') and 
						(tictac[2][i]=='O' or tictac[2][i]=='T') and 
						(tictac[3][i]=='O' or tictac[3][i]=='T') )
				{
					status=2;
					break;
				}
			}
		}
		if(status==-1)
			{
				if( (tictac[0][0]=='O' or tictac[0][0]=='T') and 
					(tictac[1][1]=='O' or tictac[1][1]=='T') and 
					(tictac[2][2]=='O' or tictac[2][2]=='T') and 
					(tictac[3][3]=='O' or tictac[3][3]=='T') )
						status=2;
				if( (tictac[0][3]=='O' or tictac[0][3]=='T') and 
					(tictac[1][2]=='O' or tictac[1][2]=='T') and 
					(tictac[2][1]=='O' or tictac[2][1]=='T') and 
					(tictac[3][0]=='O' or tictac[3][0]=='T') )
						status=2;
			}
		if(status==-1)
		{
			for(i=0;i<4;i++)
				for(j=0;j<4;j++)
					if(tictac[i][j]=='.')
					{
						status=3;
						break;
					}
		}

		if(status==-1)
			status=4;

		ans[run]=status;
		run++;
		
	}

	for(i=1;i<t+1;i++)
	{
		status=ans[i];	
		if(status==1)
			strcpy(string,"X won");
		else if(status==2)
			strcpy(string,"O won");
		else if(status==3)
			strcpy(string,"Game has not completed");
		else if(status==4)
			strcpy(string,"Draw");


		cout<<"Case #"<<i<<": "<<string<<'\n';
	}
}