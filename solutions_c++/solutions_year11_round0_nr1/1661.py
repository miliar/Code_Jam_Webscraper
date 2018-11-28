
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

ifstream inFile;
ofstream outFile;

int o_b[100];
int b_b[100];

int shortest_time;

vector<string> robots;
vector<int> buttons;

int
count_time()
{
	int o_dist = 0;
	int b_dist = 0;

	int last_o_pos = 1;
	int last_b_pos = 1;

	string last_robot = robots.front();

	int num_move = 0;
	
	while (robots.size() > 0)
	{
		string r = robots.front();
		int button = buttons.front();

		if (r.compare("O") == 0)
		{
			int o_move = abs(last_o_pos - button);
			if (last_robot.compare("B") == 0)
			{
				if (b_dist <= o_move)
					o_dist = o_move - b_dist + 1;
				else
					o_dist = 1;
				//outFile << "b_dist " << b_dist << endl;
				num_move += b_dist;
			} else {
				o_dist += o_move + 1;
			}
			last_o_pos = button;
		}
		if (r.compare("B") == 0){
			int b_move = abs(last_b_pos - button);
			if (last_robot.compare("O") == 0)
			{
				if (o_dist <= b_move)
					b_dist = b_move - o_dist + 1;
				else
					b_dist = 1;
				//outFile << "o_dist " << o_dist << endl;
				num_move += o_dist;
			} else {
				b_dist += b_move + 1;
			}
			last_b_pos = button;
		}
		last_robot = r;
		robots.erase(robots.begin());
		buttons.erase(buttons.begin());
	}
	if (last_robot.compare("O") == 0)
		num_move += o_dist;
	else
		num_move += b_dist;
	
	return num_move;
}

int
main()
{
	inFile.open("input.txt");
	outFile.open("output.txt");

	int num_cases;
	inFile >> num_cases;

	int num_button;
	int temp_num;
	string tmp_str;
	for (int curr_case = 0 ; curr_case < num_cases ; curr_case++)
	{
		memset(o_b, 0, sizeof(o_b));
		memset(b_b, 0, sizeof(b_b));

		int olb = 0;
		int blb = 0;
		shortest_time = 0;
		inFile >> num_button;
		for (int i = 0 ; i < num_button ; i++)
		{
			inFile >> tmp_str;
			inFile >> temp_num;
			
			robots.push_back(tmp_str);
			buttons.push_back(temp_num);
		}
		int result = count_time();
		outFile << "Case #" << curr_case + 1 << ": " << result << endl;
	}

	return 0;
}

