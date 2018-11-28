#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

const string inputFile = "A-large.in";

int max(int a, int b)
{
if(a>b)
return a;
return b;
}


long long process(int i)
{
	long long returnValue = 100;
	// 2 , 4, 5, 25
	int dividend =i/2;
	if(dividend * 2 == i)
	{
		returnValue /=2;
		dividend =i/4;
		if(dividend*4 == i)
		{
				returnValue /=2;
		}
	}
	
	dividend =i/5;
	if(dividend * 5 == i)
	{
		returnValue /=5;
		dividend =i/25;
		if(dividend*25 == i)
		{
				returnValue /=5;
		}
	}
	
	return returnValue;
	
}

int main()
{
	
	ifstream input;
	input.open(inputFile.c_str());
	int T;
	input>>T;
	ofstream output;
	output.open((inputFile+".out").c_str());
	
	long long* lowestNumberOfGames = new long long[101];
	
	for(int i=1; i<=100; i++)
	{
		int dividend = 100/i;
		if(dividend * i == 100) 
			lowestNumberOfGames[i] = dividend;
		else
			{
				lowestNumberOfGames[i]  = 	process(i);
			}
			
	//		cout<<i<<" "<<	lowestNumberOfGames[i] <<endl;
	}
	
	lowestNumberOfGames[0] = 0;
	
	long int N, D,G;
	for(int t=1; t<=T; t++)
	{
		input>>N>>D>>G;
		if(G==100)
		{
			if(D!= 100)
				output<<"Case #"<<t<<": Broken"<<endl;
				else
						output<<"Case #"<<t<<": Possible"<<endl;
		}
		else if(G==0)
		{
				if(D!= 0)
					output<<"Case #"<<t<<": Broken"<<endl;
					else
							output<<"Case #"<<t<<": Possible"<<endl;
		}
		else
		{
			if(N>=lowestNumberOfGames[D])
			output<<"Case #"<<t<<": Possible"<<endl;
			else
				output<<"Case #"<<t<<": Broken"<<endl;
			
			
		}
	}


	delete []	lowestNumberOfGames;
					//	output<<"Case #"<<t<<": "<<totalSteps<<endl;
	

	return 0;
}
