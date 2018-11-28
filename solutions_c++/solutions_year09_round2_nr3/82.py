#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;


const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, 1, 0, -1};

vector<string> SolveTestCase()
{
	int W, Q;
	cin >> W >> Q;

	const int maxSum = 500;

	vector<string> squareMath(W);
	for (int i = 0; i < W; i++)
		cin >> squareMath[i];

	vector<int> queries(Q);
	for (int i = 0; i < Q; i++)
	{
		cin >> queries[i];
		queries[i] += maxSum;
	}

	vector< vector< vector<bool> > > curPoss(W, vector< vector<bool> > (W, vector<bool> (2 * maxSum + 1, false) ) );
	vector< vector< vector<bool> > > prevPoss(W, vector< vector<bool> > (W, vector<bool> (2 * maxSum + 1, false) ) );

	vector< vector< vector<string> > > curBest(W, vector< vector<string> > (W, vector<string> (2 * maxSum + 1, "") ) );
	vector< vector< vector<string> > > prevBest(W, vector< vector<string> > (W, vector<string> (2 * maxSum + 1, "") ) );

	for (int i = 0; i < W; i++)
		for (int j = 0; j < W; j++)
			if (squareMath[i][j] >= '0' && squareMath[i][j] <= '9')
			{
				curPoss[i][j][ squareMath[i][j] - '0' + maxSum] = true;
				curBest[i][j][ squareMath[i][j] - '0' + maxSum] += squareMath[i][j];
			}

	vector<string> answer(Q, "");
	int queriesLeft = Q;
	for (int len = 1; queriesLeft > 0; len++)
	{
		for (int h = 0; h < Q; h++)
			if (answer[h] == "")
				for (int i = 0; i < W; i++)
					for (int j = 0; j < W; j++)
						if (curPoss[i][j][ queries[h]] ) 
						{
							if (answer[h] == "")
							{
								answer[h] = curBest[i][j][queries[h]];
								queriesLeft--;
							}
							else
							{
								if (answer[h] > curBest[i][j][queries[h]])
									answer[h] = curBest[i][j][queries[h]];
							}
						}

		prevBest = curBest;
		prevPoss = curPoss;

		curPoss = vector< vector< vector<bool> > > (W, vector< vector<bool> > (W, vector<bool> (2 * maxSum + 1, false) ) );

		for (int i = 0; i < W; i++)
			for (int j = 0; j < W; j++)
				for (int sum = 0; sum <= 2 * maxSum; sum++)
					if (prevPoss[i][j][sum])
					{
						for (int dir = 0; dir < 4; dir++)
						{
							int factor = 1;
							int ii = i + dy[dir];
							int jj = j + dx[dir];
							if (ii < 0 || ii >= W || jj < 0 || jj >= W) continue;
							if (squareMath[ii][jj] == '-') factor = -1;

							for (int dir1 = 0; dir1 < 4; dir1 ++)
							{
								int i1 = ii + dy[dir1];
								int j1 = jj + dx[dir1];
								if (i1 < 0 || i1 >= W || j1 < 0 || j1 >= W) continue;
								string newStr =  prevBest[i][j][sum] + squareMath[ii][jj] + squareMath[i1][j1];
								int newSum = sum + factor * (squareMath[i1][j1] - '0');
								if (newSum >= 0 && newSum <= 2 * maxSum)
								{
									if (curPoss[i1][j1][newSum])
										curBest[i1][j1][newSum] = min(curBest[i1][j1][newSum], newStr);
									else
									{
										curPoss[i1][j1][newSum] = true;
										curBest[i1][j1][newSum] = newStr;
									}
								}
							}
							
								
						}
							
					
					}
	}

	return answer;


}

void PrintAnswerToTestCase(int caseNumber, vector<string> answer )
{
	cout << "Case #" << caseNumber << ":"  << endl;
	for (int i = 0; i < answer.size(); i++)
		cout << answer[i] << endl;
}

int main()
{
	freopen("small.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase() );

	return 0;
}