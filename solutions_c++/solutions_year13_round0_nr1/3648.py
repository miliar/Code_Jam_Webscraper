#include <iostream>
#include <fstream>
#include <cstdint>

#include <vector>
#include <map>
#include <set>

using namespace std;

int main(int argc, char const *argv[])
{
	ifstream ifs(argv[1]);
	int ncases;
	ifs >> ncases;

	for (int casenum = 1; casenum < ncases+1; ++casenum) {
			uint16_t xfield=0, ofield=0;
			int nchars = 0;
			for (int i = 0; i < 16; ++i)
			{
				char c;
				ifs >> c;
				
				if(c == 'X' || c == 'T') {
					xfield |= (1<<(15-i));
				}

				if(c == 'O' || c == 'T') {
					ofield |= (1<<(15-i));
				}

				if(c == 'O' || c=='X' || c == 'T') {
					++nchars;
				}
			}

			vector<uint16_t> winning_positions { 0b1111000000000000, 0b0000111100000000, 0b0000000011110000, 0b0000000000001111, 0b1000100010001000, 0b0100010001000100, 0b0010001000100010, 0b0001000100010001, 0b1000010000100001, 0b0001001001001000};

			cout << "Case #" << casenum << ": ";

			for(auto pos : winning_positions) {
				if((pos & xfield) == pos) {
					cout << "X won" << endl;
					goto nextcase;
				}
				if((pos & ofield) == pos) {
					cout << "O won" << endl;
					goto nextcase;	
				}
			}


			if(nchars == 16) {
				cout << "Draw" << endl;
			} else {
				cout << "Game has not completed" << endl;				
			}



			nextcase: ;
	}

	return 0;
}

