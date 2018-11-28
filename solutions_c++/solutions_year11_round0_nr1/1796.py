//#include <boost/thread/thread.hpp>
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <assert.h>

using namespace std;

struct Task
{
	char name;
	int pos;
	Task(char name, int pos) : name(name), pos(pos){}
};

typedef vector<Task> Tasks;

struct Robot
{
	const Tasks &tasks;
	char name;
	int task, pos;
	bool just_pressed;

	Robot(char name, const Tasks &tasks) : name(name), tasks(tasks), task(-1), pos(1), just_pressed(false){ task = find_new_task(); }
	bool Robot::has_task() const { return task < INT_MAX; }
	void update(const Robot &other_robot);
private:
	int find_new_task()
	{
		task++;
		for (; task < int(tasks.size()); task++)
			if (tasks[task].name == name)
				return task;
		return INT_MAX;	
	}

	void move() { assert(!in_place() && has_task()); pos = tasks[task].pos < pos ? pos -1 : pos+1; }
	void wait(){};
	void press(){ task = find_new_task(); just_pressed = true; }
	bool in_place() const { return tasks[task].pos == pos; }
};


void Robot::update(const Robot &other_robot)
{
	if (!has_task())
		return;

//	if (has_task())
	{
		if (!in_place())
			move();
		else
			if (other_robot.task < task || other_robot.just_pressed)
				wait();
			else
				press();
		return;
	}
}

void main()
{
	ifstream f;
	f.open("in.txt");
	if (f.fail())
	{
		cout << "cannot open file" << endl;
		return;
	}

	int cases = 0;
	f >> cases;
	for (int _case=1; _case<=cases; _case++)
	{
		int tasks_count = 0;
		f >> tasks_count;
		Tasks tasks;
		for (int i=0; i<tasks_count; i++)
		{
			char ch;
			int pos;
			f >> ch;
			f >> pos;
			tasks.push_back(Task(ch, pos));
		}

		int time = 0;
		Robot o('O', tasks), b('B', tasks); // init task -1
		while (o.has_task() || b.has_task())
		{
			o.just_pressed = false;
			b.just_pressed = false;
			o.update(b);
			b.update(o);

			time++;
		}

		cout << "Case #" << _case << ": " << time << endl;
	}
}
