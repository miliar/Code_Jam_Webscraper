#include <iostream>
#include <queue>
using namespace std;

void main ()
{
	int testCases=0;
	int i=1;
	freopen("A-large.in","r",stdin);
	freopen("out1_large.txt","w",stdout);

	for (cin >> testCases; i <= testCases; i++)
    {
		queue <int> Oqueue,indexOqueue,Bqueue,indexBqueue;
		int O=1,B=1;
		int maxSeq,position;
		char color;

		cin >> maxSeq;
		for (int seq = 1; seq <= maxSeq; seq++)
		{
			cin >> color >> position;
			if (color == 'O')
			{
				Oqueue.push(position);
				indexOqueue.push(seq);
			}
			else if (color == 'B')
			{
				Bqueue.push(position);
				indexBqueue.push(seq);
			}
		}

		int curSeq=1;
		int stepCount=0;

		while (curSeq <= maxSeq)
		{
			stepCount++;
			bool pressed = false;
			if (!Oqueue.empty())
			{
				if (O < Oqueue.front()) O++;
				else if (O > Oqueue.front()) O--;
				else if ( curSeq==indexOqueue.front() && O==Oqueue.front())
				{
					Oqueue.pop(); indexOqueue.pop();
					curSeq++;
					pressed=true;
				}
			}
			if (!Bqueue.empty())
			{
				if (B < Bqueue.front()) B++;
				else if (B > Bqueue.front()) B--;
				else if ( curSeq==indexBqueue.front() && B==Bqueue.front() && !pressed)
				{
					Bqueue.pop(); indexBqueue.pop();
					curSeq++;
				}
			}
		}
		cout<< "Case #" << i << ": " << stepCount << endl;
	}
}