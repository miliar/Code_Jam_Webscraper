#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <utility>
#include <set>
#include <algorithm>
using namespace std;
typedef long long llong;
typedef long double ld;

double findWinPercentage(string a)
{
	int wins = 0, gamesPlayed = 0;
	for(int i=0; i<a.size(); i++)
	{
		if(a[i] == '.') continue;
		if(a[i] == '1') wins++;
		gamesPlayed++;
	}
	return (double(wins) / gamesPlayed);
}

double findWinPercentage(string a, int excludedIndex)
{
	int wins = 0, gamesPlayed = 0;
	for(int i=0; i<a.size(); i++)
	{
		if(a[i] == '.' || i == excludedIndex) continue;
		if(a[i] == '1') wins++;
		gamesPlayed++;
	}
	return (double(wins) / gamesPlayed);
}

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int testCases, Case = 1;
	fin >> testCases;
	while(testCases--)
	{
		fout << "Case #" << Case++ << ":" << endl;;
		int N;
		vector <string> chart;
		vector <double> wp;
		vector <double> op;
		vector <double> oop;
		fin >> N;
		for(int i=0; i<N; i++)
		{
			string temp;
			fin >> temp;
			chart.push_back(temp);
		}
		for(int i=0; i<N; i++)
			wp.push_back(findWinPercentage(chart[i]));
		for(int i=0; i<N; i++)
		{
			double sum = 0, numberTeams = 0;
			for(int j=0; j<N; j++)
			{
				if(chart[i][j] == '.') continue;
				sum += findWinPercentage(chart[j], i);
				numberTeams++;
			}
			op.push_back(sum/numberTeams);
		}
		for(int i=0; i<N; i++)
		{
			double opponentsOWP = 0, opponentsPlayed = 0;
			for(int j=0; j<N; j++)
			{
				if(chart[i][j] == '.') continue;
				opponentsOWP += op[j];
				opponentsPlayed++;
			}
			oop.push_back(opponentsOWP/opponentsPlayed);
		}
		for(int i=0; i<N; i++)
			fout << ((.25 * wp[i]) + (.5 * op[i]) + (.25 * oop[i])) << endl;
	}
	return 0;
}

