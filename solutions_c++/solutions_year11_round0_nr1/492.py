// a.exe < int.txt > out.txt

#include <iostream>
#include <list>
#include <utility>

enum RobotColor {
	__RC_MIN = 0,
	ORANGE = 0,
	BLUE = 1,
	__RC_COUNT = 2,
};

int main(int argc, char* argv[])
{
	int num_of_cases;
	std::cin >> num_of_cases;
	for (int case_num = 1; case_num <= num_of_cases; ++case_num) {
		int num_of_buttons;
		std::cin >> num_of_buttons;
		std::list<std::pair<RobotColor, int> > buttons_to_press;
		for (int button_num = 0; button_num < num_of_buttons; ++button_num) {
			char color_name;
			int button_index;
			std::cin >> color_name >> button_index;
			RobotColor color = (color_name == 'O' ? ORANGE  : BLUE);
			buttons_to_press.push_back(std::make_pair(color, button_index));
		}
		int seconds_passed = 0;
		int robot_position[2] = { 1, 1 };
		int is_button_pressed[2] = { false, false };
		while (!buttons_to_press.empty()) {
			if (is_button_pressed[buttons_to_press.front().first]) {
				is_button_pressed[buttons_to_press.front().first] = false;
				buttons_to_press.pop_front();
				if (buttons_to_press.empty())
					break;
			}
			for (RobotColor robot_color = __RC_MIN; robot_color != __RC_COUNT; robot_color = (RobotColor)(((int) robot_color) + 1)) {
				if (is_button_pressed[robot_color])
					continue;
				for (std::list<std::pair<RobotColor, int> >::iterator button_it = buttons_to_press.begin(); button_it != buttons_to_press.end(); ++button_it) {
					if (button_it->first == robot_color) {
						if (robot_position[robot_color] == button_it->second)
							is_button_pressed[robot_color] = true;
						else if (robot_position[robot_color] < button_it->second)
							robot_position[robot_color]++;
						else
							robot_position[robot_color]--;
						break;
					}
				}
			}
			seconds_passed++;
		}
		std::cout << "Case #" << case_num << ": " << seconds_passed << std::endl;
	}
	return 0;
}

