#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
	ofstream out;
	ifstream in;

	out.open("output.txt");
	in.open("input.txt");

	int T,N;
	long posO, posB, totalTime,waitTimeO, waitTimeB,addTime;
	char tempBotC;
	int tempPos,tempBotI;
	in >> T;

	for ( int i = 0; i < T; i++ )
	{
		in >> N;
		posO = 1;
		posB = 1;
		totalTime = 0;
		waitTimeO = 0;
		waitTimeB = 0;

		for( int j = 0; j < N; j++ )
		{
			in >> tempBotC;
			in >> tempPos;

			tempBotI = !(tempBotC == 'O');

			if ( tempBotI )
			{
				int tempTime = abs(tempPos - posB ) - waitTimeB;
				addTime = (tempTime > 0)?tempTime + 1:1;
				totalTime += addTime;
				waitTimeO += addTime;
				posB = tempPos;
				waitTimeB = 0;
			}
			else
			{
				int tempTime = abs(tempPos - posO ) - waitTimeO;
				addTime = (tempTime > 0)?tempTime + 1:1;
				totalTime += addTime;
				waitTimeB += addTime;
				posO = tempPos;
				waitTimeO = 0;
			}

		}
		out <<"Case #"<<i+1<<": "<<totalTime<<endl;
	}
	out.close();
	in.close();
}
