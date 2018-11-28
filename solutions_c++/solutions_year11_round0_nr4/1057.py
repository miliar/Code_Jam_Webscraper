#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream input("D-large.in");
	ofstream output("outputl.txt");

	int T;
	input >> T;

	for(int caseID = 1; caseID <= T; caseID++)
	{
		//read data
		int N;
		input >> N;
		vector<int> mydata;
		mydata.push_back(-1);
		int temp;
		for (int i = 0; i != N; i++)
		{
			input >> temp;
			mydata.push_back(temp);

		}

		//solve
		int inpos = 0;
		int mypair = 0;
		for (int i = 1; i!= mydata.size();i++)
		{
			//int index = i+1;
			if (i == mydata[i])
			{
				inpos++;
			}
			if (mydata[mydata[i] ] == i)
			{
				mypair++;
			}

		}
		float ret = float (mydata.size()-1-2*mypair - inpos + 2*mypair);

		//output result
		output << "Case #" << caseID << ": "<< ret << endl;
	}
}