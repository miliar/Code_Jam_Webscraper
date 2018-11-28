#include <iostream>
#include <sstream>
#include <fstream>
#include <ostream>
#include <string>
#include <vector>
using namespace std;

struct need_pressed_buton
{
	int robot_type;
	int sequence_number;
	int button_index;
};


struct Robot{
	int curr_index;
	int processed_button_count;
	vector<need_pressed_buton> list;	
};




int main()
{
	vector<need_pressed_buton> list_buttons;
	ifstream input;
	ofstream output;
	string filename = "A-large.in";
	input.open(filename.c_str());
	output.open("Output.out");
	if (input.fail())
	{
		cout << "Wrong input" << endl;
	}
	int i = 0;
	string line;
	getline(input,line);
	int number_of_test_cases = atoi(line.c_str());
	int sequence;
	for (int i = 0; i < number_of_test_cases; i++)
	{
		list_buttons.clear();
		int global_time = 0;
		sequence = 0;
		getline(input,line);
		istringstream iss(line);
		string val;
		iss >> val;
		int number_of_buttons = atoi(val.c_str());
		for (int j = 0; j < number_of_buttons;j++)
		{
			iss>>val;
			if (val == "O")
			{
				need_pressed_buton tmp;
				tmp.robot_type = 0;
				tmp.sequence_number = sequence++;
				iss >> val;
				tmp.button_index = atoi(val.c_str());
				list_buttons.push_back(tmp);
			}
			else if(val == "B")
			{
				need_pressed_buton tmp;
				tmp.robot_type = 1;
				tmp.sequence_number = sequence++;
				iss >> val;
				tmp.button_index = atoi(val.c_str());
				list_buttons.push_back(tmp);
			}
		}
		Robot orange, blue;
		orange.curr_index = 1;
		orange.processed_button_count = 0;
		blue.curr_index = 1;
		blue.processed_button_count = 0;
		for (int z = 0; z < number_of_buttons; z++)
		{
			//cout << list_buttons.at(z).robot_type << " " << list_buttons.at(z).button_index << " " << list_buttons.at(z).sequence_number << endl;
			if (list_buttons.at(z).robot_type == 0)
			{
				orange.list.push_back(list_buttons.at(z));
			} 
			else
			{
				blue.list.push_back(list_buttons.at(z));
			}
		}
		for (int z = 0; z < orange.list.size();z++)
		{
			cout << orange.list.at(z).robot_type << " " << orange.list.at(z).button_index << " " << orange.list.at(z).sequence_number << endl;
		}
		for (int z = 0; z < blue.list.size();z++)
		{
			cout << blue.list.at(z).robot_type << " " << blue.list.at(z).button_index << " " << blue.list.at(z).sequence_number << endl;
		}

		bool orange_done = false;
		if (orange.list.size() == 0)
		{
			orange_done = true;
		}
		bool blue_done = false;
		if (blue.list.size() == 0)
		{
			blue_done = true;
		}
		for (int z = 0; z < number_of_buttons;)
		{
			bool button_pressed = false;
			global_time++;
			if (!orange_done && orange.list.at(orange.processed_button_count).button_index == orange.curr_index)
			{
				if (orange.list.at(orange.processed_button_count).sequence_number == z)
				{
					orange.processed_button_count++;
					button_pressed = true;
					if (orange.processed_button_count == orange.list.size())
					{
						orange_done = true;
					}
				}
			}
			else
			{
				if (!orange_done && orange.list.at(orange.processed_button_count).button_index > orange.curr_index)
				{
					orange.curr_index++;
				}
				else
				{
					orange.curr_index--;
				}

			}

			if (!blue_done && blue.list.at(blue.processed_button_count).button_index == blue.curr_index)
			{
				if (blue.list.at(blue.processed_button_count).sequence_number == z)
				{
					blue.processed_button_count++;
					button_pressed = true;
					if (blue.processed_button_count == blue.list.size())
					{
						blue_done = true;
					}
				}
			}
			else
			{
				if (!blue_done && blue.list.at(blue.processed_button_count).button_index > blue.curr_index)
				{
					blue.curr_index++;
				}
				else
				{
					blue.curr_index--;
				}
			}
			if (button_pressed)
			{
				z++;
			}
		}
		output << "Case #" << i + 1 << ": " << global_time << endl;
		cout << "\n\n\n\n Global Time:" << global_time << endl;

	}
	return 0;
}