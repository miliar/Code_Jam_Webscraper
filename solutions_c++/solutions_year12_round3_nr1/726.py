#pragma once
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <list>
#include <queue>
using namespace std;

class Problem1_1C
{
public:
	void Solve(const string& inputFileName, const string& outputFileName)
	{
		cout.precision(2);
		fstream inFile(inputFileName, ios::in);
		string curLine;
		inFile >> curLine;
		int totalLines = atoi(curLine.c_str());
		vector<string> result(totalLines);

		for(size_t i = 0; i < totalLines; ++i)
		{
			int N;
			inFile >> N;
			vector<vector<int>> edges(N);

			for(size_t j = 0; j < N; ++j)
			{
				int totalEdges;
				inFile >> totalEdges;
				vector<int> curEdges(totalEdges, 0);
				for(size_t k = 0; k < totalEdges; ++k)
				{
					inFile >> curEdges[k];
				}
				edges[j] = curEdges;
			}

			result[i] = CalcDiamonds(edges);
		}

		ofstream outFile(outputFileName);
		for(size_t i = 0; i < result.size(); ++i)
		{
			outFile << "Case #" << i + 1 << ": " << fixed << result[i] << endl;
		}
		return;
	}

	string CalcDiamonds(const vector<vector<int>>& edges)
	{
		string yes = "Yes";
		string no = "No";

		vector<bool> indexesToSkip(edges.size(), false);
		for(size_t i = 0; i < edges.size(); ++i)
		{
			if(indexesToSkip[i]) continue;

			vector<int> was(edges.size(), 0);
			queue<int> currentPosition;
			currentPosition.push(i);
			while(currentPosition.size() > 0)
			{
				int cur = currentPosition.front();
				currentPosition.pop();
				was[cur]++;
				if(was[cur] > 1)
				{
					return yes;
				}
				
				for(size_t j = 0; j < edges[cur].size(); ++j)
				{
					currentPosition.push(edges[cur][j] - 1);
					indexesToSkip[edges[cur][j] - 1] = true;
				}
			}
		}
		return no;
	}
};