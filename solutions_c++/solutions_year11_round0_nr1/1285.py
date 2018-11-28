#include <iostream>
using namespace std;

class Robot
{
private:
	int position;
	int personal_time;
public:
	static int time;

	Robot();
	~Robot();

	int getDistance(int position);

	int getSpareTime();

	void moveTo(int position);

	void pushButton(int button);

	int updateTime(int amount);
};

int Robot::time = 0;

int main(int argc, char **args)
{
	int i = 0;
	cin >> i;
	for(int c=0; c < i; c++) {
		Robot a, b;
		int j = 0, p=0;
		char l;
		cin >> j;
		for(int k=0; k < j; k++) {
			cin >> l;
			cin >> p;
			switch(l) {
			case 'O':
				a.pushButton(p);
				break;
			case 'B':
				b.pushButton(p);
				break;
			}
		}
		cout << "Case #" << c+1 << ": " << Robot::time << endl;
		Robot::time = 0;
	}
	return 0;
}

Robot::Robot()
{
	this->personal_time = Robot::time;
	this->position = 1;
}
Robot::~Robot()
{
}

int Robot::getDistance(int position)
{
	return abs(this->position - position);
}

int Robot::getSpareTime()
{
	return Robot::time - this->personal_time;
}

void Robot::moveTo(int position)
{
	this->updateTime(getDistance(position));
	this->position = position;
}

void Robot::pushButton(int button)
{
	this->moveTo(button);
	this->time = Robot::time;
	this->updateTime(1);
}

int Robot::updateTime(int amount)
{
	int diff = this->getSpareTime();
	if(diff > amount) {
		this->personal_time = Robot::time;
	}
	else {
		Robot::time += amount - diff;
		this->personal_time = Robot::time;
	}
	return diff;
}
