#include <iostream>
#include <cstring>
#include <string.h>
#include <cstdio>
using namespace std;
string grid[4];
int checkR(int x,int y)
{
		int c = 0;
		for(int i = y;i < 4;i++)
			{					
				if(i >= 0 && i < 4 && grid[x][i] == grid[x][y] || grid[x][i] == 'T')
					c++;
				else
					return c;
			}
		return c;
}
int checkL(int x,int y)
{
		int c = 0;
		for(int i = y;i >= 0;i--)
			{
				if(i >= 0 && i < 4 &&grid[x][i] == grid[x][y] || grid[x][i] == 'T')
					c++;
				else
					return c;
			}
		return c;
}
int checkD(int x,int y)
{
		int c = 0;
		for(int i = x;i < 4;i++)
			{
				if(i >= 0 && i < 4 &&grid[i][y] == grid[x][y] || grid[i][y] == 'T')
					c++;
				else
					return c;
			}
		return c;
}
int checkU(int x,int y)
{
		int c = 0;
		for(int i = x;i >= 0;i--)
			{
				if(i >= 0 && i < 4 && grid[i][y] == grid[x][y] || grid[i][y] == 'T')
					c++;
				else
					return c;
			}
		return c;
}

int diagonalUL(int x,int y)
{
   int c=1;

    if(x-1 >=0 && y-1 >=0)
    if(grid[x-1][y-1] == grid[x][y]|| grid[x-1][y-1]=='T' )c++;
    if(x-2 >=0 && y-2 >=0)
    if(grid[x-2][y-2] == grid[x][y]|| grid[x-2][y-2]=='T' )c++;
    if(x-3 >=0 && y-3 >=0)
    if(grid[x-3][y-3] == grid[x][y]|| grid[x-3][y-3]=='T' )c++;

    return c;
}

int diagonalUR(int x,int y)
{   int c=1;

    if(x-1 >=0 && y+1 <4)
    if(grid[x-1][y+1] == grid[x][y]|| grid[x-1][y+1]=='T' )c++;
    if(x-2 >=0 && y+2 <4 )
    if(grid[x-2][y+2] == grid[x][y]|| grid[x-2][y+2]=='T' )c++;
    if(x-3 >=0 && y+3 <4)
    if(grid[x-3][y+3] == grid[x][y]|| grid[x-3][y+3]=='T' )c++;

    return c;

}

int diagonalDL(int x,int y)
{
   int c=1;

    if(x+1 <4 && y-1 >=0)
    if(grid[x+1][y-1] == grid[x][y]|| grid[x+1][y-1]=='T' )c++;
    if(x+2 <4 && y-2 >=0)
    if(grid[x+2][y-2] == grid[x][y]|| grid[x+2][y-2]=='T' )c++;
    if(x+3 <4&&  y-3 >=0)
    if(grid[x+3][y-3] == grid[x][y]|| grid[x+3][y-3]=='T' )c++;

    return c;
}

int diagonalDR(int x,int y)
{
    int c=1;

    if(x+1 <4 && y+1 <4)
    if( grid[x+1][y+1] == grid[x][y]|| grid[x+1][y+1]=='T' )c++;
    if(x+2 <4 && y+2 <4)
    if( grid[x+2][y+2] == grid[x][y]|| grid[x+2][y+2]=='T' )c++;
    if(x+3 <4 && y+3 <4)
    if(grid[x+3][y+3] == grid[x][y]|| grid[x+3][y+3]=='T' )c++;


    return c;
}
bool checkEmpty()
{
	for(int i = 0;i < 4;i++)
		for(int j = 0;j < 4;j++)
			if(grid[i][j] == '.')
				return true;
	return false;
}
int main()
{
int t;
cin>>t;
//getchar();
int total = 0;
while(t--)
{
	//for(int i = 0 ;i < 4;i++)
		//gets(grid[i]);

    for(int i=0;i<4;i++)
    {
       // string s;
        cin>>grid[i];
    }
	char ch = getc(stdin);
	int val_x = 0,val_o = 0;
	bool isempty;
	for(int i = 0 ;i < 4;i++)
		for(int j = 0;j < 4;j++)
		{
			if(grid[i][j] == 'X')
			{
			       	int temp = checkL(i,j);
				if(temp > val_x)
					val_x = temp;

			       	temp = checkR(i,j);
				if(temp > val_x)
					val_x = temp;

			       	temp = checkD(i,j);
				if(temp > val_x)
					val_x = temp;

			       	temp = checkU(i,j);
				if(temp > val_x)
					val_x = temp;

				temp = diagonalUL(i,j);
				if(temp > val_x)
					val_x = temp;

				temp = diagonalUR(i,j);
				if(temp > val_x)
					val_x = temp;

				temp = diagonalDL(i,j);
				if(temp > val_x)
					val_x = temp;

				temp = diagonalDR(i,j);
				if(temp > val_x)
					val_x = temp;
			}

			if(grid[i][j] == 'O')
			{
			       	int temp = checkL(i,j);
				if(temp > val_o)
					val_o = temp;

			       	temp = checkR(i,j);
				if(temp > val_o)
					val_o = temp;

			       	temp = checkD(i,j);
				if(temp > val_o)
					val_o = temp;

			       	temp = checkU(i,j);
				if(temp > val_o)
					val_o = temp;
				temp = diagonalUL(i,j);
				if(temp > val_o)
					val_o = temp;

				temp = diagonalUR(i,j);
				if(temp > val_o)
					val_o = temp;

				temp = diagonalDL(i,j);
				if(temp > val_o)
					val_o = temp;

				temp = diagonalDR(i,j);
				if(temp > val_o)
					val_o = temp;
			}			
		}
	isempty = checkEmpty();
	total++;
	//cout<<val_x<<" "<<val_o<<endl;
	if(val_x == 4  && val_o < 4)
		cout<<"Case #"<<total<<": X won"<<endl;
	else
	if(val_x < 4  && val_o == 4)
		cout<<"Case #"<<total<<": O won"<<endl;
	else
	if(val_x < 4  && val_o < 4 && isempty == false)
		cout<<"Case #"<<total<<": Draw"<<endl;
	else
		cout<<"Case #"<<total<<": Game has not completed"<<endl;

}
return 0;
}
