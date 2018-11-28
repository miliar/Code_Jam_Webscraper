// 2.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool minMoves(pair<int,int> f, pair<int,int> s)
{
	return (f.first < s.first);
}
int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inFile;
	ofstream outFile;
	inFile.open("D-small-attempt0.in");
	outFile.open("D-small-attempt0.out");
	int caseNumMax;
	inFile >> caseNumMax;
	for (int caseNum = 0; caseNum < caseNumMax; ++caseNum)
	{
		int P, W;
		inFile >> P >> W;
		bool plane[400][400];
		for (int i = 0; i < 400; ++i)
			for (int j = 0; j < 400; ++j)
				plane[i][j] = false;
		
		vector<int> tempvi;
		vector<vector<int>> plane2(P, tempvi);
		int a, b;
		char c;
		for (int i = 0; i < W; ++i)
		{
			inFile >> a >> c >> b;
			if (plane[a][b] == false)
			{
				plane[a][b] = true;
				plane[b][a] = true;
				plane2[a].push_back(b);
				plane2[b].push_back(a);
			}
		}
		vector<bool> tempvvb(P, false);
		pair<int, vector<bool>> tempii;
		tempii.first = P + 1;
		tempii.second = tempvvb;
		vector<pair<int, vector<bool>>> moves(P, tempii);
		vector<int> thr(P, 0);
		int move = 0;
		bool cont = true;
		moves[0].first = 0;
		for (vector<int>::iterator it = plane2[0].begin(); it < plane2[0].end(); ++it)
			moves[0].second[*it] = true;
		thr[0] = plane2[0].size();
		vector<int> an;
		vector<int> anNext;
		an.push_back(0);
		while(cont)
		{
			++move;
			for (vector<int>::iterator it = an.begin(); it < an.end(); ++it)
			{
				int curP = (*it);
				for (vector<int>::iterator itP = plane2[curP].begin(); itP < plane2[curP].end(); ++itP)
				{
					if (moves[(*itP)].first > move)
					{
						moves[(*itP)].first = move;
						moves[(*itP)].second = moves[curP].second;
						moves[(*itP)].second[curP] = false;
						thr[(*itP)] = thr[curP];
						if ((*itP) != 1)
						{
							--thr[(*itP)];
							for (vector<int>::iterator it2 = plane2[(*itP)].begin(); it2 < plane2[(*itP)].end(); ++it2)
							{
								if ( ((*it2) != curP) && !(moves[(*itP)].second[(*it2)]) )
								{
									moves[(*itP)].second[(*it2)] = true;
									++thr[(*itP)];
								}
							}
						}
						anNext.push_back(*itP);
					}
					else if (moves[(*itP)].first == move)
					{
						int curThr = thr[curP];
						vector<bool> curSecond = moves[curP].second;
						curSecond[curP] = false;
						
						if ((*itP) != 1)
						{
							curThr--;
							for (vector<int>::iterator it2 = plane2[(*itP)].begin(); it2 < plane2[(*itP)].end(); ++it2)
							{
								if ( ((*it2) != curP) && !(curSecond[(*it2)]) )
								{
									curSecond[(*it2)] = true;
									++curThr;
								}
							}
						}
						if (curThr > thr[(*itP)])
						{
							thr[(*itP)] = curThr;
							moves[(*itP)].second = curSecond;
						}
					}
				}
			}
			an = anNext;
			if (thr[1] != 0)
				cont = false;
		}

		outFile << "Case #" << caseNum + 1 << ": " << move-1 << ' ' << thr[1] << endl;

	}
	inFile.close();
	outFile.close();
	return 0;
}