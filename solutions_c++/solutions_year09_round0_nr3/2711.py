#include<iostream>
#include <fstream>
#include <iomanip>
using namespace std;

main()
{
	ofstream myfile ("output.txt");
	char s[520], p[3];
	char o[20]="welcome to code jam",u;
	int N, l, j, i, a[130][4], e,r,n=0, t, width=4;
	unsigned long fl[20];
	for(i=0;i<130;i++)
	{
		a[i][0]=0;
	}
	
	for(i=0;i<19;i++)
	{
		u=o[i];

		l=u;
		N=a[l][0];
		a[l][N+1]=i;
		a[l][0]++;
	}
	int c=1;
	gets(p);
	l=strlen(p);
	for(i=l-1;i>=0;i--)
	{
		N=p[i]-48;
		n=n+N*c;
		c=c*10;
	}
	t=1;
	while(n>0)
	{
	
		for(i=0;i<20;i++)
		{
			fl[i]=0;
		}
		gets(s);
		l=strlen(s);
		for(i=0;i<l;i++)
		{
			u=s[i];
			e=u;
			if(a[e][0]>0)
			{
				if(s[i]=='w')
				{
					fl[0]++;
				}
				else
				{
					for(j=1;j<=a[e][0];j++)
					{
						r=a[e][j];
						if(fl[r]==0)
						{
							fl[r]=fl[r-1];
						}
						else
						{
							fl[r]=fl[r]+fl[r-1];
						}
					}
				}
				
			}
		
		}

		
		myfile << "Case #"<<t<<": "<<setw(width)<< setfill('0')<<fl[18]%10000<<"\n";
	
		//cout<<"Case #"<<t<<": "<<setw(width)<< setfill('0')<<fl[18]%10000<<endl; 
		
		t++;
	
		n--;
	}
	
	return 0;
}

		




