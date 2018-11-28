#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<iomanip.h>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void main()
{
	int t,flag=0,n;
	long int k;
	ifstream fi("A-large.in",ios::binary|ios::in);
	ofstream fo("outputlar.out",ios::out);
	fi>>t;
	for(int t_c=0;t_c<t;t_c++)
	{
		fi>>n>>k;
		if(((k+1)%(long int)pow(2,n))==0)
			fo<<"Case #"<<(t_c+1)<<": "<<"ON"<<endl;
		else
			fo<<"Case #"<<(t_c+1)<<": "<<"OFF"<<endl;
	}
	fi.close();
	fo.close();
	getch();
}

