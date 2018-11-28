#include <iostream>
#include <vector>
using namespace std;

int solve(int n, vector<int> colors, vector<int> buttons)
{
	int step = 0;
	int loc[2];
	int time = 0;
	loc[0] = 1;
	loc[1] = 1;
	while (step < n) {
		int change = 0;
		
		while (loc[colors[step]] != buttons[step]) {
			if (loc[colors[step]] < buttons[step])
				loc[colors[step]]++;
			else
				loc[colors[step]]--;
			time++;
			change++;
		}

		int next = -1;
		for (int i = 1; step+i < n; i++) {
			if (colors[step+i] != colors[step]) {
				next = step+i;
				break;
			}
		}
		
		if (next != -1) {
			for (int i = 0; i < change+1; i++) {
				if (buttons[next] != loc[colors[next]]) {	
					if (loc[colors[next]] < buttons[next])
						loc[colors[next]]++;
					else
						loc[colors[next]]--;
				}
			}
		}

		time++;
		step++;
	}
	return time;
}

int main()
{
	int c;
	cin >> c;
	for (int i = 0; i < c; i++) {
		int n;
		cin >> n;
		vector<int> colors;
		vector<int> buttons;
		int result = 0;
		for (int j = 0; j < n; j++) {
			char col;
			cin >> col;
			int btn;
			cin >> btn;
			colors.push_back(col == 'O' ? 0 : 1);
			buttons.push_back(btn);
		}
		cout << "Case #" << i+1 << ": ";
		cout << solve(n, colors, buttons);
		cout << endl;
	}
}
