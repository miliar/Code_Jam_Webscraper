#include <iostream>
#include <fstream>
#include <list>

using namespace std;

char getTurn(list<char> &l) {
	if(!l.empty()) {
		char temp = l.front();
		l.pop_front();

		return temp;
	}

	return ' ';
}

int getButton(list<int> &l) {
	if(!l.empty()) {
		int temp = l.front();
		l.pop_front();

		return temp;
	}

	return -1;
}

int main(int argc, const char *argv[])
{
	int cases, buttons, pressed, oPos, bPos, oBut, bBut, time, temp2;
	char temp, turn;

	ifstream input;
	input.open("input.txt");

	// No error checking zzz

	input >> cases;

	list<int> o, b;
	list<char> order;

	for (int i = 0; i < cases; i++) {
		// Reset
		oPos = 1;
		bPos = 1;
		time = 0;
		pressed = 0;
		input >> buttons;
		o.clear();
		b.clear();
		order.clear();

		// Get buttons from input
		for (int j = 0; j < buttons; j++) {
			input >> temp;
			input >> temp2;

			if (temp == 'B') {
				b.push_back(temp2);
				order.push_back('B');
			}
			else {
				o.push_back(temp2);
				order.push_back('O');
			}
		}

		// Get starting buttons
		oBut = getButton(o);
		bBut = getButton(b);
		turn = getTurn(order);

		// Go
		while (pressed != buttons) {
			time++;
			temp2 = pressed;

			if (oBut != -1) {
				if (oPos == oBut && turn == 'O') { 
					pressed++;

					turn = getTurn(order);
					oBut = getButton(o);
				}
				else if (oPos < oBut) {
					oPos++;
				}
				else if (oPos > oBut) {
					oPos--;
				}
			}

			if (bBut != -1) {
				if (bPos == bBut && turn == 'B' && temp2 == pressed) { 
					pressed++;

					turn = getTurn(order);
					bBut = getButton(b);
				}
				else if (bPos < bBut) {
					bPos++;
				}
				else if (bPos > bBut) {
					bPos--;
				}
			}
		}
		cout << "Case #" << i+1 << ": " << time << endl;

	}

	return 0;
}
