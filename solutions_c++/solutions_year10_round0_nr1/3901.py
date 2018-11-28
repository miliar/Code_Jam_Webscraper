#include <fstream>
#include <cmath>
using namespace std;

long t;
long n[10000], k[10000];

int main()
{
	ifstream infile("1.in");
	ofstream outfile("1.out");
	infile>>t;
	for (int i=0; i<t; i++)
		infile>>n[i]>>k[i];
	
	for (int i=0; i<t; i++)
	{
		outfile<<"Case #"<<i+1<<": ";
		long temp = (long)pow(2, (double)n[i]);
		if (k[i]%temp == temp - 1)
			outfile<<"ON"<<endl;
		else
			outfile<<"OFF"<<endl;
	}
	return 0;
}
			
			
