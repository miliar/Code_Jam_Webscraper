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
	for(s= 0; ((a|b)&1)==0; ++s) //a,b모두 짝수면 2로 계속해서 나눠줌
	{
		a >>= 1;
		b >>= 1;
	}
	while((a&1)==0)	//a만 짝수면 a를 계속해서 2로 나눔
		a>>=1;
	do 
	{
		while((b&1)==0)	//b만 짝수면 b를 계속해서 2로 나눔
			b>>=1;
		if(a<b) //a<b일때 a=(a,b)중 작은값, b=(a,b)의 차
		{
			b-=a;
		}
		else //a>b일때 a=(a,b)중 작은값, b=(a,b)의 차
		{
			int diff=a-b;
			a=b;
			b=diff;
		}
		b>>=1;
	}
	while(b!=0);
	return a << s; //나온 결과에 2^s(2의 s제곱)를 곱해줌
}