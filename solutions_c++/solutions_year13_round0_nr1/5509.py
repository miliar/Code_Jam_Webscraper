#include <iostream>
#include <fstream>

using namespace std;

typedef unsigned int uint;

bool equals(char a, char b) {
	return a == 'T' || b == 'T' || a == b;
}

enum GameState {
	OWin = 'O',
	XWin = 'X',
	Draw = 1,
	NotComplete = 0
};

char test(char table[4][4], bool h) {
	bool complete = true;
	for(uint x = 0; x != 4; x++) {
		bool win = true;
		char w = table[h ? x : 0][h ? 0 : x];
		w = (w == 'T') ? table[h ? x : 1][h ? 1 : x] : w;
		if(w != '.') {
			for(uint y = 0; y != 4; y++) {
				char c = table[h ? x : y][h ? y : x];
				complete = (c == '.') ? false : complete;
				//cout<<complete<<endl;
				if(!equals(w, c)) {
					win = false;
					break;
				}
			}
			if(win) {
				return w;
			}
		} else {
			complete = false;
		}

	}
	char w = table[h ? 0 : 3][0];
	if(w != '.') {
		w = (w == 'T') ? table[h ? 1 : 2][1] : w;
		bool win = true;
		for(uint x = 0; x != 4; x++) {
			char c = table[h ? x : 3 - x][x];
			if(!equals(w, c)) {
				win = false;
				break;
			}
		}
		if(win) {
			return w;
		}
	}
	return complete;
}

int main()
{
	ifstream in;
	in.open("test.txt");

	if(!in.is_open()) {
		cerr<<"Unable to open input file"<<endl;
		return 1;
	}

	uint t = 0;
	in>>t;
	//cout<<"T = "<<t<<endl;

	for(uint i = 0; i != t; i++) {
		char table[4][4];
		for(uint j = 0; j != 4; j++) {
			in.get();
			in.read(table[j], 4);
		}
		in.get();

		/*for(uint x = 0; x != 4; x++) {
			for(uint y = 0; y != 4; y++) {
				cout<<table[x][y]<<" ";
			}
			cout<<endl;
		}*/

		char a = test(table, false);
		if(a == Draw || a == NotComplete) {
			char b = test(table, true);
			if(b != Draw && b != NotComplete) {
				a = b;
			}
		}
		cout<<"Case #"<<i + 1<<": ";
		switch(a) {
			case NotComplete:
				cout<<"Game has not completed"<<endl;
			break;
			case Draw:
				cout<<"Draw"<<endl;
			break;
			case OWin:
				cout<<"O won"<<endl;
			break;
			case XWin:
				cout<<"X won"<<endl;
			break;
			default:
				cerr<<"Error : "<<(int)a<<endl;
		}
		//cout<<endl;
	}
	return 0;
}

