// Problem A. Bot Trust

#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;


struct UNIT
{
	char color; // 'O', 'B'
	int pos;    // 1 <= pos <= 100
};

int main()
{
	std::queue<UNIT> q;
	std::vector<int> vecO;
	std::vector<int> vecB;
	
	int T, N, cntO, cntB, posO, posB, time, boundO, boundB;
	UNIT unit;
	bool check;
	
	cin >> T;
	
	for(int count=1; count<=T; ++count)
	{
		// Inputs
		cin >> N;

		vecO.clear();
		vecB.clear();
		
		while(N)
		{
			cin >> unit.color >> unit.pos;
			q.push(unit);
			
			if(unit.color == 'O')
				vecO.push_back(unit.pos);
			else // 'B'
				vecB.push_back(unit.pos);
			--N;
		}
		boundO = static_cast<int>(vecO.size());
		boundB = static_cast<int>(vecB.size());
		
		// Problem Solving
		cntO = 0; cntB = 0;
		posO = 1; posB = 1;
		time = 0;
		while (!q.empty())
		{
			unit = q.front(); q.pop();
//			cout << "UNIT - [" << unit.color << " " << unit.pos << "]" << endl;
			
			check = false;
			while(!check)
			{
				// MOVE +1/-1 or STAY or PUSH for robot O
				if (cntO < boundO)
				{
					if (posO < vecO[cntO])				// MOVE +1
					{	
						++posO;
//						cout << "O - MOVE +1 (" << posO << ")\t\t";
					}
					else if (posO > vecO[cntO])			// MOVE -1
					{	
						--posO;
//						cout << "O - MOVE -1 (" << posO << ")\t\t";
					}
					else if (unit.color == 'O') 		// PUSH
					{	
//						;
//						cout << "O - PUSH (" << posO << ")\t\t";
						
						if (posO == unit.pos) { ++cntO; check = true; }
					}
//					else 								// STAY
//					{
//						;
//						cout << "O - STAY (" << posO << ")\t\t";
//					}
				}
//				else
//				{
//					cout << "O - STAY (" << posO << ")\t\t";
//				}
				
				// MOVE +1/-1 or STAY or PUSH for robot B
				if (cntB < boundB)	
				{
					if (posB < vecB[cntB])				// MOVE +1
					{	
						++posB;
//						cout << "B - MOVE +1 (" << posB << ")\t\t";
					}
					else if (posB > vecB[cntB])			// MOVE -1
					{	
						--posB;
//						cout << "B - MOVE -1 (" << posB << ")\t\t";
					}
					else if (unit.color == 'B') 		// PUSH
					{	
						if (posB == unit.pos) { ++cntB; check = true; }
//						cout << "B - PUSH (" << posB << ")\t\t";
					}
//					else 								// STAY
//					{
//						;
//						cout << "B - STAY (" << posB << ")\t\t";
//					}
				}
//				else
//				{
//					cout << "B - STAY (" << posB << ")\t\t";
//				}
				
				// MOVE or PUSH or STAY consumes 1 sec.
				++time;
//				cout << "TIME - " << time << "\t\t";
//				cout << endl;
			}
		}
		
		// Outputs
		cout << "Case #" << count << ": " << time << endl;
	}
	
	return 0;
}