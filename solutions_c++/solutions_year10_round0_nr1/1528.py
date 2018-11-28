#include <cstdlib>
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

ifstream in("A.in");
ofstream out("A.txt");

int main()
{
	int n[31];
	for (int i=0; i<=30; i++)
	{
		n[i]=pow(2,i);
	}
	
	int T;
	in>>T;
	for (int t=1; t<=T; t++)
	{
		int N, K;
		in>>N>>K;
		out<<"Case #"<<t<<": ";
		if (((K+1)%n[N])==0)
			out<<"ON"<<endl;
		else
			out<<"OFF"<<endl;
	}
    return 0;
}
