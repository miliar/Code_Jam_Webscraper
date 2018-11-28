// initializing C++
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;

// declaring function prototypes
int get_variables(ifstream &iFile, int &N_buttons, class sequence &seq);
int calculate_result( int &N_candy, class sequence &seq);

class sequence
{
	public:
		vector<int> button;
		vector<int> robot;
		int current_pos_sequence;
		int pos_robot[2];
		int current_robot;
		int N;

	public:
		void set_values(int, char);
		char get_cur_robot();
		int get_cur_button();
		int get_next_button_other();
		int distance_cur_robot();
		void move_robots(int time_to_move);
};

void sequence::move_robots(int time_to_move)
{
	int other_robot = (current_robot+1)%2;
	pos_robot[current_robot] = get_cur_button();

	int direction = 1;
	int next_button_other = get_next_button_other();
	int distance_other = next_button_other - pos_robot[other_robot];
	if(distance_other < 0)
	{
		distance_other = -distance_other;
		direction = -1;
	}

	if ( distance_other < time_to_move)
	{
		pos_robot[other_robot] = next_button_other;
	}
	else
	{
		pos_robot[other_robot] = pos_robot[other_robot] + (direction * time_to_move);
	}
	current_pos_sequence++;
}

int sequence::distance_cur_robot()
{
	int current_pos = get_cur_button();
	int distance = current_pos - pos_robot[current_robot];
	if(distance<0)
		distance = -distance;

	return distance;
}

void sequence::set_values(int button_position, char robot_color)
{
	current_pos_sequence = 0;
	pos_robot[0] = pos_robot[1] = 1;
	button.push_back(button_position);
	
	int robot_number;
	if(robot_color=='O')
		robot_number = 0;
	else
		robot_number = 1;

	robot.push_back(robot_color);
}

char sequence::get_cur_robot()
{
	return robot[current_pos_sequence];
}

int sequence::get_cur_button()
{
	current_robot = robot[current_pos_sequence];
	return button[current_pos_sequence];
}

int sequence::get_next_button_other()
{
	int cur_color = get_cur_robot(); //0 - Orange
	int search = current_pos_sequence;
	while ( robot[search] == cur_color)
	{
		search++;
		if(search >= N)
			return -1;
	}
	return button[search];
}

int main ()
{
	int no_test_cases;
	ifstream iFile("input.txt");        // input.txt has integers, one per line
	ofstream oFile("output.txt");

	//Acquire initial variables
	iFile >> no_test_cases ;

	for(int i=0; i<no_test_cases ; i++)
	{
		class sequence seq;
		int N_buttons;

		get_variables(iFile,  N_buttons, seq);

		int result;
		result = calculate_result(N_buttons, seq);


		//unsigned __int64 result;
		//vector<int> boards_size;
		//vector<int> boards_count;

		//cout << "Case #" << i+1 << ": " << result << endl;
		oFile << "Case #" << i+1 << ": " << result << endl;
	}

	//cin.ignore( 80, '\n' );
	return 0;
}

int calculate_result( int &N_buttons, sequence &seq)
{
	int result=0;

	for( int i=0; i<N_buttons; i++)
	{
		int time_to_move = seq.distance_cur_robot();
		seq.move_robots(time_to_move+1);
		result += time_to_move+1;
	}
	return result;
}


int get_variables(ifstream &iFile, int &N_buttons, class sequence &seq)
{
	iFile >> N_buttons;
	seq.N = N_buttons;
	for( int k =0; k < N_buttons; k++ )
	{
		char color;
		char robot;
		int button_position;

		iFile >> color;
		iFile >> button_position;

		if(color=='O')
			robot = 0;
		else
			robot = 1;

		seq.set_values(button_position, robot);

	}

	return 0;
}
