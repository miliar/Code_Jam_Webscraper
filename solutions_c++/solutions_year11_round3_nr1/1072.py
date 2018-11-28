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
#include<bigint.h>
#include<bigint.cpp>
#define bigint CBigInt
#define max(a,b) a>b?a:b
//#include"ritwik.h"
using namespace std;		
void main()
{
	
	int t,i,j,k,r,c,btiles,flag;
	char **pic;
	ifstream fi("A-large.in",ios::binary|ios::in);
	ofstream fo("outputAl.out",ios::out);
	fi>>t;
	for(int t_c=0;t_c<t;t_c++)
	{
		fi>>r>>c;
		fo<<"Case #"<<t_c+1<<": "<<endl;
		pic=new char*[r];
		btiles=flag=0;
		for(i=0;i<r;i++)
		{
			pic[i]=new char[c];
			for(j=0;j<c;j++)
			{
				fi>>pic[i][j];
				if(pic[i][j]=='#')
					btiles++;
			}
		}
		if(btiles==0)
		{
			for(i=0;i<r;i++)
			{
				for(j=0;j<c;j++)
				{
					fo<<pic[i][j];
				}
				fo<<endl;
			}
		}
		else if(btiles%4!=0)
			fo<<"Impossible"<<endl;
		else
		{
			for(i=0;i<r;i++)
			{
				for(j=0;j<c;j++)
				{
					if(pic[i][j]=='#')
					{
						if(pic[i][j+1]=='#'&&pic[i+1][j]=='#'&&pic[i+1][j+1]=='#')
						{
							pic[i][j]=pic[i+1][j+1]='/';
							pic[i+1][j]=pic[i][j+1]='\\';
						}
						else
						{
							flag=1;
							fo<<"Impossible"<<endl;
							//cout<<"imp"<<endl;
							break;
						}
					}
				}
				if(flag==1)	break;
			}
			if(flag==0)
			{
				for(i=0;i<r;i++)
				{
					for(j=0;j<c;j++)
					{
						fo<<pic[i][j];
						cout<<pic[i][j];
					}
					fo<<endl;
					cout<<endl;
				}
			}
		}
		cout<<t_c+1<<endl;
		//cout<<flag<<endl;
	}
	fi.close();
	fo.close();
	getch();
}
