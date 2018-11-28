#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

main ()
{
	int t;
	cin >> t;

	for (int T = 1; T <= t; T++)
	{
		int n;
		cin >> n;

		queue < int > bluePos;
		queue < int > orangePos;
		char colour[n];

		// read the button colours and positions
		
		char color;
		int pos;
		for (int i = 0; i < n; i++)	
		{ 
			cin >> color >> pos;			
			if (color == 'O') orangePos.push(pos);
			else bluePos.push(pos);
			colour[i] = color;
		}		
	
		int sec = 0;
		int o = 1, b = 1;
		int i = 0;
		while (i < n)
		{
			sec++;
			int curr_o = -1,curr_b = -1;
			if (!orangePos.empty()) curr_o = orangePos.front();
			if (!bluePos.empty()) curr_b = bluePos.front();
			if (colour[i] == 'O' && curr_o == o)
			{
				// push this button	
				//cout << "Orange pushed button O " << o << " -------------- ";
				orangePos.pop();
				i++;
				if (i == n) break;
				else
				{
					if (curr_b == -1) continue;
					if (curr_b > b) b++; // move 1 forward
					else if (curr_b < b) b--; // move 1 backward
					else { } // wait here itself
					//cout << "Blue moved to button B " << b << "\n";
				}
			} else if (colour[i] == 'B' && curr_b == b)
			{
				//cout << "Blue pushed button B " << b << " -------------- ";
				// push this button	
				bluePos.pop();
				i++;
				if (i == n) break;
				else
				{
					if (curr_o == -1) continue;
					if (curr_o > o) o++; // move 1 forward
					else if (curr_o < o) o--; // move 1 backward
					else { } // wait here itself
					//cout << "Orange moved to button O " << o << "\n";
				}
			} else 
			{
				if (curr_o != -1)
				{
					if (curr_o > o) o++;
					else if (curr_o < o) o--;
					//cout << "Orange moved to button O " << o << "\n";
				}
				if (curr_b != -1)
				{
					if (curr_b > b) b++;
					else if (curr_b < b) b--;
					//cout << "Blue moved to button B " << b << "\n";
				}
			}
		}	
		cout << "Case #" << T << ": " <<  sec << "\n";			
	}
}
