#include <iostream>
#include <vector>
#include <fstream>

using namespace std;
pair <bool,bool> checkNumber(int Number,int S,int P);
int main()
{
	ifstream cin("B-large.in");
	ofstream cout("B-large.out");

	int testCases;
	cin >> testCases;
	for (int i = 0; i < testCases; i++)
	{
		int N,S,P;
		cin >> N >> S >> P;
		vector <int> googlers;
		int current_s = 0;
		int count = 0;
		for (int j = 0; j < N; j++)
		{
			int temp;
			cin >> temp;
			pair <bool,bool> result = checkNumber(temp,S,P);
			if (result.first && !result.second)
				count++;
			else if (result.first && result.second)
			{
				if (current_s < S)
				{
					count++;
					current_s++;
				}
			}
		}
		cout << "Case #" << i + 1 << ": " << count << endl;
	}
	return 0;
}

pair <bool,bool> checkNumber(int Number,int S,int P)
{
	if (Number == 0)
	{
		if (P == 0)
			return make_pair(true,false);
		else
			return make_pair(false,false);
	}
	pair <int,int> result = make_pair(false,false);
	int rem = Number % 3;
	int base_number = Number/3;
	if (rem == 0)
	{
		if (base_number >= P)
			result.first = true;
		else
		{
			if (base_number + 1 >= P)
			{
				result.first = true;
				result.second = true;
			}
		}
	}
	else if (rem == 1)
	{
		if (base_number >= P)
			result.first = true;
		else 
		{
			if (base_number + 1 >= P)
				result.first = true;
		}
	}
	else
	{
		if (base_number >= P || base_number + 1 >= P)
			result.first = true;
		else
		{
			if (base_number +2 >= P)
			{
				result.first = true;
				result.second = true;
			}
		}
	}

	return result;
}