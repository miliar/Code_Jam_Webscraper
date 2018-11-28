#include<iostream>
#include<fstream>
#include<stdint.h>

using namespace std;

int main(int argc, char ** argv) {
    //read
    ifstream file(argv[1]);
    ofstream ofile("output.txt");
    int numT;
    file>>numT;

    //pattern
    uint16_t pattern[] = {0xf000, 0x0f00, 0x00f0, 0x000f, 
	                0x8888, 0x4444, 0x2222, 0x1111,
			0x8421, 0x1248};

    for(int i=0; i<numT; i++) {
	string aline;
	uint16_t board_x = 0x0000;
	uint16_t board_o = 0x0000;
	bool dot = false;
	for(size_t k=0; k<4; k++) {
	    file >> aline;
	    for(size_t j=0; j<4; j++)
		if(aline[j] == 'X') {
		    board_x |= (1<<(k*4+j));
		} else if(aline[j] == 'O') {
		    board_o |= (1<<(k*4+j));
		} else if(aline[j] == 'T') {
		    board_x |= (1<<(k*4+j));
		    board_o |= (1<<(k*4+j));
		} else {dot = true;}
	}

	ofile<<"Case #"<<(i+1)<<": ";

	bool x_won = false;
	for(size_t j=0; j<10; j++) {
	    x_won |= ((board_x&pattern[j]) == pattern[j]);
	}

	if(x_won) {
	    ofile<<"X won"<<endl;
	    continue;
	}

	bool o_won = false;
	for(size_t j=0; j<10; j++) {
	    o_won |= ((board_o&pattern[j]) == pattern[j]);
	}

	if(o_won) {
	    ofile<<"O won"<<endl;
	    continue;
	}
	
	if(dot) {
	    ofile<<"Game has not completed"<<endl;
	} else {
	    ofile<<"Draw"<<endl;
	}

    }
    return 0;
}
