#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream input("C-large.in");
	ofstream output("outputl.txt");

	int T;
	input >> T;

	for(int caseID = 1; caseID <= T; caseID++)
	{
		//read data
		int N;
		input >> N;
		vector<long> prices;
		long temp;
		for (int i = 0; i != N; i++)
		{
			input >> temp;
			prices.push_back(temp);
		}

		//solve
		long xorSum = 0;
		for (int i = 0; i != N; i++)
		{
			xorSum = xorSum^prices[i];
		}
		long count = 0;
		long min = prices[1];
		for (int i = 0; i != N; i++)
		{
			count = count + prices[i];
			if (min > prices[i])
			{
				min = prices[i];
			}
		}
		count = count - min;


		//output result
		if (xorSum != 0)
		{
			output << "Case #" << caseID << ": NO"<< endl;
		}
		else
		{

			output << "Case #" << caseID << ": "<< count << endl;
		}
		
	}
}