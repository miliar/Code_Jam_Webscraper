#include <fstream>
#include <iostream>
#include <exception>
#include <queue> 

using namespace std;

static const bool DEBUG = false;


class Robot {
	bool move(int destination){
		if (position != destination)
		{
			if (DEBUG)
				cout << name << " move from " << position;

			if (position < destination)
				position++;
			else
				position--;

			if (DEBUG)
				cout << " to " << position << endl;

			return true;
		}
		else {
			if (DEBUG)
				cout << name << " stay at " << position << endl;
			return false;
		}
	}

	bool push(int destination){
		if (position == destination) {
			if (DEBUG)
				cout << name << " pushed " << position << endl;
			
			return true;
		}else
			return false;
	}

	int getPosition(){
		return position;
	}
	

	int position;
	char name;

	std::queue<int> commandQueue;

	public:

	Robot(char name):name(name),position(1) {
	}

	void addToCommandQueue(int position) {
		commandQueue.push(position);
	}

	bool move() {
		return move(commandQueue.front());
	}

	bool push() {
		if (push(commandQueue.front())) {
			commandQueue.pop();
			return true;
		}else
			return false;		
	}
};

typedef std::pair<Robot*,int> qitem;

int solve(fstream& in) {
	int items = 0;
	in >> items;

	Robot rb('B'),ro('O');

	std::queue<qitem> q;

	for (int i=0;i<items;++i) {
		char crobot = 0;
		in >> crobot;

		Robot* robot = NULL;

		if (crobot == 'B')
			robot = &rb;
		else if (crobot == 'O')
			robot = &ro;
		else {
			cerr << "Unknown Robot: " << crobot << endl;
			return -1;
		}

		int dest = 0;
		in >> dest;


		q.push(qitem(robot,dest));
		robot->addToCommandQueue(dest);
	}


	int secs = 0;

	while (!q.empty()) {
		secs++;
		if (DEBUG)
			cout << endl << "_______" << endl << "Sekunde: " << secs << endl;

		qitem i = q.front();

		Robot* r = i.first;
		int dest = i.second;

		if (r->push())
			q.pop();
		else
			r->move();		
		
		if (r == &rb)
			ro.move();
		else if (r == &ro)
			rb.move();
	}

	return secs;
}

int main(int argc, char** argv){
	fstream in;
    in.open(argv[1], ios::in);

	ofstream out;
	out.open(argv[2]);

	int caseCount = 0;

	in >> caseCount;

	for (int i=1;i<=caseCount;++i) {
		out << "Case #" << i << ": " << solve(in) << endl;
	}	

	return 0;
}

