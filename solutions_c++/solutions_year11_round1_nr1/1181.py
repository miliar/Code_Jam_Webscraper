#include<iostream>
#include<fstream>

using namespace std;

ifstream fin;

long long hcf(long long m,long long n)
{
if(m==0) return 0;
if(n==0) return 0;

long long temp,reminder;
if(m<n)
{

temp=m;
m=n;
n=temp;

}

while(true)
{

reminder=m%n;
if(reminder==0)
return n;
else
m=n;
n=reminder;

}

}


char* run_test(void)
{
	char* T = "Possible";
	char* F = "Broken";	
	
	long long N, Pd, Pg;
	fin>>N>>Pd>>Pg;

	long long HCFd = hcf(Pd,100-Pd);
	long long HCFg = hcf(Pg,100-Pg);

	long long Wd, Ld, Wg, Lg;

	if(Pd==0)
	{ 
		Wd = 0; Ld = 1; 
	}
	else if(Pd==100)
	{
		Wd = 1; Ld = 0; 
	}
	else
	{	
		Wd = Pd/HCFd;
		Ld = (100-Pd)/HCFd;
	}

	if(Pg==0)
	{ 
		Wg = 0; Lg = 1; 
	}
	else if(Pg==100)
	{
		Wg = 1; Lg = 0; 
	}
	else
	{	
		Wg = Pg/HCFg;
		Lg = (100-Pg)/HCFg;
	}

	// conditions
	if((Lg == 0 && Ld > 0)||(Wg == 0 && Wd > 0)||(Wd+Ld > N))
		return F;
	else 
		return T;
	
}

int main()
{
	fin.open("A-large.in");
	long long noTests;
	fin>>noTests;
	ofstream fout("output2.out");

	long long i=0;
	while(i<noTests)
	{
		fout<<"Case #"<<i+1<<": ";
		fout<<run_test()<<'\n';
		i++;
	}
}
