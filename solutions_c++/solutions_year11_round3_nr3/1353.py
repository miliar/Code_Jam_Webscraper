#include<iostream>
#include<fstream>
using namespace std;

int lcm(int,int,int [],int);
void main()
{
	int *f;
	int n,t;
	int l,h;
	ifstream fin;
	ofstream fout;
	fin.open("C-small-attempt0.in");
	fout.open("o.txt");
	fin>>t;
	for(int k=1;k<=t;k++)
	{
	fin>>n;
	f=new int [n];
	fin>>l>>h;
	for(int i=0;i<n;i++)
	{
		fin>>f[i];
	}
	int a=lcm(l,h,f,n);
	if(a==-1)
	{
		fout<<"Case #"<<k<<": NO"<<"\n";
	}
	else
		fout<<"Case #"<<k<<": "<<a<<"\n";
	}
	fin.close();
	fout.close();
}
int lcm(int l,int h,int f[],int n)
{
	int flag=0,lc=-1;
	for(int i=l;i<=h;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(((i%f[j])!=0) && (((f[j])%i)!=0))
			{
				flag=-1;
				break;
			}
			else flag=0;
				
			
		}
		if(flag==0)
		{
			return i;
		}
		
	}
	return -1;
}






