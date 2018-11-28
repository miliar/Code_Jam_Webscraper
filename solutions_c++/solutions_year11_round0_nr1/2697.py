#include <iostream>
#include <fstream>
using namespace std;

#define N (100)

class Bot {
public:
	int position, BTC[N], BTCC, count;
	bool myChance, clicked, finished;
	Bot(){
		position = 1;
		BTCC = 0;
		count = 0;
		myChance = false;
		finished = false;
		clicked = false;
	}
	void makeMove(void);
	
	void setCount(int i);
};


void Bot::setCount(int i) {
	if (i == 0) {
		finished = true;
		
	}
	count = i;
}

void Bot::makeMove(void) {
	if (position < BTC[BTCC]) {
		clicked = false;
		position++;
	} else if (position > BTC[BTCC]) {
		clicked = false;
		position--;
	} else {
		if (myChance) {
			BTCC++;
			clicked = true;
		}
		if (BTCC == count) {
			finished = true;
		}
	}
	
}


int numOfSeconds = 0;

int main (int argc, char * const argv[]) {
	ifstream input(argv[1]);
	ofstream output("output.txt");
	int cases, buttons_num;
	input >> cases;
	char bot; int button;
	char *chances; int chancesCount = 0;
	for (int i = 0; i < cases; i++) {
		Bot orange, blue;
		chancesCount = 0;
		input >> buttons_num;
		chances = new char[buttons_num];
		for (int j = 0; j < buttons_num; j++) {
			input >> bot >> button;
			chances[chancesCount++] = bot;
			switch (bot) {
				case 'O':
				{
					orange.BTC[orange.BTCC++] = button;
				}
					break;
					
				case 'B':
				{
					blue.BTC[blue.BTCC++] = button;
				}
			}
		}
		chancesCount = 0;
		orange.setCount(orange.BTCC);
		blue.setCount(blue.BTCC);
		orange.BTCC = blue.BTCC = 0;
		bool finished = false;
		while (!finished) {
			numOfSeconds++;
			if (chances[chancesCount] == 'O') {
				orange.myChance = true;
				blue.myChance = false;
				orange.makeMove();
				blue.makeMove();
				if (orange.clicked) {
					chancesCount++;
				}
			} else {
				orange.myChance = false;
				blue.myChance = true;
				orange.makeMove();
				blue.makeMove();
				if (blue.clicked) {
					chancesCount++;
				}
			}
			finished = (orange.finished && blue.finished);
		}
		output << "Case #" << i+1 << ": " << numOfSeconds << endl;
		delete []chances;
		numOfSeconds = 0;
	}
	return 0;
}
