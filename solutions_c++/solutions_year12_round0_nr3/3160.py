// problem3.cpp : Defines the entry point for the console application.
//


#include <fstream>
using namespace std;
int A,B;
int left_move(int a,int size)
{
	int a0=a;
	int multiple=1;
	int b1,b2,sum=0;
	for(int j=0;j<size-2;j++)
	{
		multiple*=10;
	}
	for(int k=0;k<size-1;k++)
	{
		b1=a/(multiple*10);
		b2=(a%(multiple*10))/multiple;
		a=(a%(multiple*10))*10+b1;
		if(0==b2||a<A||a>B||a0>=a)continue;
		sum++;
	}
	return sum;
}
int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt.out");
	int n,num_size;
	int temp,result;
	fin>>n;
	for(int i=0;i<n;i++)
	{
		fin>>A>>B;
		temp=A;
		result=0;
		num_size=1;
		while(temp/=10)num_size++;
		if(1==num_size)result=0;
		else 
		{
			for(int j=A;j<=B;j++)
			{
				result+=left_move(j,num_size);
			}
		}
		fout<<"Case #"<<i+1<<": "<<result;
		if(i<n-1)fout<<endl;
	}
		return 0;
}


