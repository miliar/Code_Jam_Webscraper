#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("atc");
#define cin fin
int GCD(int b)
{
	int a=100;
    while( 1 )
    {
        a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

        if( b == 0 )
			return a;
    }
}

void stuff()
{
	int N,PD,PG;
	cin>>N>>PD>>PG;
	if(PG==0)
	{
		if(PD==0 )
			cout<<"Possible";
		else
			cout<<"Broken";
		return;
	}
	if(PG==100)
	{
		if(PD ==100)
			cout<<"Possible";
		else
			cout<<"Broken";
		return;
	}
	int G1=GCD(PD);
	double k=100/G1;
	if(k>N)
		cout<<"Broken";
	else
		cout<<"Possible";
	
}

int main(void)
{
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		stuff();
		cout<<endl;
	}
	
}
