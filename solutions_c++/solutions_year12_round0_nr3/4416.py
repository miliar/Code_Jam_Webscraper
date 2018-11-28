#include<iostream>
#include<conio.h>
#include<fstream>
using namespace std;
int fun(int a,int b)
{
	
	int n,r=0,d=0,ct=0,t=0,res=0;
	
	for(int i=a;i<=b;i++)
	{
		for(int j=i+1;j<=b;j++)
		{
			
			n=i;
			d=0;
			while(n!=0)
			{
				n/=10;
				d++;
			}
			//cout<<i<<"  "<<j<<"  "<<d<<endl;
			n=i;
			r=0,ct=0,t=0;
			while(n!=0)
			{
				r+=pow(10.0,ct)*(n%10);
				ct++;
				n/=10;
				t=n+r*pow(10.0,d-ct);
				if(t==j)
				{
					res++;
				}
			}
			
		}
	}
	return res;
}

void main()
{
	int T,A,B;
	ifstream ifile;
	ofstream ofile;
	ifile.open("C-small-attempt0.in",ios::in);
	ofile.open("output.out",ios::out);
	ifile>>T;

	for(int i=0;i<T;i++)
	{
		ifile>>A>>B;
		ofile<<"Case #"<<i+1<<": "<<fun(A,B)<<endl;
	}
	
	getch();
}