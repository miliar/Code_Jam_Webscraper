#include <cstdlib>
#include <cctype>
#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <assert.h>

using namespace std;

struct Move
{
	char color;
	int space;

	Move(){}
	Move(char C, int S)
	{
		color=C;
		space=S;
	}
};

int next(vector<Move> move, int current, char color)
{
	for(int c=current+1;c<(int)move.size();c++)
	{
		if(move[c].color==color)
		{
			return move[c].space;
		}
	}
	return -1;
}

int main()
{
	ifstream cin("C:\\Users\\Bryan\\Desktop\\TestFile.txt");
	ofstream cout("C:\\Users\\Bryan\\Desktop\\Output.txt");

	int T;
	cin >> T;
	for(int counter=1;counter<=T;counter++)
	{
		int N;
		cin >> N;

		vector<Move> move;
		for(int c=0;c<N;c++)
		{
			char C;
			int S;
			cin >> C >> S;
			move.push_back(Move(C,S));
		}

		int bluePos=1;
		int orangePos=1;

		int blueNext=next(move,-1,'B');
		int orangeNext=next(move,-1,'O');

		int time=0;

		for(int c=0;c<N;c++)
		{
			if(move[c].color=='B')
			{
				time+=(abs(bluePos-blueNext)+1);
				if(orangePos<orangeNext)
				{
					orangePos+=min(abs(bluePos-blueNext)+1,orangeNext-orangePos);
				}
				if(orangePos>orangeNext)
				{
					orangePos-=min(abs(bluePos-blueNext)+1,orangeNext-orangePos);
				}
				bluePos=blueNext;
				blueNext=next(move,c,'B');
			}

			if(move[c].color=='O')
			{
				time+=(abs(orangePos-orangeNext)+1);
				if(bluePos<blueNext)
				{
					bluePos+=min(abs(orangePos-orangeNext)+1,blueNext-bluePos);
				}
				if(bluePos>blueNext)
				{
					bluePos-=min(abs(orangePos-orangeNext)+1,blueNext-bluePos);
				}
				orangePos=orangeNext;
				orangeNext=next(move,c,'O');
			}
		}

		cout << "Case # " << counter << ": " << time << '\n';
	}

	return 0;
}