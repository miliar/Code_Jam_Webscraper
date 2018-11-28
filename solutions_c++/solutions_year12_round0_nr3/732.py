// Problem C. Recycled Numbers.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <map>
using namespace std;

int digits(int n)
{
	int dig=0;
	n/=10;
	while(n)
	{
		n/=10;
		dig++;
	}
	return dig;
}

int power(int exp)
{
	int n=1;
	while(exp--)
	{
		n*=10;
	}
	return n;
}

void recorrer(int &n,int dig)
{
	int aux=n%10;
	n/=10;
	n+=aux*power(dig);
}

int main()
{
	ifstream in("Input.in");
	ofstream out("Data.txt");
	int T,A,B,aux,n;
	long long int tot;
	map<int,int> rep;
	in>>T;
	for(int t=1;t<=T;++t)
	{
		in>>A>>B;
		tot=0;
		for(int i=A;i<=B;++i)
		{
			rep.clear();
			aux=digits(i);
			n=i;
			for(int j=0;j<aux;++j)
			{
				recorrer(n,aux);
				if(n<=B&&n>i&&!rep[n])
				{
					tot++;
					rep[n]++;
				}
			}
		}
		out<<"Case #"<<t<<": "<<tot<<endl;
	}
	return 0;
}

