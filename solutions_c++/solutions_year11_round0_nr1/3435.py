#include <iostream>
#include <fstream>
#include <queue>
using namespace std;

bool take_turn(queue<int> main, queue<int> second, 
		int& loc_main, int& loc_second);

int main()
{
	ifstream input;
	input.open("bot_trust.in");
	ofstream output;
	output.open("bot_trust.out");
	int cases;
	input >> cases;
	for(int i = 1; i <= cases; i++) {
		int buttons;
		queue<int> orange;
		queue<int> blue;
		queue<char> order;

		input >> buttons;
		char color;
		int temp;
		for(int j = 0; j < buttons; j++) {
			input >> color >> temp;
			order.push(color);
			if(color == 'O') {
				orange.push(temp);
			} else {
				blue.push(temp);
			}
		}

		int time = 0;
		int orange_loc = 1;
		int blue_loc = 1;

		while(!order.empty()) {

			time++;

			cout << "time = " << time << "\norange location/goal: "
			     << orange_loc << '/' << orange.front() << 
			     "\nblue location/goal: " << blue_loc << '/' << 
			     blue.front() << endl;

			if(order.front() == 'O') {
				if(take_turn(orange, blue, orange_loc, 
				   blue_loc)) {
					order.pop();
					orange.pop();
				}
			} else {
				if(take_turn(blue, orange, blue_loc,
				   orange_loc)) {
					order.pop();
					blue.pop();
				}
			}
		}

		output << "Case #" << i << ": " << time << endl;
	}
	
	return 1;
}


bool take_turn(queue<int> main, queue<int> second, int& loc_main, int& loc_second)
{
	if(main.empty())
		throw new int;
	if (!second.empty() && second.front() > loc_second)
		loc_second++;
	else if (!main.empty() && second.front() < loc_second)
		loc_second--;
	if (main.front() > loc_main)
		loc_main++;
	else if (main.front() < loc_main)
		loc_main--;
	else
		return true;
	return false;
}
