	// one hundred buttons [1, 100]
	// button k is k meters from start
	// begin at button 1

	// execute a sequence of things as fast as possible!
	// always move to the next button to press then wait for your turn

	// OK!

	// First, convert the instructions into the following format:

	// Stack of destinations for each robot
	// A global "whose turn is it?" stack

	// Then, each time step move towards your destination...
	// UNLESS you are already at your destination...
	// In which case you wait.
	
	// AND if you are at your destination AND its your turn, PRESS YOUR BUTTON! (and then remove the fact that its your turn and get your next destination)

#include <queue>
#include <string>

#include <fstream>
#include <sstream>
#include <iostream>

using namespace std;



int main(int argc, char* argv[]) {

	queue<char> robot_order;
	queue<int> blue_destinations, orange_destinations;
	
	int steps_taken;

	int blue_location, blue_destination;
	int orange_location, orange_destination;

	// UGH, IO TIME
	// For each test case, read in the number of moves (or discard it, who cares)
	// Then, mow through and add the robot name to robot_order...
	// And the robot destination to orange_destinations or blue_destinations, respectively

	// THEN RUN THE ACTUAL PROGRAM

	fstream input_file(argv[1]);
	int num_test_cases;
	input_file >> num_test_cases;	
	
	string guuuh;
	getline(input_file, guuuh);

	for (int i = 0; i < num_test_cases; ++i) {

		string s;	
		getline(input_file, s);
		stringstream current_line(s);

		int who_cares;
		current_line >> who_cares;	
	
		char robot_name;
		int  robot_destination;

		//while (current_line) {
		while (current_line >> robot_name && current_line >> robot_destination) {

			robot_order.push(robot_name);

			if (robot_name == 'O')
				orange_destinations.push(robot_destination);
			else
				blue_destinations.push(robot_destination);
				
		}	

		// ACTUAL PROGRAM STARTS HERE

		steps_taken = 0;

		blue_location = 1;
		blue_destination = blue_destinations.front();

		orange_location = 1;
		orange_destination = orange_destinations.front();

		while (robot_order.empty() != true) {

			char current_turn = robot_order.front();

			// Blue, go!
			if (current_turn == 'B' && blue_location == blue_destination) {

				robot_order.pop();
				blue_destinations.pop();			// OH SHIT WHAT IF THERE ARENT ANY LEFT?
		
				if (blue_destinations.empty() != true)	
					blue_destination = blue_destinations.front();
				else
					blue_destination = blue_location;	// Wait for the game to end...
							
			}	
			else {
		
				if (blue_location < blue_destination)
					blue_location++;
				else if (blue_location > blue_destination)
					blue_location--;

			}

			// Orange, go!
			if (current_turn == 'O' && orange_location == orange_destination) {

				robot_order.pop();
				orange_destinations.pop();
		
				if (orange_destinations.empty() != true)	
					orange_destination = orange_destinations.front();
				else
					orange_destination = orange_location;	// Wait for the game to end...
							
			}	
			else {
		
				if (orange_location < orange_destination)
					orange_location++;
				else if (orange_location > orange_destination)
					orange_location--;

			}

			steps_taken++;

		}

		cout << "Case #" << (i +1) << ": " << steps_taken << endl;	

	}

	return 0;

}
