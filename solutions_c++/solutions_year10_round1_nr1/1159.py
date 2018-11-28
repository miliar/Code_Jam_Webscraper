#include<iostream>
#include<fstream>
#include<conio.h>
#include<inttypes.h>
#include<iomanip>
#include<assert.h>
#include<ctype.h>
#include<errno.h>
#include<float.h>
#include<limits.h>
#include<locale.h>
#include<math.h>
#include<string.h>
#include<stdarg.h>
#include<stddef.h>
#include<stdint.h>
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<wchar.h>
#include<wctype.h>
//#include<bigint.h>
//#include<bigint.cpp>
#define bigint CBigInt
//#include"ritwik.h"
using namespace std;
void main()
{
	
	int t,n,k,i,j,c,b,r,count,x,flag;
	char **board,ch;
	ifstream fi("A-small-attempt-0.in",ios::binary|ios::in);
	ofstream fo("outputAs.out",ios::out);
	fi>>t;
	for(int t_c=0;t_c<t;t_c++)
	{
		fi>>n>>k;
		board=new char*[n];
		for(i=0;i<n;i++)
			board[i]=new char[n];
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				fi>>board[i][j];
		for(i=0;i<n;i++)
		{
			count=0;
			for(j=0;j<n;j++)
				if(board[i][j]=='.')
					count++;
			//cout<<count<<" ";
			if(count<n)
			{
				x=0;
				while(x<n)
				{
					for(j=n-1;j>0;j--)
					{
						if(board[i][j]=='.')
						{
							for(c=j;c>0;c--)
								board[i][c]=board[i][c-1];
							board[i][0]='.';
						}
						//cout<<board[i][j]<<" "<<j<<" "<<endl;
					}
					x++;
				}
				cout<<endl;
			}
		}
		b=r=0;
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				ch=board[i][j];
				if(ch=='R')
				{
					//cout<<i<<" "<<j<<endl;
					if(i+k-1<n)
					{	
						flag=0;
						for(x=0;x<k;x++)
							if(!(board[i+x][j]==ch))
							{
								flag=1;
								break;
							}
						if(flag==0)
						{
							r++;
							//cout<<i<<j<<"1"<<endl;
						}
					}
					if(j+k-1<n)
					{
						flag=0;
						for(x=0;x<k;x++)
							if(!(board[i][j+x]==ch))
							{
								flag=1;
								break;
							}
						if(flag==0)
						{
							r++;
							//cout<<i<<j<<"2"<<endl;
						}
					}
					if(i+k-1<n&&j+k-1<n)
					{
						flag=0;
						for(x=0;x<k;x++)
							if(!(board[i+x][j+x]==ch))
							{
								flag=1;
								break;
							}
						if(flag==0)
						{
							r++;
							//cout<<i<<j<<"3"<<endl;
						}
					}
					if((i+k-1<n)&&(j-k+1>=0))
					{
						flag=0;
						//cout<<"fffffffffffff";
						for(x=0;x<k;x++)
							if(!(board[i+x][j-x]==ch))
							{
								flag=1;
								break;
							}
						if(flag==0)
						{
							r++;
							//cout<<i<<j<<"4"<<endl;
						}
					}
				}
				else if(ch=='B')
				{
					if(i+k-1<n)
					{	
						flag=0;
						for(x=0;x<k;x++)
							if(!(board[i+x][j]==ch))
							{
								flag=1;
								break;
							}
						if(flag==0)
						{
							b++;
							
						}
					}
					if(j+k-1<n)
					{
						flag=0;
						for(x=0;x<k;x++)
							if(!(board[i][j+x]==ch))
							{
								flag=1;
								break;
							}
						if(flag==0)
						{
							b++;
							
						}
					}
					if(i+k-1<n&&j+k-1<n)
					{
						flag=0;
						for(x=0;x<k;x++)
							if(!(board[i+x][j+x]==ch))
							{
								flag=1;
								break;
							}
						if(flag==0)
						{
							b++;
							
						}
					}
					if(i+k-1<n&&j-k+1>=0)
					{
						flag=0;
						for(x=0;x<k;x++)
							if(!(board[i+x][j-x]==ch))
							{
								flag=1;
								break;
							}
						if(flag==0)
						{
							b++;
							
						}
					}
				}
			}
		}
		/*for(i=0;i<n;i++)
		{	for(j=0;j<n;j++)
				cout<<board[i][j]<<" ";
			cout<<endl;
		}*/
		if(r>0&&b>0)
		{
			fo<<"Case #"<<t_c+1<<": "<<"Both"<<endl;
		}
		else if(r>0&&b==0)
		{
			fo<<"Case #"<<t_c+1<<": "<<"Red"<<endl;
		}
		else if(b>0&&r==0)
		{
			fo<<"Case #"<<t_c+1<<": "<<"Blue"<<endl;
		}
		else if(r==0&&b==0)
		{
			fo<<"Case #"<<t_c+1<<": "<<"Neither"<<endl;
		}
		cout<<t_c<<endl;
	}
	fi.close();
	fo.close();
	getch();
}
