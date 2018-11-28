#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

struct list_pair
{
	int x;
	int y;
	list_pair* next;
	list_pair* prev;
	list_pair* first;
};

struct list_int
{
	int i;
	list_int* next;
	list_int* prev;
	list_int* first;
};

int main(int argc, char* argv[])
{
	char buffer[1024];

	if(argc < 3)
	{
		cout << "provide input and output file names" << endl;
		exit(1);
	}
	
	string ifname(argv[1]);
	string ofname(argv[2]);

	ifstream input_file(ifname.c_str());
	if( input_file.bad() || !input_file.is_open() )
	{
		cout << "failed opening the input file" << endl;
		exit(2);
	}
	ofstream output_file(ofname.c_str());
	if( output_file.bad() || !output_file.is_open() )
	{
		cout << "failed opening the output file" << endl;
		exit(3);
	}


	int T=0;
	int N=0;
	
	list_pair* robots_intervals[2];
	robots_intervals[0] = 0;
	robots_intervals[1] = 0;
	list_int* robots_order = 0;

	input_file >> T;
	input_file.getline(buffer, 1024); //skip newline char

	char robot = 0;
	int robot_index = 0;
	int robot_button= 0;

	for ( int test_case=1; test_case<=T; test_case++ )
	{
		robots_intervals[0] = 0;
		robots_intervals[1] = 0;
		robots_order = 0;

		input_file.getline(buffer, 1024);

		istringstream istream(buffer);

		istream >> N;

		for ( int button_count=0;button_count<N;button_count++ )
		{
			istream >> robot;
			istream >> robot_button;

			if ( robot == 'B' )
				robot_index = 0;
			else
			if ( robot == 'O' )
				robot_index = 1;
			else
			{
				cout << "not good! error reading input" << endl;
				exit(4);
			}
			
			if ( robots_intervals[robot_index] == 0 )
			{
				robots_intervals[robot_index] = new (nothrow) list_pair();
				if ( robots_intervals[robot_index] == 0 )
				{
					cout << "not good! no memory" << endl;
					exit(5);
				}
				robots_intervals[robot_index]->first = robots_intervals[robot_index];
				robots_intervals[robot_index]->next = robots_intervals[robot_index]->prev = 0;
				robots_intervals[robot_index]->x = robot_button;
				robots_intervals[robot_index]->y = robot_button;
			}
			else
			{
				robots_intervals[robot_index]->next = new (nothrow) list_pair();
				if ( robots_intervals[robot_index]->next == 0 )
				{
					cout << "not good! no memory" << endl;
					exit(6);
				}
				robots_intervals[robot_index]->next->prev=robots_intervals[robot_index];
				robots_intervals[robot_index]->next->next = 0;
				robots_intervals[robot_index]->next->first=robots_intervals[robot_index]->first;
				robots_intervals[robot_index]=robots_intervals[robot_index]->next;
				robots_intervals[robot_index]->x = robot_button;
				robots_intervals[robot_index]->y = abs(robots_intervals[robot_index]->x - robots_intervals[robot_index]->prev->x);
			}
			

			if ( robots_order == 0 )
			{
				robots_order = new (nothrow) list_int();
				if ( robots_order == 0 )
				{
					cout << "not good! no memory" << endl;
					exit(7);
				}
				robots_order->first = robots_order;
				robots_order->next = robots_order->prev = 0;
			}
			else
			{
				robots_order->next = new (nothrow) list_int();
				if ( robots_order->next == 0 )
				{
					cout << "not good! no memory" << endl;
					exit(8);
				}
				robots_order->next->prev = robots_order;
				robots_order->next->next = 0;
				robots_order->next->first= robots_order->first;
				robots_order=robots_order->next;
			}
			robots_order->i = robot_index;
		} // end of for ( int button_count=0;button_count<N;button_count++ )
		if ( robots_intervals[0] != 0 )
			robots_intervals[0]=robots_intervals[0]->first;
		if ( robots_intervals[1] != 0 )
			robots_intervals[1]=robots_intervals[1]->first;
		robots_order=robots_order->first;
		
		int current_robot = 0;
		int current_times [2];
		current_times[0]=current_times[1]=0;
		while ( robots_order != 0 )
		{
			int current_robot = robots_order->i;
			int other_robot = (current_robot+1) % 2;

			current_times[current_robot] += robots_intervals[current_robot]->y;
			if ( current_times[current_robot] >= current_times[other_robot] )
				current_times[current_robot]++;
			else
				current_times[current_robot] = current_times[other_robot]+1;

			if ( robots_intervals[current_robot]->next == 0 )
			{
				delete robots_intervals[current_robot];
				robots_intervals[current_robot] = 0;
			}
			else
			{
				robots_intervals[current_robot]=robots_intervals[current_robot]->next;
				delete robots_intervals[current_robot]->prev;
			}
				

			if ( robots_order->next == 0 )
			{
				delete robots_order;
				robots_order = 0;
			}
			else
			{
				robots_order = robots_order->next;
				delete robots_order->prev;
			}
		}
		
		int found_time = (current_times[1]>current_times[0])?current_times[1]:current_times[0];
		found_time--;
		//cout << "Case #" << test_case << ": " << found_time << endl;
		output_file << "Case #" << test_case << ": " << found_time << endl;
	} // for ( int test_case=1; test_case<=T; test_case++ )

	//cout << "done" << endl;
	return 0;
}
