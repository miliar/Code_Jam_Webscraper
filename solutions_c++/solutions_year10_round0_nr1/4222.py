#include<iostream>
#include<cmath>
#include<fstream>
using namespace std;

int main()
{
	ifstream in("A-small-attempt1.in");
	ofstream out("out.txt");
	int T,N,K;
	in>>T;

	for(int i=1;i<=T;i++)
	{
		in>>N>>K;
		if((K)%(int)(pow(2,N))==(int)(pow(2,N)-1))
		{
			out<<"Case #"<<i<<": ON"<<endl;
		}
		else
		{
			out<<"Case #"<<i<<": OFF"<<endl;
		}
	}	
}