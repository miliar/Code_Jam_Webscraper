#include <string>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

struct Robot {
	int position;
	int timeLastMove;
};

struct Command {
	char robot;
	int pos;
};


int testCase( const vector<Command>& commands ) {
	Robot o,b;
	o.position = 1;
	o.timeLastMove = 0;

	b.position = 1;
	b.timeLastMove = 0;

	int time = 0;

	for (vector<Command>::const_iterator it = commands.begin(); it != commands.end(); ++it) {
		const Command & c = *it;

		Robot * r;
		if (c.robot == 'O') {
			r = &o;
		} else {
			r = &b;
		}

		int timeToMove = abs(c.pos - r->position);

		int timeAfterMove = max(r->timeLastMove + timeToMove, time);

		time = timeAfterMove + 1;
		r->timeLastMove = time;
		r->position = c.pos;
	}

	return time;
}

int main(int argc, char** argv) {
	
	ifstream fin;

	string filename = "a.in";

	if (argc > 1) {
		filename = argv[1];
	}

	fin.open(filename, ios_base::in);

	int T;

	fin >> T;

	for (int i = 0; i < T; i++) {
		vector<Command> v;
		Command c;

		int N;
		int Pi;
		char Ri;

		fin >> N;
		for (int j = 0; j < N; j++) {
			fin >> Ri >> Pi;

			c.robot = Ri;
			c.pos = Pi;

			v.push_back(c);	
		}

		int result = testCase(v);
		cout << "Case #" << (i+1) << ": "<< result << endl;
	}

	//cin.get();

	return 0;

	

/*	c.pos = 2;
	c.robot = 'o';
	v.push_back( c );

	c.pos = 1;
	c.robot = 'b';
	v.push_back( c );

	c.pos = 2;
	c.robot = 'b';
	v.push_back( c );

	c.pos = 4;
	c.robot = 'o';
	v.push_back( c );

	int result = testCase(v);

	cout << result << endl;
	*/
	return 0;
}