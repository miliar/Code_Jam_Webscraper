#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int binary_gcd(int a, int b);

int main()
{
	int c; //test case
	int n; //time count
	
	ifstream fin;
	fin.open("B-small.in");
	ofstream fout;
	fout.open("B-small.out");

	fin>>c;
	for(int i=0; i<c; i++)
	{
		fin>>n;
		int* t = new int[n];
		for(int j=0; j<n; j++)
			fin>>t[j];
		
		int* t_sub = new int[n-1];
		for(int j=0; j<n-1; j++)
			t_sub[j] = abs(t[j]-t[j+1]);

		int T = t_sub[0]; //multiple of the largest possible integer factor
		for(int j=1; j<n-1; j++)
			T = binary_gcd(T, t_sub[j]);

		int y = 0; //the minimum number of slarboseconds
		if(T != 1)
			y = T - t[0]%T;
		if(T == y)
			y = 0;

		delete t;
		delete t_sub;

		fout<<"Case #"<<i+1<<": "<<y<<"\n";
	}

	fin.close();
	fout.close();

	return 0;
}

int binary_gcd(int a, int b)
{
	int s;
	if(a==0) return b;
	if(b==0) return a;
	for(s= 0; ((a|b)&1)==0; ++s) //a,b��� ¦���� 2�� ����ؼ� ������
	{
		a >>= 1;
		b >>= 1;
	}
	while((a&1)==0)	//a�� ¦���� a�� ����ؼ� 2�� ����
		a>>=1;
	do 
	{
		while((b&1)==0)	//b�� ¦���� b�� ����ؼ� 2�� ����
			b>>=1;
		if(a<b) //a<b�϶� a=(a,b)�� ������, b=(a,b)�� ��
		{
			b-=a;
		}
		else //a>b�϶� a=(a,b)�� ������, b=(a,b)�� ��
		{
			int diff=a-b;
			a=b;
			b=diff;
		}
		b>>=1;
	}
	while(b!=0);
	return a << s; //���� ����� 2^s(2�� s����)�� ������
}