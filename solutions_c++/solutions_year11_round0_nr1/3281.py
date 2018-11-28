#include <iostream>
#include <vector>
#include <stdint.h>

using namespace std;

int abs(int a)
{
	if (a < 0)
	{
		return -a;
	}
	return a;
}

void solve(int n, int *buttons)
{
	int pos_orange = 1;
	int pos_blue = -1;
	int steps = 0;
	int steps_orange = 0;
	int steps_blue = 0;

	for (int i = 0; i < n; i++)
	{
		int target = buttons[i];
		
		if (target > 0)
		{
			//
			// Orange's task
			//
			steps_orange += abs(target - pos_orange) + 1;
			if (steps_orange <= steps_blue)
			{
				steps_orange = steps_blue + 1;
			}
			pos_orange = target;
		}
		else
		{
			//
			// Blue's task
			//
			steps_blue += abs(target - pos_blue) + 1;
			if (steps_blue <= steps_orange)
			{
				steps_blue = steps_orange + 1;
			}
			pos_blue = target;
		}
	}
	steps = steps_orange > steps_blue ? steps_orange : steps_blue;
	
	cout << steps << endl;
}


int main()
{
	int ncases = 0;
	cin >> ncases;
	if (!cin) return -1;
	
	for (int i = 0; i < ncases; i++)
	{
		int n, b;
		char c;
		cin >> n;
		int *buttons = new int[n];

		for (int j = 0; j < n; j++)
		{
			cin >> c;
			cin >> b;
			if (!cin) return -1;
			if (c != 'O' && c != 'B') return -1;
			if (b <= 0) return -1;
			if (c == 'O')
			{
				buttons[j] = b;
			}
			else
			{
				buttons[j] = -b;
			}
		}
		
		if (!cin) return -1;
		cout << "Case #" << (i+1) << ": ";
		solve(n, buttons);
	}
	return 0;
}

