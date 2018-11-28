#include <vector>
#include <iostream>
#include <cstdlib>

using namespace std;

typedef unsigned int uint;
typedef unsigned long long ull;

struct action
{
	char bot;
	int button;
};


int main()
{
	uint numTest;
	cin >> numTest;
	for(uint test=0; test<numTest; ++test)
	{
		
		uint numMoves;
		cin>>numMoves;
		vector<action> moves(numMoves);
		//cout<<test<<endl;
		for(uint move = 0; move < numMoves; ++move)
		{
			cin>>moves.at(move).bot>>moves.at(move).button;
		}
		
		int totTime = 0, BTime = 0, OTime = 0;
		uint BPos = 1, OPos = 1;
		for(uint mov = 0; mov < moves.size(); ++mov)
		{
			if(moves.at(mov).bot == 'O')
			{
				totTime += BTime;
				int temp = abs((int)(moves.at(mov).button - OPos))-BTime;
				if(temp < 0) temp=0;
				OTime += temp+1;
				BTime = 0;
				OPos = moves.at(mov).button;
			}
			else
			{
				totTime += OTime;
				int temp = abs((int)(moves.at(mov).button - BPos))-OTime;
				if(temp < 0) temp=0;
				BTime += temp+1;
				OTime = 0;
				BPos = moves.at(mov).button;
			}
		}
		totTime += (BTime + OTime);
		cout<<"Case #"<<test+1<<": "<<totTime<<endl;
	}
}
