#include <cmath>

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream input_file("../input");

	int num_tests;
	input_file >> num_tests;

	for (int i = 1; i <= num_tests; i++)
	{
		int num_buttons;
		char robot;
		int next_button;

		int position_o = 1;
		int position_b = 1;

		int time_o = 0;
		int time_b = 0;

		int output = 0;
		int time_to_move;

		input_file >> num_buttons;
		for (int j = 0; j < num_buttons; j++)
		{
			input_file >> robot >> next_button;
			switch (robot) {
			case 'O':
				time_to_move = abs(next_button - position_o);
				time_o += time_to_move + 1;
				if (time_o <= time_b)
					time_o = time_b + 1;
				output = time_o;
				position_o = next_button;
				break;
			case 'B':
				time_to_move = abs(next_button - position_b);
				time_b += time_to_move + 1;
				if (time_b <= time_o)
					time_b = time_o + 1;
				output = time_b;
				position_b = next_button;
				break;
			}
		}
		cout << "Case #" << i << ": " << output << endl;
	}

	input_file.close();
	return 0;
}
