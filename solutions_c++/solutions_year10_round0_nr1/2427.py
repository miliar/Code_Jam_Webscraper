#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int main()
{
	string fn = "A-large.in";
	
	ifstream input;
	input.open(fn.c_str());
	
	int T,N;
	long long K;
	
	input>>T;
	
	long long bit;
	ofstream output;
	fn = fn.substr(0,fn.length()-2)+"out";
	output.open(fn.c_str());
	
	for(int i=1; i<=T; i++)
	{
		input>>N>>K;
	/*	if(K!=0)
	/	{
			output<<"Case #"<<i<<": OFF"<<endl;
		}
		else */
		{
			bit = 1;
			bit = bit<<(N);
			K= K%bit;
			if(K == bit-1)
			{
				output<<"Case #"<<i<<": ON"<<endl;

			}
			else
			{
				output<<"Case #"<<i<<": OFF"<<endl;
	
			}

		}

		
		
	}

	input.close();
	output.close();
	
	return 0;
}
