#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

const string inputFile = "C-large.in";



int main()
{
	
	ifstream input;
	input.open(inputFile.c_str());
	int T;
	input>>T;
	ofstream output;
	output.open((inputFile+".out").c_str());
	
	for(int t=1;t<=T; t++)	
	{
			int N;
			int min = 10000000;
			int number;
			int sum = 0;
			long int real_sum =0;
			input>>N;
			
			for(int n=1; n<=N; n++)
			
			{
				input>>number;
				sum ^= number;
				if(number<min)
				{
					min = number;
				
				}
				real_sum += long(number);
				
			}
			
			if(sum!=0)
					output<<"Case #"<<t<<": NO"<<endl;
			else
				output<<"Case #"<<t<<": "<<real_sum-long(min)<<endl;
	}

	return 0;
}
