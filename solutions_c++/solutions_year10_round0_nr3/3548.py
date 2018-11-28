// ThemePark.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

int main()
{
	ifstream inputFile ("C-small-attempt0.in");
	ofstream outputFile ("output.in");
	if(!inputFile.is_open())
		return 0;
	if(!outputFile.is_open())
		return 0;

	string line;
	int totalCases = 0;
	inputFile >> totalCases;
	getline(inputFile, line);  //Get to next line

	for (int i=0; i < totalCases; ++i)  
	{
		int R = 0, k = 0, N = 0;
		inputFile >> R;
		inputFile >> k;
		inputFile >> N;
		getline(inputFile, line);  //Get to next line
		queue<int> groups;
		for (int j=0; j<N; ++j)
		{
			int group_size;
			inputFile >> group_size;
			groups.push(group_size);
		}
		getline(inputFile, line);  //Get to next line

		int amount = 0;
		for (int n=0; n<R; ++n)
		{
			int people = 0;
            queue<int> next_queue;
			while (groups.size() > 0)
			{
				int front = groups.front();
				if((people + front) > k)
					break;
				else
				{
					people += front;
					groups.pop();
					next_queue.push(front);
				}
			}
			int next_queue_size = (int)next_queue.size();
			for(int s=0; s<next_queue_size; ++s)
			{
				groups.push(next_queue.front());
				next_queue.pop();
			}
			amount += people;
		}

		outputFile << "Case #" << (i+1) << ": " << amount << endl;
	}

	inputFile.close();
	outputFile.close();
	return 0;
}

