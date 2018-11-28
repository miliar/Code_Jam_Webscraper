
#include <fstream> 
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main()
{
	int numOfTests = 0;
	int count = 1;
	int num = 0;
	int snap = 0;

	// obtain the number of test cases
	ifstream input("G:/test.txt");
	ofstream output("G:/output.txt");
	input >> numOfTests;

	//output<< numOfTests <<endl;

	while(count <= numOfTests)
	{
		num = snap = 0;
		input >> num;
		input >> snap;

		// the first ON of the light
		int s = (double)pow(2.0,num);
		s = s - 1;

		// accelerate the decision
		if(snap < s) 
		{
			//output<<num;
			//output<<" ";
			//output<<snap;
			output<<"Case #";
			output<<count;
			output<<": OFF"<<endl;
		}
		else if((snap-s)%(s+1) == 0)  // round
		{
			/*output<<num;
			output<<" ";
			output<<snap;*/
			output<<"Case #";
			output<<count;
			output<<": ON"<<endl;
		}
		else
		{
			/*output<<num;
			output<<" ";
			output<<snap;*/
			output<<"Case #";
			output<<count;
			output<<": OFF"<<endl;
		}

		// next test case
		count++;
	}

	return 0;
}
