#include <fstream>

using namespace std;

int main (int argc, char* argv[])
{
	ifstream in("A-large.in");
	//ifstream in("A-small-attempt2.in");
	//ifstream in("A-small-practice.in");
	ofstream out("out.txt");
	if (in.is_open() && out.is_open())
	{
		int case_count;
		in >> case_count;
		for(int i = 0; i < case_count; ++i)
		{
			int actions_count = 0,
				total_time = 0,
				o_time = 0,
				b_time = 0,
				button_num,
				prev_button_num[2] = {1, 1},
				robot_time[2] = {0, 0};
			bool robot_index = false;
			char curr_robot,
				 prev_robot;

			in >> actions_count;
			in >> curr_robot;
			in >> button_num;
			total_time = abs(button_num - prev_button_num[robot_index]) + 1;
			prev_robot = curr_robot;
			prev_button_num[robot_index] = button_num;
			robot_time[robot_index] = total_time;
			for (int j = 0; j < actions_count - 1; ++j)
			{
				in >> curr_robot;
				in >> button_num;

				if (curr_robot == prev_robot)
				{
					robot_time[robot_index] += abs(button_num - prev_button_num[robot_index]) + 1;
					total_time += abs(button_num - prev_button_num[robot_index]) + 1;
					prev_button_num[robot_index] = button_num;
				} 
				else 
				{
					robot_time[!robot_index] = abs(button_num - prev_button_num[!robot_index]) + 1;
					if (robot_time[!robot_index] > robot_time[robot_index]) {
						robot_time[!robot_index] -= robot_time[robot_index];
						total_time += robot_time[!robot_index];						
					} else {
						robot_time[!robot_index] = 1;
						++total_time;
					}
					robot_time[robot_index] = 0;
					robot_index = !robot_index;
					prev_button_num[robot_index] = button_num;
					prev_robot = curr_robot;
				}
			}
			out << "Case #" << i + 1 << ": " << total_time << '\n';
		}
	}

	in.close();
	out.close();
	return 0;
}