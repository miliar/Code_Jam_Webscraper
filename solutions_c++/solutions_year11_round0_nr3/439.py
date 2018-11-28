#include <iostream>
#include <fstream>
using namespace std;

int N;
int C[1000];

bool Check()
{
	int CC[1000];
	int sign;
	int temp;
	for (int j=0;j<=N-1;j++)
	{
		CC[j]=C[j];
	}

	sign=1;
	while (sign==1)
	{
		sign=0;
		temp=0;
		for (int j=0;j<=N-1;j++)
		{
			temp=temp+CC[j]%2;
			CC[j]=CC[j]/2;
			if (CC[j]!=0)
			{
				sign=1;
			}
		}
		if (temp%2==1)
		{
			return false;
		}
	}
	return true;
}

int main()
{
	int T;
	int sum;
	int small;
	ifstream fin;
	ofstream fout;
	fin.open("C-large.in");
	fout.open("Clarge.txt");
	fin>>T;
	for (int i=1;i<=T;i++)
	{
		fin>>N;
		sum=0;
		small=2000000;
		for (int j=0;j<=N-1;j++)
		{
			fin>>C[j];
		}

		if (Check()==true)
		{
			for (int j=0;j<=N-1;j++)
			{
				sum=sum+C[j];
				if (C[j]<small)
				{
					small=C[j];
				}
			}
			sum=sum-small;
			fout<<"Case #"<<i<<": "<<sum<<endl;
		}
		else
		{
			fout<<"Case #"<<i<<": NO"<<endl;
		}
	}
	return 0;
}