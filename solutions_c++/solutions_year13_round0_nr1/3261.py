#include <iostream>

using namespace std;

int main()
{
	int cases;
	cin >> cases;
	for(int n=1; n<=cases; n++)
	{
		int columnX[4] = {0, 0, 0, 0};
		int columnO[4] = {0, 0, 0, 0};
		int diagOneX = 0;
		int diagTwoX = 0;
		int diagOneO = 0;
		int diagTwoO = 0;
		int state = 2; // 0=X won, 1=O won, 2=Draw, 3=Not ended
		for(int i=0; i<4; i++)
		{
			int lineX = 0;
			int lineO = 0;
			string line;
			cin >> line;
			
			for(int j=0; j<4; j++)
			{
				char current = line[j];
				if(current == '.')
				{
					if(state == 2)
						state = 3;
				}
				else if(current == 'X')
				{
					lineX++;
					columnX[j]++;
					if(i == j)
						diagOneX++;
					else if(i+j==3)
						diagTwoX++;
				}
				else if(current == 'O')
				{
					lineO++;
					columnO[j]++;
					if(i == j)
						diagOneO++;
					else if(i+j==3)
						diagTwoO++;
				}
				else if(current == 'T')
				{
					lineX++;
					lineO++;
					columnX[j]++;
					columnO[j]++;
					if(i == j)
					{
						diagOneX++;
						diagOneO++;
					}
					else if(i+j==3)
					{
						diagTwoX++;
						diagTwoO++;
					}
				}
			}
			if(lineX == 4)
				state = 0;
			else if(lineO == 4)
				state = 1;
		}
		if(diagOneX == 4 || diagTwoX == 4 || columnX[0] == 4 || columnX[1] ==4 || columnX[2]==4 || columnX[3] == 4)
			state = 0;
		else if(diagOneO == 4 || diagTwoO == 4 || columnO[0] == 4 || columnO[1] ==4 || columnO[2]==4 || columnO[3] == 4)
			state = 1;

		cout << "Case #" << n <<": ";

		if(state == 0)
			cout << "X won";
		else if(state == 1)
			cout << "O won";
		else if(state == 2)
			cout << "Draw";
		else if(state == 3)
			cout << "Game has not completed";
		cout << endl;
	}
	return 0;
}
