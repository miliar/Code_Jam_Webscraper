#include <iostream>
#include <vector>

void move_robot(int& robot, int button) {
	if (button != -1) {
		if (button < robot) {
			--robot;
		}
		else if (button > robot) {
			++robot;
		}
	}
}

int next_button(int b, int color, const std::vector< std::pair<int,int> >& buttons) {
	while (b < buttons.size()) {
		if (buttons[b].first == color) {
			return buttons[b].second;
		}
		++b;
	}
	return -1;
}

int solve(const std::vector< std::pair<int,int> >& buttons) {
	int t = 0;
	int robot[2] = {1,1};
	int b = 0;
	while (b < buttons.size()) {
		//std::cerr << t << " " << b << " [" << robot[0] << ", " << robot[1] << "] " << next_button(b, 0, buttons) << " " << next_button(b, 1, buttons) << std::endl;
		bool pressed = false;
		for (int r = 0; r < 2; ++r) {
			if (buttons[b].first == r && buttons[b].second == robot[r]) {
				pressed = true;
			}
			else {
				move_robot(robot[r], next_button(b, r, buttons));
			}
		}
		if (pressed) {
			++b;
		}
		++t;
	}
	return t;
}

int main() {
	int T;
	std::cin >> T;
	for (int i = 0; i < T; ++i) {
		int N;
		std::cin >> N;
		std::vector< std::pair<int,int> > buttons(N);
		for (int j = 0; j < N; ++j) {
			char color;
			std::cin >> color >> buttons[j].second;
			//std::cerr << "(" << color << ")" << std::endl;
			buttons[j].first = color == 'O' ? 0 : 1;
		}
		//for (int j = 0; j < N; ++j) {
		//	std::cerr << "| " << buttons[j].first << " " << buttons[j].second << std::endl;
		//}
		std::cout << "Case #" << (i + 1) << ": " << solve(buttons) << std::endl;
	}
}
