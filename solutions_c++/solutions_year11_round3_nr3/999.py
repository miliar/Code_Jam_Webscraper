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
long int hcf(long int a,long int b)
{
	long int temp;
	while(a%b!=0)
	{
		temp=a;
		a=b;
		b=temp%b;
	}
	return b;
}
void main()
{
	
	int t,i,j,k,n,l,h,*fr,lcm,flag,freq,a,b;
	ifstream fi("C-small-attempt0.in",ios::binary|ios::in);
	ofstream fo("outputCs0.out",ios::out);
	fi>>t;
	for(int t_c=0;t_c<t;t_c++)
	{
		fi>>n>>l>>h;
		flag=0;
		fr=new int[n];
		for(i=0;i<n;i++)
			fi>>fr[i];
		for(freq=l;freq<=h;freq++)
		{
			flag=0;
			for(i=0;i<n;i++)
			{
				if(freq>fr[i])
				{
					a=freq;
					b=fr[i];
				}
				else
				{
					a=fr[i];
					b=freq;
				}
				if(a%b!=0)
				{
					flag=1;
					break;
				}
			}
			if(flag==0)
				break;
		}
		if(flag==0)
			fo<<"Case #"<<t_c+1<<": "<<freq<<endl;
		else
			fo<<"Case #"<<t_c+1<<": NO"<<endl;
		cout<<t_c+1<<endl;
		//cout<<flag<<endl;
	}
	fi.close();
	fo.close();
	getch();
}
