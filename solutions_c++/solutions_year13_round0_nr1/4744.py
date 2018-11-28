#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int in[4][4];
bool judge(int x)
{
	//00 01 02 03
	bool yes=false;
	int i,j,k;
	if((in[0][0]==x || in[0][0]==3) && (in[0][1]==x || in[0][1]==3) && (in[0][2]==x || in[0][2]==3) && (in[0][3]==x || in[0][3]==3))
	{
		yes=true;
		for(i=0,k=0;i<1;i++)
		{
			for(j=0;j<4;j++)
			{
				if(in[i][j]==3)
				{
					k++;
				}
			}
		}
		if(k>1)yes=false;
	}
	if((in[1][0]==x || in[1][0]==3) && (in[1][1]==x || in[1][1]==3) && (in[1][2]==x || in[1][2]==3) && (in[1][3]==x || in[1][3]==3))
	{
		yes=true;
		for(i=1,k=0;i<2;i++)
		{
			for(j=0;j<4;j++)
			{
				if(in[i][j]==3)
				{
					k++;
				}
			}
		}
		if(k>1)yes=false;
	}
	if((in[2][0]==x || in[2][0]==3) && (in[2][1]==x || in[2][1]==3) && (in[2][2]==x || in[2][2]==3) && (in[2][3]==x || in[2][3]==3))
	{
		yes=true;
		for(i=2,k=0;i<3;i++)
		{
			for(j=0;j<4;j++)
			{
				if(in[i][j]==3)
				{
					k++;
				}
			}
		}
		if(k>1)yes=false;
	}
	if((in[3][0]==x || in[3][0]==3) && (in[3][1]==x || in[3][1]==3) && (in[3][2]==x || in[3][2]==3) && (in[3][3]==x || in[3][3]==3))
	{
		yes=true;
		for(i=3,k=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(in[i][j]==3)
				{
					k++;
				}
			}
		}
		if(k>1)yes=false;
	}
	
	
	if((in[0][0]==x || in[0][0]==3) && (in[1][0]==x || in[1][0]==3) && (in[2][0]==x || in[2][0]==3) && (in[3][0]==x || in[3][0]==3))
	{
		yes=true;
		for(i=0,k=0;i<4;i++)
		{
			for(j=0;j<1;j++)
			{
				if(in[i][j]==3)
				{
					k++;
				}
			}
		}
		if(k>1)yes=false;
	}
	if((in[0][1]==x || in[0][1]==3) && (in[1][1]==x || in[1][1]==3) && (in[2][1]==x || in[2][1]==3) && (in[3][1]==x || in[3][1]==3))
	{
		yes=true;
		for(i=0,k=0;i<4;i++)
		{
			for(j=1;j<2;j++)
			{
				if(in[i][j]==3)
				{
					k++;
				}
			}
		}
		if(k>1)yes=false;
	}
	if((in[0][2]==x || in[0][2]==3) && (in[1][2]==x || in[1][2]==3) && (in[2][2]==x || in[2][2]==3) && (in[3][2]==x || in[3][2]==3))
	{
		yes=true;
		for(i=0,k=0;i<4;i++)
		{
			for(j=2;j<3;j++)
			{
				if(in[i][j]==3)
				{
					k++;
				}
			}
		}
		if(k>1)yes=false;
	}
	if((in[0][3]==x || in[0][3]==3) && (in[1][3]==x || in[1][3]==3) && (in[2][3]==x || in[2][3]==3) && (in[3][3]==x || in[3][3]==3))
	{
		yes=true;
		for(i=0,k=0;i<4;i++)
		{
			for(j=3;j<4;j++)
			{
				if(in[i][j]==3)
				{
					k++;
				}
			}
		}
		if(k>1)yes=false;
	}
	
	if((in[0][0]==x || in[0][0]==3) && (in[1][1]==x || in[1][1]==3) && (in[2][2]==x || in[2][2]==3) && (in[3][3]==x || in[3][3]==3))
	{
		yes=true;
		for(i=0,j=0,k=0;i<4;i++,j++)
		{
			if(in[i][j]==3)
			{
				k++;
			}
		}
		if(k>1)yes=false;
	}
	if((in[0][3]==x || in[0][3]==3) && (in[1][2]==x || in[1][2]==3) && (in[2][1]==x || in[2][1]==3) && (in[3][0]==x || in[3][0]==3))
	{
		yes=true;
		for(i=0,j=3,k=0;i<4;i++,j--)
		{
			if(in[i][j]==3)
			{
				k++;
			}
		}
		if(k>1)yes=false;
	}
	return yes;
}
int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int n;
	fin>>n;
	int count=1;
	
	char input;
	int i,j;
	bool isempty,X,O;
	while(n--)
	{
		isempty=false;
		fout<<"Case #"<<count<<": ";
		count++;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				fin>>input;
				if(input=='X')
				{
					in[i][j]=1;
				}
				else if(input=='O')
				{
					in[i][j]=2;
				}
				else if(input=='T')
				{
					in[i][j]=3;
				}
				else
				{
					isempty=true;
					in[i][j]=0;
				}
			}
		}
		//input over
		X=judge(1);
		O=judge(2);
		if(X && !O)
		{
			fout<<"X won"<<endl;
		}
		else if(!X && O)
		{
			fout<<"O won"<<endl;
		}
		else if(X && O)
		{
			fout<<"Draw"<<endl;
		}
		else if(!X && !O && isempty)
		{
			fout<<"Game has not completed"<<endl;
		}
		else if(!X && !O && !isempty)
		{
			fout<<"Draw"<<endl;
		}
		if(n!=0)
		{
			//fin>>input;
		}
		
	}
	return 0;
}