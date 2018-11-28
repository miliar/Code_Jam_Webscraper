#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

void main()
{
	ifstream inp("Input.txt");
	ofstream out("Output.txt");
	int T;
	inp>>T;
	for(int i=0;i<T;++i)
	{
		double n1;
		__int64 K;
		inp>>n1>>K;
		__int64 N=pow(2,n1)-1;
		__int64 RES=K&N;
		
		if(RES==N)
		{out<<"Case #"<<i+1<<":"<<" "<<"ON\n";}
		else 
		{out<<"Case #"<<i+1<<":"<<" "<<"OFF\n";}
	}
}
