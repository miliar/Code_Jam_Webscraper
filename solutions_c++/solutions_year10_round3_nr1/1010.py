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
#include<string>
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
	
	int t,n,i,j,**wire,count;
	ifstream fi("A-small-attempt0.in",ios::binary|ios::in);
	ofstream fo("output.out",ios::out);
	fi>>t;
	for(int t_c=0;t_c<t;t_c++)
	{
		fi>>n;
		count=0;
		wire=new int*[n];
		for(i=0;i<n;i++)
		{
			wire[i]=new int[2];
			fi>>wire[i][0]>>wire[i][1];
		}
		for(i=0;i<n-1;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if((wire[i][0]-wire[j][0]<0&&wire[i][1]-wire[j][1]>0)||(wire[i][0]-wire[j][0]>0&&wire[i][1]-wire[j][1]<0))
					count++;
			}
		}
		fo<<"Case #"<<t_c+1<<": "<<count<<endl;
		cout<<t_c<<endl;
	}
	fi.close();
	fo.close();
	getch();
}
