#include <iostream>
#include <fstream>
using namespace  std;

int cal(int * c,int n);

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("..\\C-large.in");
	fout.open("..\\C-large.out");

	int testNum;
	fin>>testNum;
	for(int i=1;i<=testNum;i++)
	{
		int n;
		fin>>n;
		int * c=new int[n];
		for(int j=0;j<n;j++)
		{
			fin>>c[j];
		}

		int r=cal(c,n);
		cout<<"Case #"<<i<<": ";
		fout<<"Case #"<<i<<": ";
		if(r<0)
		{
			cout<<"NO"<<endl;
			fout<<"NO"<<endl;
		}
		else
		{
			cout<<r<<endl;
			fout<<r<<endl;
		}
	}

	return 0;
}

int cal(int * c,int n)
{
	int result=0;
	for(int i=0;i<n;i++)
	{
		result=result^c[i];
	}

	if(result!=0)
		return -1;
	int sum=0;
	for(int i=0;i<n;i++)
	{
		sum=sum+c[i];
	}
	int min=c[0];
	for(int i=1;i<n;i++)
	{
		if(c[i]<min)
			min=c[i];
	}

	return sum-min;
}