#include <iostream>
#include <xutility>
#include <vector>

using namespace std;

void SolveTest();

void main()
{
	int numTests;
	cin >> numTests;

	for(int i = 0; i < numTests; ++i)
	{
		cout << "Case #" << i+1 << ": ";
		SolveTest();
	}
}

void SolveTest()
{
	static int testNum = 0;
	++testNum;

	int numPlayers, low, high;
	int players[1000];

	cin >> numPlayers;
	cin >> low;
	cin >> high;

	for(int i = 0; i < numPlayers; ++i)
	{
		int freq;
		cin >> freq;
		players[i] = freq;
	}
		

	for(int i = low; i <= high; ++i)
	{
		bool divides = true;
		for(int j = 0; j < numPlayers; ++j)
		{
			if(players[j] % i != 0 && i % players[j] != 0)		
			{
				divides = false;
				break;
			}
		}
		if(divides == true)
		{
			cout << i << endl;
			return;
		}
	}

	cout << "NO" << endl;
}