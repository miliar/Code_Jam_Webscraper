
#include <iostream>
#include <fstream>
#include <string>
#include <queue>

using namespace std;


int main()
{

	ifstream input("smallC.in");
	ofstream output("smallC.out");
	string line;

	int numInputs;

	input >> numInputs;

	for (int i=0; i<numInputs; i++)
	{
		//Parse a test case
		//Get R,k,N
		long R, k, N;
		long in;
		do
		{
			getline(input,line);
		} while (line == "");
		
		sscanf(line.c_str(),"%ld %ld %ld",&R, &k, &N);

		//Set the queue
		queue<long> x;
		for (int j=0; j<N; j++)
		{
			input >> in;
			x.push(in);
		}

		//Queue assembled. Make R rides:
		long money = 0;
		for (int j=0; j<R; j++)
		{
			long inRide = 0;
			queue<long> tempQ;
			while (!x.empty() && x.front()+inRide<=k)
			{
				tempQ.push(x.front());
				money += x.front();
				inRide += x.front();
				x.pop();
			}

			//Restore the queue
			while (!tempQ.empty())
			{
				x.push(tempQ.front());
				tempQ.pop();
			}
		}

		//Write output line
		output << "Case #" << i+1 << ": " << money << endl;

	}

	input.close();
	output.close();

	cout << "done\n";

	int a;
	cin >> a;
	return 0;
}