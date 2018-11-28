#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	int test;
	cin>>test;
	int p=1;
	
	while(test--)
	{
		int a[4][4];
		char c[4][5];
		int t1,t2;
		int NoofWhite=0;
		for(int i=0;i<4;i++)
		{
			cin>>c[i];
			for(int j=0;j<strlen(c[i]);j++)
			{
				if(c[i][j]=='X')
				{
					a[i][j]=1;
				}
				else if(c[i][j]=='O')
				{
					a[i][j]=0;
				}
				else if(c[i][j]=='.')
				{
					a[i][j]=-1;	
					NoofWhite++;
				}
				else if(c[i][j]=='T')
				{
					a[i][j]=1;//considering T as X
					t1=i;
					t2=j;
				}
			}
		}	
		int ans=-2;//No winner uptill
		//cout<<c[2][0]<<c[2][1]<<c[2][2]<<c[2][3];
		if(a[0][0]==1&&a[0][1]==1&&a[0][2]==1&&a[0][3]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[0][0]==0&&a[0][1]==0&&a[0][2]==0&&a[0][3]==0)
		{
			//O wins.
			ans=0;//O is winner
			
		}
		if(a[0][0]==1&&a[1][1]==1&&a[2][2]==1&&a[3][3]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[0][0]==0&&a[1][1]==0&&a[2][2]==0&&a[3][3]==0)
		{
			ans=0;//O is winner
			
		}
		if(a[0][0]==1&&a[1][0]==1&&a[2][0]==1&&a[3][0]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[0][0]==0&&a[1][0]==0&&a[2][0]==0&&a[3][0]==0)
		{
			ans=0;//O is winner
			
		}
		if(a[0][1]==1&&a[1][1]==1&&a[2][1]==1&&a[3][1]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[0][1]==0&&a[1][1]==0&&a[2][1]==0&&a[3][1]==0)
		{
			ans=0;//O is winner
			
		}
		//3rd col
		if(a[0][2]==1&&a[1][2]==1&&a[2][2]==1&&a[3][2]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[0][2]==0&&a[1][2]==0&&a[2][2]==0&&a[3][2]==0)
		{
			ans=0;//O is winner
			
		}
		//4 th colums
		if(a[0][3]==1&&a[1][3]==1&&a[2][3]==1&&a[3][3]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[0][3]==0&&a[1][3]==0&&a[2][3]==0&&a[3][3]==0)
		{
			//O wins.
			ans=0;
		}
		//second diagonal
		if(a[0][3]==1&&a[1][2]==1&&a[2][1]==1&&a[3][0]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[0][3]==0&&a[1][2]==0&&a[2][1]==0&&a[3][0]==0)
		{
			//O wins.
			ans=0;
		}
		//2nd row
		if(a[1][0]==1&&a[1][1]==1&&a[1][2]==1&&a[1][3]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[1][0]==0&&a[1][1]==0&&a[1][2]==0&&a[1][3]==0)
		{
			//O wins.
			ans=0;
		}
		//3rd row
		if(a[2][0]==1&&a[2][1]==1&&a[2][2]==1&&a[2][3]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[2][0]==0&&a[2][1]==0&&a[2][2]==0&&a[2][3]==0)
		{
			ans=0;//O is winner
			
		}
		//4th row
		if(a[3][0]==1&&a[3][1]==1&&a[3][2]==1&&a[3][3]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[3][0]==0&&a[3][1]==0&&a[3][2]==0&&a[3][3]==0)
		{
			ans=0;//O is winner
		}		
		a[t1][t2]=0;
		//assuming now T os O
		//-------------------
		//-------------------
		if(a[0][0]==1&&a[0][1]==1&&a[0][2]==1&&a[0][3]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[0][0]==0&&a[0][1]==0&&a[0][2]==0&&a[0][3]==0)
		{
			//O wins.
			ans=0;//O is winner
			
		}
		if(a[0][0]==1&&a[1][1]==1&&a[2][2]==1&&a[3][3]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[0][0]==0&&a[1][1]==0&&a[2][2]==0&&a[3][3]==0)
		{
			ans=0;//O is winner
			
		}
		if(a[0][0]==1&&a[1][0]==1&&a[2][0]==1&&a[3][0]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[0][0]==0&&a[1][0]==0&&a[2][0]==0&&a[3][0]==0)
		{
			ans=0;//O is winner
			
		}
		if(a[0][1]==1&&a[1][1]==1&&a[2][1]==1&&a[3][1]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[0][1]==0&&a[1][1]==0&&a[2][1]==0&&a[3][1]==0)
		{
			ans=0;//O is winner
			
		}
		//3rd col
		if(a[0][2]==1&&a[1][2]==1&&a[2][2]==1&&a[3][2]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[0][2]==0&&a[1][2]==0&&a[2][2]==0&&a[3][2]==0)
		{
			ans=0;//O is winner
			
		}
		//4 th colums
		if(a[0][3]==1&&a[1][3]==1&&a[2][3]==1&&a[3][3]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[0][3]==0&&a[1][3]==0&&a[2][3]==0&&a[3][3]==0)
		{
			//O wins.
			ans=0;
		}
		//second diagonal
		if(a[0][3]==1&&a[1][2]==1&&a[2][1]==1&&a[3][0]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[0][3]==0&&a[1][2]==0&&a[2][1]==0&&a[3][0]==0)
		{
			//O wins.
			ans=0;
		}
		//2nd row
		if(a[1][0]==1&&a[1][1]==1&&a[1][2]==1&&a[1][3]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[1][0]==0&&a[1][1]==0&&a[1][2]==0&&a[1][3]==0)
		{
			//O wins.
			ans=0;
		}
		//3rd row
		if(a[2][0]==1&&a[2][1]==1&&a[2][2]==1&&a[2][3]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[2][0]==0&&a[2][1]==0&&a[2][2]==0&&a[2][3]==0)
		{
			ans=0;//O is winner
			
		}
		//4th row
		if(a[3][0]==1&&a[3][1]==1&&a[3][2]==1&&a[3][3]==1)
		{
			ans=1;//x is winner
			
		}
		if(a[3][0]==0&&a[3][1]==0&&a[3][2]==0&&a[3][3]==0)
		{
			ans=0;//O is winner
		}		
		
		if(ans==-2)
		{
			if(NoofWhite==0)
			{
				//draw
				cout<<"Case #"<<p++<<": "<<"Draw"<<endl;
			}
			else
			{
				//Game has not completed
				cout<<"Case #"<<p++<<": "<<"Game has not completed"<<endl;
			}
		}
		else if(ans==1)
		{
			//x is winner
			cout<<"Case #"<<p++<<": "<<"X won"<<endl;
		}
		else if(ans==0)
		{
			//O is winner
			cout<<"Case #"<<p++<<": "<<"O won"<<endl;
		}
		
	}
	
	return 0;
	
}
