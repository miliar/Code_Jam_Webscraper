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
	
	int t,n,m,i;
	char *color;
	int *button;
	int time,moveO,moveB,curO,curB;
	ifstream fi("A-large.in",ios::binary|ios::in);
	ofstream fo("outputAl.out",ios::out);
	fi>>t;
	//cin>>t;
	for(int t_c=0;t_c<t;t_c++)
	{
		fi>>n;
		//cin>>n;
		color=new char[n];
		button=new int[n];
		for(i=0;i<n;i++)
			cin>>color[i]>>button[i];
		moveO=moveB=time=0;
		curO=curB=1;
		for(i=0;i<n;i++)
		{
			if(color[i]=='O')
			{
				moveO+=abs(button[i]-curO)+1;
				if(moveO>=moveB)
				{
					time+=abs(button[i]-curO)+1-moveB;
					moveB=0;
				}
				else
				{
					moveB-=moveO;
					time++;
				}
				curO=button[i];
			}
			else if(color[i]=='B')
			{
				moveB+=abs(button[i]-curB)+1;
				if(moveB>=moveO)
				{
					time+=abs(button[i]-curB)+1-moveO;
					moveO=0;
				}
				else
				{
					moveO-=moveB;
					time++;
				}
				curB=button[i];
			}
		}
		fo<<"Case #"<<t_c+1<<": "<<time<<endl;
		cout<<"Case #"<<t_c+1<<": "<<time<<endl;
	}
	fi.close();
	fo.close();
	getch();
}
