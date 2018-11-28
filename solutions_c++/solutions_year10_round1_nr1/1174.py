#include <stdio.h>
#include <iostream>
#include <conio.h>
#include <fstream>
#include <math.h>
using namespace std;
void read();
void readt();
void readnk();
void readgrid();
void rotate();
void check();
unsigned long int pos=0,x=0,k=0,n=0,t=0,num;
int countrv=0,countbv=0,rvflag=0,bvflab=0,rhflag=0,bhflag=0,rd1flag=0,bd1flag=0,rd2flag=0,bd2flag=0,countd2b,countd2r,rflag,bflag;
char arr[1000000],grid[100][100];
void main()
{
	ofstream fout;
	fout.open("output.in" , ios::out);
	read();
	readt();
	for (int xx=0;xx<t;xx++)
	{
		readnk();
		readgrid();
		/*for(int yy=0;yy<n;yy++)
		{
			puts(grid[yy]);
		}*/
		rotate();
		/*for(int yy=0;yy<n;yy++)
		{
			puts(grid[yy]);
		}*/
		


		check();
		if((rflag == 1)&&(bflag ==0))
		{
			fout << "Case #" << xx + 1<<": " << "Red\n";
		}
		if((rflag == 0)&&(bflag == 1))
		{
			fout << "Case #" << xx + 1  <<": " << "Blue\n";
		}
		if((rflag == 1)&&(bflag == 1))
		{
			fout << "Case #" << xx + 1<<": " << "Both\n";
		}
		if((rflag == 0)&&(bflag == 0))
		{
			fout << "Case #" << xx + 1<<": " << "Neither\n";
		}
	}
	fout.close();

}

void read()
{
	ifstream fin;
	fin.open("input.in" , ios :: in);
	while(fin)
	{
		fin.get(arr[x]);
		x++;
	}
	fin.close();
}
void readt()
{
	while (arr[pos] != '\n')
	{
		t =  (t*10) + (arr[pos] - 48);
		pos++;
	}
}
void readnk()
{
	n=0;
	
	pos++;
	
	
	while (arr[pos] != ' ')
	{
		n =  (n*10) + (arr[pos] - 48);
		pos++;
	}
	k=0;
	pos++;
	while ((arr[pos] != '\n')&&(arr[pos] != '\0'))
	{
		k =  (k*10) + (arr[pos] - 48);
		pos++;
	}
}
void readgrid()
{
	pos++;
	int yy;
	for(int xx=0;xx<n;xx++)
	{
		for(yy=0;yy<n;yy++)
		{
			grid[xx][yy]=arr[pos];
			pos++;
		}
		grid[xx][yy] = '\0';
		pos++;
	}
	pos--;
}
void rotate()
{
	for(int xx=0 ; xx<n ; xx++)
	{
		for (int zz = 0;zz<n;zz++)
		{

		for (int yy=0;  yy<n-1  ; yy++)
		{
			if(grid[xx][yy] != '.')
			{
				if(grid[xx][yy+1] == '.')
				{
					grid[xx][yy+1] = grid[xx][yy];
					grid[xx][yy] = '.';
				}
			}
		}
		}
	}
}
void check()
{
	rflag=0;
	bflag=0;
	
	//Vertical Red

	for (int xx=0;xx<n;xx++)
	{
		int yy=0;
		countbv = 0;
		countrv =0;
		while (yy != n)
		{
			if(grid[xx][yy]=='R')
			{
				countrv++;
			}
			else 
			{
				countrv = 0;
			}
			if(grid[xx][yy]=='B')
			{
				countbv++;
			}
			else 
			{
				countbv = 0;
			}
			yy++;
			if (countrv == k)
			{
				rflag=1;
			}
			if (countbv == k)
			{
				bflag=1;
			}
		}
	}
	/*cout << "\nHorizontal Red = " << rflag;
	cout << "\nHorizontal Blue = " << bflag;
	getch();*/
	//HORIZONTAL//
	for (int yy=0;yy<n;yy++)
	{
		int xx=0;
		countrv =0;
		countbv = 0;
		while (xx != n)
		{
			if(grid[xx][yy]=='R')
			{
				countrv++;
			}
			else if(grid[xx][yy] != 'R')
			{
				countrv = 0;
			}
			if(grid[xx][yy]=='B')
			{
				countbv++;
			}
			else if(grid[xx][yy] != 'B')
			{
				countbv = 0;
			}
			xx++;
			if (countrv == k)
			{
				rflag=1;
			}
			if (countbv == k)
			{
				bflag=1;
			}
		}
	}
	/*cout << "\nVertical Red = " << rflag;
	cout << "\nVertical Blue = " << bflag;
	getch();*/
	//DIAGONAL 1
	for (int xx=0;xx<n;xx++)
	{
		for(int yy=0;yy<n;yy++)
		{
			int countd1b=0;
			int countd1r=0;
			int temp=xx;
			for(int zz = yy;zz<n;zz++)
			{
				if(grid[xx][zz] == 'B')
				{
					countd1b++;
				}
				else
				{
					countd1b = 0;
				}
				if(grid[xx][zz] == 'R')
				{
					countd1r++;
				}
				else
				{
					countd1r = 0;
				}
				if(countd1r == k)
				{
					rflag=1;
				}
				if(countd1b == k)
				{
					bflag=1;
				}
				xx++;
				if(xx==n)
				{
					goto skip;
				}
			}
skip:
			;
			xx=temp;
		}
	}
	/*cout << "\nDiagonal Red 1 = " << rflag;
	cout << "\nDiagonal Blue 1 = " << bflag;
	getch();*/
	//DIAGONAL 2
	for (int xx=n-1;xx>=0;xx--)
	{
		for(int yy=0;yy<n;yy++)
		{
			int countd2b=0;
			int countd2r=0;
			int temp=xx;
			//cout <<"\n\n\nNEW Loop \n\n";
			for(int zz = yy;zz<n;zz++)
			{
				//cout << "XX = " << xx << "   YY = " << yy << " ZZ = " << zz <<"\n";
				if(grid[xx][zz] == 'B')
				{
					countd2b++;
				}
				else
				{
					countd2b = 0;
				}
				if(grid[xx][zz] == 'R')
				{
					countd2r++;
				}
				else
				{
					countd2r = 0;
				}
				if(countd2r == k)
				{
					rflag=1;
				}
				if(countd2b == k)
				{
					bflag=1;
				}
				xx--;
				if(xx==-1)
				{
					goto skip1;
				}
			}
skip1:
			;
			xx=temp;
		}
	}
	/*cout << "\nDiagonal Red 2 = " << rflag;
	cout << "\nDiagonal Blue 2 = " << bflag;
	cout <<"\n";
	getch();*/

}