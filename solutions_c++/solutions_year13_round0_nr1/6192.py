// a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-smalllast.out","w",stdout);
	char a[4][4],b[3],winner;
	bool winner_is_present=false;
    b[0] = 'X';
    b[1] = 'O';
    b[2] = 'T';
    long T,n,i,j,k,c[100],count=0,l,m;
    cin>>n;
	for(T=0;T<n;T++)
	{
	winner_is_present=false;
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			cin>>a[i][j];

	//row wise
    for(int i=0;i<4;i++)
    {

		count = 0;
		c[0]=c[1]=c[2]=0;
    
		for(int j=0;j<4;j++)
		{
			if(a[i][j]=='.')
    
			count++;
    
			for(k=0;k<3;k++)
    
				if(b[k]==a[i][j])
				{
			//		printf("%c  \n",b[k]);
					c[k]++;
					break;
				}
		}
    
		if(c[0]==4||(c[0]==3&&c[2]==1))
		{
		//printf("Debug ::: C[0]= %d, C[1]= %d, C[2]= %d\n",c[0],c[1],c[2]);
		winner = b[0];
		//cout<<winner<<endl;
		printf("Case #%ld: %c won\n",T+1,winner);
		winner_is_present=true;
		break;
		}
		else if(c[1]==4||(c[1]==3&&c[2]==1))
		{
		//printf("Debug ::: C[0]= %d, C[1]= %d, C[2]= %d\n",c[0],c[1],c[2]);
		winner = b[1];
		//cout<<winner<<endl;
		printf("Case #%ld: %c won\n",T+1,winner);
		winner_is_present=true;
		break;
		}
	}	
	//column search
	if(!winner_is_present)
	{
	for(i=0;i<4;i++)
	{
			c[0]=c[1]=c[2]=0;
    
		for(int j=0;j<4;j++)
		{
			for(k=0;k<3;k++)
    
				if(b[k]==a[j][i])
				{
					//printf("%c  \n",b[k]);
					c[k]++;
					break;
				}
		}
    
		if(c[0]==4||(c[0]==3&&c[2]==1))
		{
		//printf("Debug ::: C[0]= %d, C[1]= %d, C[2]= %d\n",c[0],c[1],c[2]);
		winner = b[0];
		//cout<<winner<<endl;
		printf("Case #%ld: %c won\n",T+1,winner);
		winner_is_present=true;
		break;
		}
		else if(c[1]==4||(c[1]==3&&c[2]==1))
		{
		//printf("Debug ::: C[0]= %d, C[1]= %d, C[2]= %d\n",c[0],c[1],c[2]);
		winner = b[1];
		//cout<<winner<<endl;
		printf("Case #%ld: %c won\n",T+1,winner);
		winner_is_present=true;
		break;
		}	
	}
	}
	//diagonal search
		//c[0]= c[1]= c[2]= 0;
	if(!winner_is_present)
	{
		if((a[3][0]==b[1] || a[3][0]==b[0]) && !winner_is_present)
		{
			char t=a[3][0];
			if((a[2][1]==t || a[2][1]=='T') && (a[1][2]==t || a[1][2]=='T') && (a[0][3]==t || a[0][3]=='T'))
			{
				//printf("%c\n",a[3][0]);
				winner = a[3][0];
				printf("Case #%ld: %c won\n",T+1,winner);
				winner_is_present=true;
				//break;
			}
		}
		if((a[0][0]==b[1] || a[0][0]==b[0]) && !winner_is_present)
		{
			char t=a[0][0];
			if((a[1][1]==t || a[1][1]=='T') && (a[2][2]==t || a[2][2]=='T') && (a[3][3]==t || a[3][3]=='T'))
			{
				//printf("%c\n",a[0][0]);
				winner = a[0][0];
				printf("Case #%ld: %c won\n",T+1,winner);
				winner_is_present=true;
				//break;
			}
		}
		if((a[0][3]==b[1] || a[0][3]==b[0]) && !winner_is_present)
		{
			char t=a[0][3];
			if((a[1][2]==t || a[1][2]=='T') && (a[2][1]==t || a[2][1]=='T') && (a[3][0]==t || a[3][0]=='T'))
			{
				winner = a[0][3];
				//printf("%c\n",a[0][3]);
				printf("Case #%ld: %c won\n",T+1,winner);
				winner_is_present=true;
				//break;
			}

		}
		if((a[3][3]==b[1] || a[3][3]==b[0]) && !winner_is_present)
		{
			char t=a[3][3];
			if((a[2][2]==t || a[2][2]=='T') && (a[1][1]==t || a[1][1]=='T') && (a[0][0]==t || a[0][0]=='T'))
			{
				winner = a[3][3];
				printf("Case #%ld: %c won\n",T+1,winner);
				//printf("%c\n",a[3][3]);
				winner_is_present=true;
				//break;
			}
		}
		//printf("Count : %ld\n",count);
		//Diagonal search ends
	}
	if(winner_is_present==false)
	{
		if(count>0)
			printf("Case #%ld: Game has not completed\n",T+1);
		else printf("Case #%ld: Draw\n",T+1);
	}
	
}
	return 0;
}

