#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

int findAmount(int split, vector <int> candy)
{
	int left = candy[0], right = candy[split];
	for(int i=1; i<split; i++)
		left = (left ^ candy[i]);
	for(int i=split+1; i<candy.size(); i++)
		right = (right ^ candy[i]);
	
	if(left != right) return -1;
	
	left = 0;
	right = 0;
	for(int i=0; i<split; i++)
		left += candy[i];
	for(int i=split; i<candy.size(); i++)
		right += candy[i];
	
	if(right > left) return right;
	return left;
}

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int testcases;
	fin >> testcases;
	vector <int> answers;
	while(testcases--)
	{
		vector <int> candies;
		int max = 0, numberCandies;
		fin >> numberCandies;
		for(int i=0; i<numberCandies; i++)
		{
			int temp;
			fin >> temp;
			candies.push_back(temp);
		}
		sort(candies.begin(), candies.end());
		for(int i=1; i<numberCandies; i++)
		{
			int temp = findAmount(i, candies);
			if(temp > max)max = temp;
		}
		answers.push_back(max);
	}
	for(int i=0; i<answers.size(); i++)
	{
		if(answers[i] > 0)
			fout << "Case #" << i+1 << ": " << answers[i] << endl;
		else fout << "Case #" << i+1 << ": " << "NO" << endl;
	}
	return 0;
}
