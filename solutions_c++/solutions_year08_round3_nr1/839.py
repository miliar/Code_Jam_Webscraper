#include<iostream>
#include<fstream>
#include<conio.h>
#include<list>
#include<algorithm>
#include<string>

using namespace std;
long n;
long maxi,pad,lang; 
long a[10000];
int main(void)
{
	fstream fin("a.in",ios::in);
	fstream fout("output.txt",ios::out);

	fin>>n;
	int i;

	for(int k=0;k<n;k++)
	{
		fin>>maxi;
		fin>>pad;
		fin>>lang;
		
		for(i=0;i<lang;i++)
			fin>>a[i];

		long max_f=0,sum=0,r=0,index;

		long pos=1;
for(int j=0;j<lang;j++)
{
	max_f=0;

		for(i=0;i<lang;i++)
		{
			if(max_f<a[i])
			{
				max_f=a[i];
				index=i;
			}
		}
		sum=sum+ max_f*pos;
		a[index]=0;
		r++;
		if(r==pad)
		{
			r=0;
			pos++;
		}
}
fout<<"Case #"<<k+1<<": ";
		fout<<sum<<"\n";
	}
	getch();

	return 0;
}








#include<iostream>
#include<fstream>
#include<conio.h>
#include<list>
#include<algorithm>
#include<string>

using namespace std;
long n;
long maxi,pad,lang; 
long a[10000];
int main(void)
{
	fstream fin("a.in",ios::in);
	fstream fout("output.txt",ios::out);

	fin>>n;
	int i;

	for(int k=0;k<n;k++)
	{
		fin>>maxi;
		fin>>pad;
		fin>>lang;
		
		for(i=0;i<lang;i++)
			fin>>a[i];

		long max_f=0,sum=0,r=0,index;

		long pos=1;
for(int j=0;j<lang;j++)
{
	max_f=0;

		for(i=0;i<lang;i++)
		{
			if(max_f<a[i])
			{
				max_f=a[i];
				index=i;
			}
		}
		sum=sum+ max_f*pos;
		a[index]=0;
		r++;
		if(r==pad)
		{
			r=0;
			pos++;
		}
}
fout<<"Case #"<<k+1<<": ";
		fout<<sum<<"\n";
	}
	getch();

	return 0;
}








