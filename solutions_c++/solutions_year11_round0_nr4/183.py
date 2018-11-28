#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

/*
int nextIndex(vector<int> input, int startFrom)
{
	for(int i = startFrom; i < input.size(); i++)
	{
		if(input[i] == startFrom + 1 )
		{
			return i;
		}
	}
}

double func(vector<int> input)
{
	double exp = 0.0;
	for(int i = 0; i < input.size(); i++)
	{
		if(input[i] != i+1)
		{
			int index = nextIndex(input, i);
			int temp = input[i];
			input[i] = input[index];
			input[index] = temp; 

			exp += 2.0;
		}
	}

	return exp;

}
*/


double numNonPlace(vector<int> vec)
{
	double count = 0;
	for(int i = 0; i < vec.size(); i++)
	{
		if(vec[i] != i+1)
			count = count + 1.0;

	}

	return count; 
}

int main()
{
	ifstream in("D-large.in");
	ofstream out("D-large.out");

	int T;
	in >> T;
	int i, j; 
	string s;

	getline(in, s); 

	for(i = 0; i < T; i++)
	{
		int N;
		in >> N;
		vector<int> vec; 
		int temp;
		for(j = 0; j < N; j++)
		{
			in >> temp;
			vec.push_back(temp);
		}

		out << "Case #" << i + 1 << ": " << numNonPlace(vec) << endl;

		getline(in, s); 
	}
	return 0;
}