#include "codejam.h"



void qual_A()
{
	int T;
	cin >> T;
	for (int testCase = 1; testCase <= T; testCase++)
	{
		int N;
		cin >> N;

		list<char> robotSeq;  
		list<int> blueSeq;
		list<int> orangeSeq;

		for (int i = 1; i <= N; i++)
		{
			char robot;
			cin >> robot;
			robotSeq.push_back(robot);

			int button;
			cin >> button;
			if (robot == 'B')
			{
				blueSeq.push_back(button);
			}
			else if (robot == 'O')
			{
				orangeSeq.push_back(button);
			}
		}

		int moves = 0;
		int bluePos = 1;
		int orangePos = 1;

		for (list<char>::iterator currentBot = robotSeq.begin(); currentBot != robotSeq.end(); currentBot++)
		{
			list<int>* currentSeq;
			list<int>* otherSeq;
			int* thisPos;
			int* otherPos;
			int currentMoves;

			if (*currentBot == 'B')
			{
				currentSeq = &blueSeq;
				otherSeq = &orangeSeq;
				thisPos = &bluePos;
				otherPos = &orangePos;
			}
			else if (*currentBot == 'O')
			{
				currentSeq = &orangeSeq;
				otherSeq = &blueSeq;
				thisPos = &orangePos;
				otherPos = &bluePos;
			}
			else
			{
				exit(0);
			}

			currentMoves = abs(currentSeq->front() - *thisPos) + 1;
			*thisPos = currentSeq->front();

			if (!otherSeq->empty())
			{
				if (abs(otherSeq->front() - *otherPos) <= currentMoves)
				{
					*otherPos = otherSeq->front();
				}
				else
				{
					if (otherSeq->front() > *otherPos)
					{
						*otherPos += currentMoves;
					}
					else if (otherSeq->front() < *otherPos)
					{
						*otherPos -= currentMoves;
					}
				}
			}
			
			
			currentSeq->pop_front();
			moves += currentMoves;
		}

		cout << "Case #" << testCase << ": " << moves << "\n";

	}
}

