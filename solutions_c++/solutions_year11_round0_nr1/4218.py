#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>

typedef std::pair<char,int> task_t;

int solve(const std::vector<task_t>& tasks)
{	
	std::deque<task_t> orange_tasks;
	std::deque<task_t> blue_tasks;
	
	for (std::vector<task_t>::const_iterator it = tasks.begin(); it != tasks.end(); ++it) {
		if (it->first == 'B') {
			blue_tasks.push_back(*it);
		}
		else if (it->first == 'O') {
			orange_tasks.push_back(*it);
		}
	}
	
	std::vector<task_t>::const_iterator current_task = tasks.begin();
	std::deque<task_t>::iterator orange_task = orange_tasks.begin();
	std::deque<task_t>::iterator blue_task = blue_tasks.begin();
	
	// O, B
	int robots[2] = {1, 1};
	
	int time = 0;
	while (current_task != tasks.end()) {
		int& robot_pos = robots[current_task->first != 'O'];
		int& other_robot_pos = robots[current_task->first == 'O'];
		int task_time = std::abs(robot_pos - current_task->second) + 1;
		robot_pos = current_task->second;
		time += task_time;
		
		int other_robot_next = 0;
		std::vector<task_t>::const_iterator next_task = current_task + 1;
		if (next_task != tasks.end()) {
			if (current_task->first != 'O') {
				other_robot_next = orange_task != orange_tasks.end() ? orange_task->second : 0;
			}
			else {
				other_robot_next = blue_task != blue_tasks.end() ? blue_task->second : 0;
			}
		}
		if (other_robot_next) {
			if (task_time >= std::abs(other_robot_pos - other_robot_next)) {
				other_robot_pos = other_robot_next;
			}
			else {
				if (other_robot_pos - other_robot_next > 0)
					other_robot_pos -= task_time;
				else
					other_robot_pos += task_time;
			}
		}
		if (current_task->first == 'O') {
			++orange_task;
		}
		else {
			++blue_task;
		}
		++current_task;
	}
	
	return time;
}

int main(int argc, char **argv) 
{
    int T;
	
	std::cin >> T;
	
	for (int i=0; i<T; ++i) {
		int N;
		std::cin >> N;
		
		std::vector<task_t> tasks;
		for (int j=0; j<N; ++j) {
			char color;
			int button;
			std::cin >> color >> button;
			tasks.push_back(task_t(color, button));
		}
		int answer = solve(tasks);
		std::cout << "Case #" << i+1 << ": " << answer << std::endl;
	}
	
	return 0;
}
