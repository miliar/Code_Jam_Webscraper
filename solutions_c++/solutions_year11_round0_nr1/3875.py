#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int main(void) {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		int N;
		cin >> N;

		int orange[200]; 
		int blue[200];  

		int orangeNext[200]; 
		int blueNext[200];  

		for (int j = 0; j < 200; j++)
		{
			orange[j] = blue[j] = orangeNext[j] = blueNext[j] = 0;
		}

		int orSeq = 1;
		int blSeq = 1;

		for (int j = 1; j  <= N; j++)
		{
			char d;
			int p;
			cin >> d;
			cin >> p;
			if (d == 'O') 
			{					
				orange[orSeq] = j;
				orangeNext[orSeq++] = p;
			} else {
				blue[blSeq] = j;
				blueNext[blSeq++] = p;
			}
		}
		int steps			= 1;
		int totalTime		= 0;

		int actPosBlue		= 1;
		int actPosOrange	= 1;

		int actSeqBlue		= 1;
		int actSeqOrange	= 1;

		int headingBlue		= blueNext[actSeqBlue];
		int headingOrange	= orangeNext[actSeqOrange];

		int actDirBlue = (actPosBlue > headingBlue) ? -1 : (actPosBlue == headingBlue)? 0 : 1;
		int actDirOrange = (actPosOrange > headingOrange) ? -1 : (actPosOrange == headingOrange)? 0 : 1;

		int blueActive = 1;
		int orangeActive  = 1;

		int pushedButton = 0;
		do {
			pushedButton = 0;
			if (blueActive) {
				if (actPosBlue != headingBlue) 
				{
					actPosBlue += actDirBlue;
				} else {
					if ((pushedButton == 0) && (blue[actSeqBlue] == steps))
					{
						pushedButton = 1;
						steps += 1;
						if (actSeqBlue <= blSeq) {
							actSeqBlue++;
							headingBlue	= blueNext[actSeqBlue];
							actDirBlue = (actPosBlue > headingBlue) ? -1 : (actPosBlue == headingBlue)? 0 : 1;
						} else blueActive = 0;
					}
				}
			}
			if (orangeActive)
			{
				if (actPosOrange != headingOrange) {
					actPosOrange += actDirOrange;	
				} else {
					if ((pushedButton == 0) && (orange[actSeqOrange] == steps))
					{
						pushedButton = 1;
						steps += 1;
						if (actSeqOrange <= orSeq) {
							actSeqOrange++;
							headingOrange	= orangeNext[actSeqOrange];
							actDirOrange	= (actPosOrange > headingOrange) ? -1 : (actPosOrange == headingOrange)? 0 : 1;
						} else orangeActive = 0;
					}
				}
			}
			totalTime++;			
		} while (steps <= N);
		cout << "Case #" << (i+1) <<": " <<totalTime << "\n";
	}
}
