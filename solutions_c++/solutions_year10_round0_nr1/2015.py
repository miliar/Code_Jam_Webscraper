#include<iostream>
#include<fstream>
#include<cmath>
#include<time.h>
using namespace std;
#define S 30
int N[S],two[31];

void init()
{
	for (int i = 0; i <= S ; i++)
	{
		N[i] = 0;
	}
	two[0]=1;
	for ( int i = 1 ; i <=30 ; i++)
	{
		two[i] = two[i-1]*2;
	}
}
int func(long long unsigned int n,long long unsigned int k)
{
	if ( ((k%two[n]) / ( two[n] - 1 )) == 1 )
		return 1;

	return 0;
	

}
int main()
{  
	init();
	long long int no;
	fstream f("a.in",ios::in);
	fstream f2("outpu.txt",ios::out);
	f >> no;
	long long unsigned int n,k;
	for ( int i = 1 ; i <= no ; i ++)
	{
		f >> n >> k;
		if ( func(n,k))
			f2 << "Case #"<<i<<": ON"<<endl;
		else
			f2 << "Case #"<<i<<": OFF"<<endl;
	}
	f.close();
	f2.close();
	return 0;
}

