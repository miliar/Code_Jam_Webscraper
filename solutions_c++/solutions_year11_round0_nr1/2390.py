#include <vector>
#include <iostream>
#include <fstream>

#include <cstdio>

using namespace std;

typedef struct _button
{
	char color;
	int number;
} Button;

typedef struct _robot
{
	int index;
	char color;
	int curr;
	int next;
	bool pushing;
} Robot;

int total_time;
char next_button;

int robot_find_next(vector<Button *> & in, Robot &r);
// return time takes to get to next button
// always return a non-negative integer
int time_to_next(int current, int next);
// return 1 if a button is pushed
int make_movement(Robot &r, vector<Button *> & in);

void init_robot(Robot &r, char color);

int main(int argc, char *argv[])
{
	ifstream fin;
	ofstream fout;
	fin.open(argv[1]);
	fout.open(argv[2]);

	int num_test_cases;
	fin >> num_test_cases;

	for(int test_cases_i = 0; test_cases_i < num_test_cases; test_cases_i++) {
		vector<Button *> input;
		{	/* read input start */
		// read input
		int num_buttons;
		fin >> num_buttons;
		char c;
		int n;
		for(int buttons_i = 0; buttons_i < num_buttons; buttons_i++) {
			fin >> c >> n;
			Button *btn = new Button;
			btn->color = c;
			btn->number = n;
			input.push_back(btn);
		}
		}	/* read input end */
		/*
		 * testing reading input - passed
		 */
		/*
		for(int i = 0; i < num_buttons; i++)
			cout << input[i]->color << input[i]->number << ' ';
		cout << '\n';
		*/
		{	/* processing start */
		 total_time = 0;
		int btn_counter = 0;
		int in_i = 0;

		Robot o, b;
		init_robot(o, 'O');
		init_robot(b, 'B');

		robot_find_next(input, o);
		robot_find_next(input, b);

		next_button = input[in_i]->color;
		while(btn_counter < input.size()) {
			total_time++;
			int tmp;
			tmp = make_movement(o, input) + make_movement(b, input);
			btn_counter += tmp;
			if (tmp) {
				in_i++;
				if (in_i < input.size()) {
					next_button = input[in_i]->color;
					//printf("at time%3d, a button is pushed, next button is %c\n", total_time, next_button);
				}
			}
		}
		printf("Case #%d: %d\n", test_cases_i+1, total_time);
		fout << "Case #" << test_cases_i+1 << ": " << total_time << endl;
		}	/* processing end */
	}

	fin.close();
	fout.close();
}

int robot_find_next(vector<Button *> & in, Robot &r)
{
	bool found = false;
	for(int i = r.index+1; i < in.size(); i++)
		if (in[i]->color == r.color) {
			r.index = i;
			r.next = in[i]->number;
			found = true;
			break;
		}
	if (!found) {
		return 0;
	}
	return 1;
}
int make_movement(Robot &r, vector<Button *> & in)
{
	//printf("time%3d\t%c go from%3d to %3d\n", total_time, r.color, r.curr, r.next);
	int res = 0;
	if (r.curr > r.next)
		r.curr--;
	else if (r.curr < r.next)
		r.curr++;
	else {
		if (next_button == r.color) {
			robot_find_next(in, r);
			res = 1;
		}
	}
	return res;
}
void init_robot(Robot &r, char color)
{
	r.index = -1;
	r.color = color;
	r.curr = 1;
	r.next = 0;
	r.pushing = false;
}