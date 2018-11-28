#include <map>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int calc(int surprising, int avg, vector<int> scores)
{
	int result = 0;

	for(int i = 0; i != scores.size(); i++)
	{
		int average = scores[i] / 3;
		int rest = scores[i] - average * 3;

		if (scores[i] == 0 && avg == 0)
			result++;
		else if (rest == 1)
		{
			int highest = average + 1;
			if (highest >= avg)
				result++;
		}
		else if (rest == 2)
		{
			int highest = average + 1;
			if (highest >= avg)
				result++;
			else if(highest + 1 >= avg && surprising != 0)
			{
				result++;
				surprising--;
			}
		}
		else if (rest == 0 && scores[i] > 0)
		{
			int highest = average;
			if (highest >= avg)
				result++;
			else if(highest + 1 >= avg && surprising != 0)
			{
				result ++;
				surprising--;
			}

		}
	}

	return result;
}


int main()
{
	ifstream input("c:\\large2.in");
	ofstream output("c:\\output.txt");
	int n;
	input >> n;
	for(int i = 0; i < n; i++)
	{
		string temp = "Case #";
		int num;
		int surprising;
		int average;
		vector<int> scores;

		input >> num >> surprising >> average;

		for(int j = 0; j != num; j++)
		{
			int t;
			input >> t;
			scores.push_back(t);
		}
		
		char msg[1000];
		itoa(i + 1, msg, 10);
		temp += msg;
		temp += ": ";
		itoa(calc(surprising, average, scores), msg, 10);
		temp += msg;
		temp += '\n';
		output << temp;

	}
	output.close();
	input.close();
}

