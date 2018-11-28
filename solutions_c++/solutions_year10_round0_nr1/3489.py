#include <iostream>
#include <fstream>
using namespace std;

long long int power(long long int a, long long int b) // rturns a^b
{
	long long int c = 1;
	for (int i=0;i<b;i++)
		c *= a;
	return c;	
}

int main()
{
	ifstream in;
	in.open("A-large.in");
	ofstream out;
	out.open("A-large.out");
	long long int T, N, K;
	in >> T;
	for (int i=0;i<T;i++)
	{
		in >> N >> K;
		out << "Case #" << i+1 << ": ";
		if (K % power(2, N) == (power(2, N) - 1))
			out << "ON" << endl;
		else
			out << "OFF" << endl;
	}
	return 0;	
}
