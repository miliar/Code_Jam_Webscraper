#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
void main()
{
	int t,n,k;
	ifstream input;
	ofstream output;
	input.open ("A-large.in");
	output.open ("output.txt");
	input>>t;
	for(int i=1;i<=t;i++)
	{
		input>>n>>k;
		int res = (int) pow(2.0,n);
		if(((k+1) % res)==0)
			output<<"Case #"<<i<<": ON";
		else
			output<<"Case #"<<i<<": OFF";
		output<<endl;
	}
	input.close();
	output.close();
}