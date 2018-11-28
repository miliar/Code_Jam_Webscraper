#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <list>
#include <stdlib.h>

using namespace std;

bool palindrome(string word)
{
	for(int i = 0; i < word.size() - 1; i++)
	{
		if(word[i] != word[i + 1])
			return false;
	}

	return true;
}

list<int> recycle(int number)
{
	stringstream ss;
	ss << number;
	string num = ss.str();

	list<int> results;

	if(num.size() <= 1)
	{
		return results;
	}
	else
	{
		string curr = num;

		for(int i = 0; i < num.size() - 1; i++)
		{
			curr = curr[curr.size() - 1] + curr.substr(0, curr.size() - 1);
			results.push_back(atoi(curr.c_str()));
		}
	}

	return results;
}

int main(int argc, char** argv)
{
	ifstream myfile(argv[1]);

	string num_inputs;
	getline(myfile, num_inputs);

	int num = atoi(num_inputs.c_str());

	list<int> numbers;

	//read in number pairs
	for(int i = 0; i < num; i++)
	{
		string line;
		getline(myfile, line);
		
		string num1;
		string num2;

		for(int j = 0; j < line.size(); j++)
		{
			if(line[j] == ' ')
			{
				num1 = line.substr(0, j);
				num2 = line.substr(j + 1, line.size());
				break;
			}
		}

		numbers.push_back(atoi(num1.c_str()));
		numbers.push_back(atoi(num2.c_str()));
	}	

	int count = 1;
	list<int>::iterator it;
	ofstream result;
	result.open("output.txt");
	
	//find the number of recycled numbers and write to file
	for(it = numbers.begin(); it != numbers.end(); ++it)
	{
		int recs = 0;
		int num1 = *it;
		it++;
		int num2 = *it;

		list<int> found;

		for(int n = num1; n < num2; n++)
		{
			list<int> recycled_nums = recycle(n);

			list<int>::iterator iter;
			for(iter = recycled_nums.begin(); iter != recycled_nums.end(); ++iter)
			{
				int m = *iter;
				if((m >= num1)&&(m > n)&&(m <= num2))
				{
					recs++;
					found.push_back(m * n);
				}
			}
		}

		found.sort();
		found.unique();

		result << "Case #" << count << ": " << found.size() << endl;
		count++;
	}

	result.close();
}
