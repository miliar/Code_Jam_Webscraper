#include <iostream>
#include <list>
#include <utility>
#include <map>

typedef std::list<std::pair<char, int> > Orders;

std::pair<char, int> next_move(Orders orders, char robot) {
	char current = 'N';
	std::pair<char, int> ret = std::pair<char, int>(current, -1);
	for(Orders::iterator it = orders.begin(); it != orders.end(); ++it) {
		current = it->first;
		if(current == robot) {
			ret.first = current;
			ret.second = it->second;
			break;
		}
	}
	return ret;
}

char other_robot(char robot) {
	return robot == 'O' ? 'B': 'O';
}

int moves(Orders orders) {
	// Robot positions
	std::map<char, int> robots;
	robots['O'] = 1;
	robots['B'] = 1;
	
	// time count
	int count = 0;

	// move the "other" robot should be preparing
	std::pair<char, int> next = next_move(orders, other_robot(orders.front().first));
	
	while(!orders.empty()) {
		char first = orders.front().first;
		char other = other_robot(first);
		int objective = orders.front().second;

		// if we found a move for the other robot
		if(next.first == other) {
			if(next.second > robots[other]) {
				robots[other]++;
				//std::cout << other << " Move to button " << robots[other] << " ";
			} else if(next.second < robots[other]) {
				robots[other]--;
				//std::cout << other << " Move to button " << robots[other] << " ";
			} else {
				//std::cout << other << " Stay at button " << robots[other] << " ";
			}
		} else {
			//std::cout << other << " Stay at button " << robots[other] << " ";
		}

		// Robot who should act first
		if(objective > robots[first]) {
			robots[first]++;
			//std::cout << first << " Move to button " << robots[first] << std::endl;
		} else if(objective < robots[first]) {
			robots[first]--;
			//std::cout << first << " Move to button " << robots[first] << std::endl;
		} else {
			//std::cout << first << " Push button " << objective << std::endl;
			orders.pop_front();
			// Has the next robot changed?
			if(orders.front().first != first) {
				next = next_move(orders, first);
			}
		}


		count++;
	}
	return count;
}

int main(void) {
	int lines;
	std::cin >> lines;

	for(int cases = 0; cases < lines; ++cases) {
		std::list<std::pair<char, int> > orders;
		int steps;
		std::cin >> steps;
		for(int step = 0; step < steps; ++step) {
			char robot;
			int k;
			std::cin >> robot;
			std::cin >> k;
			orders.push_back(std::pair<char, int>(robot, k));
		}

		std::cout << "Case #" << cases+1 << ": " << moves(orders) << std::endl;
	}


	return 0;
}
