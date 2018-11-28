/*
 * TheNextNumber.cpp
 *
 *  Created on: 2009-9-13
 *      Author: sailingwood
 */

#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

class TheNextNumber
{
public:
	int T;
	void run()
	{
		ifstream input("B-small-attempt0.in");
		ofstream output("B-small-attempt0.out");
		input>>T;
		for (int i=0; i<T; i++)
		{
			long long N;
			input>>N;
			long long result = 0;
			vector<int> list;
			list.push_back(N%10);
			N = N/10;
			unsigned int j;
			int next;
			while(1)
			{
				next = N%10;
				N = N / 10;
				for (j=0; j<list.size(); j++)
				{
					if (next<list[j])
						break;
				}
				// ÕÒµ½~£¡
				if (j<list.size())
					break;
				// Î´ÕÒµ½
				else
					list.push_back(next);
			}
			result = N * 10 + list[j];
			for (int k=0; k<j; k++)
			{
				result = result * 10 + list[k];
			}
			result = result * 10 + next;
			for (int k=j+1; k<list.size(); k++)
			{
				result = result * 10 + list[k];
			}
			output<<"Case #"<<i+1<<": "<<result<<endl;
		}
	}
};

int main(int argc, char** argv)
{
	TheNextNumber tnn;
	tnn.run();
	return 0;
}
