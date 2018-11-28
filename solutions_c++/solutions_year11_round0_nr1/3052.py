#include <fstream>
using namespace std;

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	char botColor;
	int maxNumOfTests, buttonsInTestCase, buttonNumber;
	
	cin >> maxNumOfTests;
	for (int t = 0; t < maxNumOfTests; t++)
	{
		int orangeCurrent = 1;
		int blueCurrent = 1;
		int blueTime = 0;
		int orangeTime = 0;

		cin >> buttonsInTestCase;
		for (int i = 0; i < buttonsInTestCase; i++)
		{
			cin >> botColor >> buttonNumber;
			switch (botColor)
			{
				case 'O':
					orangeTime += abs(orangeCurrent - buttonNumber) + 1;
					orangeCurrent = buttonNumber;
					if (orangeTime <= blueTime)
					{
						orangeTime = blueTime + 1;
					}
					break;
				case 'B':
					blueTime += abs(blueCurrent - buttonNumber) + 1;
					blueCurrent = buttonNumber;
					if (blueTime <= orangeTime)
					{
						blueTime = orangeTime + 1;
					}
					break;
			}
		}

		cout << "Case #" << t + 1 << ": " << max(blueTime, orangeTime) << endl;;
	}

	return 0;
}