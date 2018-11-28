#include<iostream>
#include<cmath>

using namespace std;

int abs(int x)
{
	if(x >= 0)
		return x;
	return (-1)*x;
}

int sgn(int x)
{
	if(x >= 0)
		return 1;
	return -1;
}
int main(int argc, char** argv)
{
	int T;
	cin >> T;

	for(int t = 0; t < T; t++)
	{
		int N;
		cin >> N;
		int time = 0;
		int bot;
		int position;
		int current[2];
		current[0] = current[1] = 1;
		int bot_previous;
		int delta = 0;
		for(int n = 0; n < N; n++)
		{
			char bot_name;
			cin >> bot_name;
			if(bot_name == 'O')
				bot = 0;
			if(bot_name == 'B')
				bot = 1;
			cin >> position;

			if(n == 0)
				bot_previous = bot;
			if(bot != bot_previous)
			{
				if(delta >= abs((position - current[bot])))
					current[bot] = position;
				else
					current[bot] = current[bot] + delta*sgn(position - current[bot]);
					delta = 0;
			}

			time += abs((position - current[bot])) + 1;
			delta += abs((position - current[bot])) + 1;
			current[bot] = position;
			bot_previous = bot;
		}
		cout << "Case #" << (t+1) << ": " << time << endl;
	}

}

