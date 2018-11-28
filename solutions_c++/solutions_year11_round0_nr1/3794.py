
#include<iostream>
#include<algorithm>
using namespace std;

int
main()
{
	int steps, pos[2], coins[2];
	int ncases; cin >> ncases;
	for (int i = 0; i < ncases; i++) {
		pos[0] = pos[1] = 1;
		coins[0] = coins[1] = 0;
		steps = 0;
		int nbuttons; cin >> nbuttons;
		for (int j = 0; j < nbuttons; j++) {
			char c; cin >> c;
			int bot = (c == 'O')? 0: 1;
			int button; cin >> button;
			int exec = max(button, pos[bot]) - min(button, pos[bot]) + 1;
			if (exec > coins[bot]) {
				exec -= coins[bot];
				coins[bot] = 0;
				coins[1 - bot] += exec;
				steps += exec;
			} else {
				coins[bot] = 0;
				coins[1 - bot] = 1;
				steps++;
			}
			pos[bot] = button;
		}
		cout << "Case #" << i + 1 << ": " << steps << endl;
	}
}
