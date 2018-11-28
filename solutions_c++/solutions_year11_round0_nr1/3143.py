#include<iostream>
#include<queue>
#include<cstdlib>

using namespace std;

struct button {
	int pos;
	char color;
};

int solve() {
	int nm; cin >> nm;
	queue<button> buttons;
	
	for (int i = 0; i < nm; i++) {
		button b;
		cin >> b.color >> b.pos;
		buttons.push(b);
	}

	int p_b = 1;
	int p_o = 1;

	int t_b = 0;
	int t_o = 0;

	while (!buttons.empty()) {
		button b = buttons.front();
		if (b.color == 'B') {
			t_b += abs(p_b - b.pos);
			p_b = b.pos;
			t_b = max(t_o, t_b);
			t_b++; buttons.pop();
		} else {
			t_o += abs(p_o - b.pos);
			p_o = b.pos;
			t_o = max(t_o, t_b);
			t_o++; buttons.pop();
		}
	}


	return max(t_o, t_b);
}

int main() {
	int tc; cin >> tc;

	for (int t = 1; t <= tc; t++) cout << "Case #" << t << ": " << solve() << endl;

	return 0;
}
