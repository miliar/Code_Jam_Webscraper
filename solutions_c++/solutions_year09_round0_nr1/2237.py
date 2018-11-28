// code_jam_a.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <fstream>
#include <string>
using namespace std;

int main()
{
	long i,j,k,l,m,n,d,o;
	ifstream in ("A-large.in");
	ofstream out ("A-large.out");

	in>>l>>d>>n;
	bool p[27][17], fl[16];
	char mas[5005][17];
	for(i=0;i<d;i++)
	{
		in>>mas[i];
	}
	char c;
	long t, res;

	for(o=0;o<n;o++)
	{
		for(i=0;i<27;i++)
		{
			for(j=0;j<15;j++)
			{
				p[i][j]=false;
			}
		}
		for(i=0;i<=15;i++)
		{
			fl[i]=0;
		}

		res=d;
		t=0;
		while(t<l)
		{
			in>>c;
			if(c=='(')
			{
				in>>c;
				while(c!=')')
				{
					p[c-'a'][t]=true;
					in>>c;
				}
				t++;
			}
			else
			{
				p[c-'a'][t]=true;
				t++;
			}
		}	

		for(i=0;i<d;i++)
		{
			for(j=0;j<l;j++)
			{
				if(p[mas[i][j]-'a'][j]==false)
				{
					res--;
					break;
				}
			}
		}

		out<<"Case #"<<o+1<<": "<<res<<"\n";


	}
	




	return 0;
}

