// code_jam_rc_a.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <fstream>
using namespace std;

int main()
{
	long long i,j,k,l,m,n,t,tt,rs;
	char c, st[70];
	long long mas[200], res[200];
	ifstream in ("A-large.in");
	ofstream out ("A-large.out");
	in>>tt;
	for(t=0;t<tt;t++)
	{
		in>>st;
		for(i=0;i<200;i++)
		{	
			mas[i]=-1;
			res[i]=0;
		}
		mas[st[0]]=1;
		res[1]=1;
		l=2;
		k=0;
		for(i=1;i<strlen(st);i++)
		{
			if(mas[st[i]]==-1)
			{
				mas[st[i]]=k;
				res[l]=k;
				if(k==0)
				{	
					k++;
				}
				k++;
			}
			else
			{
				res[l]=mas[st[i]];
			}
			l++;
		}
		n=1;
		if(k==0)
		{
			k+=2;
		}
		rs=0;
		for(i=l-1;i>0;i--)
		{
			rs+=res[i]*n;
			n*=k;
		}
		out<<"Case #"<<t+1<<": "<<rs<<"\n";
	}


	return 0;
}

