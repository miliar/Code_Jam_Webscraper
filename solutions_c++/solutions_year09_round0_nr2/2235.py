// Alien.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fi("D:\\B.in");
	ofstream fo("D:\\B.out");
	int T;


	fi >> T;
	for (int t = 0; t < T; ++t)
	{
		int H, W;
		fi >> H >> W;
		vector<vector<int> > vr(H, vector<int>(W));
		for (int i = 0; i< H; ++i)
			for (int j =0; j< W; ++j)
				fi >> vr[i][j];

		fo << "Case #" << t +1 << ":" << endl; 

		vector<vector<int> > vrVisited(H, vector<int>(W,-1));

		int uBas = 1;
		int curBas = -1;
		vector<int> bas(20000);

		for (int i = 0; i< H; ++i)
			for (int j =0; j< W; ++j)
			{
				if (vrVisited[i][j] != -1)
					continue;
				curBas++;
				int y = i;
				int x = j;

				do
				{
					if (vrVisited[y][x] != -1)
					{
						bas[curBas] = bas[vrVisited[y][x]];
						break;
					}
					vrVisited[y][x] = curBas;
					vector<pair<int, int> > nextMove;
					nextMove.push_back(make_pair(vr[y][x], 0));
					if (y > 0)
						nextMove.push_back(make_pair(vr[y-1][x], 1));
					if (x > 0)
						nextMove.push_back(make_pair(vr[y][x-1], 2));
					if (x +1  < W)
						nextMove.push_back(make_pair(vr[y][x+1], 3));
					if (y +1  < H)
						nextMove.push_back(make_pair(vr[y+1][x], 4));
					sort(nextMove.begin(), nextMove.end());

					if (nextMove.front().second == 0)
					{
						bas[curBas] = uBas;
						uBas++;
						//curBas++;
						break;
					}
					if (nextMove.front().second == 1)
						y--;
					if (nextMove.front().second == 2)
						x--;
					if (nextMove.front().second == 3)
						x++;
					if (nextMove.front().second == 4)
						y++;
				} while(true);
			}

			vector<char> ubasToChar(27, 'N');

			char curLetter= 'a';
			for (int i = 0; i< H; ++i)
			{
				for (int j =0; j< W; ++j)
				{
					char & ch = ubasToChar[bas[vrVisited[i][j]]];
					if (ch == 'N')
					{
						ch = curLetter;
						curLetter++;
					}
					fo << ch;
					if (j+1 < W)
						fo << " ";

				}
				fo << endl;
			}


		
	}



	return 0;
}

