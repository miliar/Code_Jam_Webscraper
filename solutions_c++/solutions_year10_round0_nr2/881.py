#include <iostream.h>
#include <fstream.h>
#include <conio.h>
#include <stdio.h>
#include <math.h>
int gcd(long a, long b)
{
	long temp;
	while(b!=0)
	{
		temp=a;
		a=b;
		b=temp%b;
	}
	return a;
}
void main()
{
	int T;
	int N;
	long a,b,c,out,max;
	long bc,sum,temp,temp1,temp2,temp3;
	char* infile="B-small-attempt3.in";
	char* outfile="B-small-attempt3.out";
	fstream fin;
	fstream	fout;
	fin.open(infile, ios::in);
	fout.open(outfile,ios::out);
	fin>>T;
	for(int i=1;i<=T;i++)
	{
		fin>>N;
		if(N==2)
		{
			fin>>a;
			fin>>b;
			
				temp=abs(a-b);
				max=a>=b?a:b;
				if(temp==1) out = 0;
				else
				{
					int i=1;
					long tempout=temp;
					while(tempout<max)
					{
						i++;
						tempout=temp*i;		
					}
					out=tempout-max;
				}
				
		}
		else
		{
			fin>>a;
			fin>>b;
			fin>>c;
			temp1=abs(a-b);
			temp2=abs(b-c);
			temp3=abs(a-c);
			temp=gcd(gcd(temp1,temp2),temp3);
			max=((a>=b)&&(a>=c))?a:((b>=a)&&(b>=c))?b:c;
			if(temp==1) out=0;
			else
			{
				int i=1;
				long tempout=temp;
				while(tempout<max)
				{
					i++;
					tempout=temp*i;
				}	
				out=tempout-max;
			}		
		}
		fout<<"Case #"<<i<<": "<<out;
		
		if(i<T) fout<<"\n";
	}
	
	fin.close();
	fout.close();

	
     
}

