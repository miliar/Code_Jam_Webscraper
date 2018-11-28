#include <iostream>

using namespace std;


// Patrick McCulloch
// patmcculloch@gmail.com
// Friday, May 6 2011
// 5:41 PM
// Let's hope this works
// but really, it probably won't

int moveRobot(int robotButtons[], int pos, int pushed);

int main()
{
	// start with number of test cases T
	int T;
	cin >> T;
	// array to store which buttons need pushing
	// array index will be the necessary ordering
	// and value at index will be button number
	// if -1, that indicates other robots button

	for (int i=0; i<T; i++)
	{
		int bButtons [150];
		int oButtons [150];
		int oButs = 0;
		int oPushed = 0;
		int bButs = 0;
		int bPushed = 0;
		int bPos = 1;
		int oPos = 1;
		cout << "Case #" << i+1 << ": ";
		// number of button pushes in this case
		int N;
		cin >> N;	
		for (int j=0; j<N; j++)
		{
			char robot;
			cin >> robot;
			if (robot == 'O')
			{
				oButs++;
				bButtons[j] = -1;
				cin >> oButtons[j];
			}
			if (robot == 'B')
			{
				bButs++;
				oButtons[j] = -1;
				cin >> bButtons[j];
			}
		}
		int time = 0;
		int butsPushed = 0;
		
		while (butsPushed < N)
		{
			if (bButtons[butsPushed] == bPos)
			{
				// blue robot at right place in proper order
				// so move the orange robot, if applicable
				if (oPushed < oButs) 
					oPos = oPos + moveRobot(oButtons, oPos, butsPushed);
				butsPushed++; // and then blue pushes his button
				bPushed++;
				time++;
			}
			else if (oButtons[butsPushed] == oPos)
			{
				// orange robot at right place in proper order
				// so move blue robot, if applicable
				if (bPushed < bButs)
					bPos = bPos + moveRobot(bButtons, bPos, butsPushed);
				butsPushed++;
				oPushed++;
				time++;
			}
			else
			{
				// well, somebody needs to move somewhere...
				if (oPushed < oButs)
					oPos = oPos + moveRobot(oButtons, oPos, butsPushed);
				if (bPushed < bButs)
					bPos = bPos + moveRobot(bButtons, bPos, butsPushed);
				time++;
			}
			
		}	
		cout << time << endl;
	}
	return 0;
}

int moveRobot(int robotButtons[], int pos, int pushed)
{
	// returns 1 if next button is ahead of where he is
	// -1 if next button is behind
	// 0 if he's fine where he is
	int push = pushed;
	int nextBut = robotButtons[push];

	while (nextBut == -1)
	{
		push++;
		nextBut = robotButtons[push];
	}

	if (pos > nextBut)
		return -1;
	else if(pos < nextBut)
		return 1;
	else
		return 0;
}	
