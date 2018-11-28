#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

double get(double a,int t)
{
	if(t == 0)
		return 1;
	if(t == 1)
		return a;
	
	double k;
	if(t%2==0)
	{
		k = get(a,t/2);
		k = k*k;
	}
	else
	{
		k = get(a,t/2);
		k = k*k * a;
	}
	while(k>10000000)
		k-=10000000;
	return k;
}

int main()
{
	ifstream fin ("C-small-attempt2.in");
	ofstream fout ("test.out");

	int i,j;
	double a = log(3 + sqrt(5.0)) / log(10.0);
	int n,cases;
	
	fin>>n;
	int t;
	int precalc[30]=
	{
		1,27,143,751,935,
		607,903,991,335,47,
		943,471,55,447,463,
		991,95,607,263,151,
		855,527,743,351,135,
		407,903,791,135,647
	};
	for(cases = 1; cases <= n; cases++)
	{
		fin>>t;
		double k = a * t;
		while(k>1000)
			k-=1000;
		while(k>10)
			k-=10;
		
		int kk = (int)(pow(10.0,k)+ 0.0001);

		char str[100];
		sprintf(str, "%03ld",precalc[t-1]);
		fout<<"Case #"<<cases<<": "<<str<<endl;
	}

}
