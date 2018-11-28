#include <iostream>
#include <vector>
using namespace std;

enum winner {xx, oo, draw, none};

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		vector < vector <char> > in(4, vector <char> (4,'.'));
		winner win = none;
        bool f = true;
		for (int j = 0; j < 4; ++j) {
			int x = 0, o = 0;
			for (int k = 0; k < 4; ++k) {
				char a;
				cin >> a;
				in[j][k] = a;
				if (a == 'X') ++x;
				else if (a == 'O') ++o;
				else if (a == 'T') {
					++x;
					++o;
				}
                else if (a == '.') f = false; 
			}
			if (o == 4) win = oo;
			else if (x == 4) win = xx;
            else if (f) win = draw;
        }
        if (win == none || win == draw) {
            //vertical
            for (int j = 0; j < 4; ++j) {
                int x = 0, o = 0;
		        for (int k = 0; k < 4; ++k) {
        			if (in[k][j] == 'X') ++x;
    				else if (in[k][j] == 'O') ++o;
    				else if (in[k][j] == 'T') {
    					++x;
    					++o;
    			    }
		        }
                if (o == 4) win = oo;
                else if (x == 4) win = xx;
            }
        }
            
        if (win == none || win == draw) {
            //diagonal
            int x1 = 0, o1 = 0, x2 = 0, o2 = 0;
            for (int j = 0; j < 4; ++j) {
                if (in[j][j] == 'X') ++x1;
    			else if (in[j][j] == 'O') ++o1;
				else if (in[j][j] == 'T') {
					++x1;
					++o1;
			    }
                
                if (in[3-j][j] == 'X') ++x2;
        		else if (in[3-j][j] == 'O') ++o2;
				else if (in[3-j][j] == 'T') {
					++x2;
					++o2;
			    }
                if (o1 == 4 || o2 == 4) win = oo;
	            else if (x1 == 4 || x2 == 4) win = xx;
                
            }  
        }                

		cout << "Case #" << i+1 << ": ";
		if (win == xx) cout << "X won";
		else if (win == oo) cout << "O won";
		else if (win == draw) cout << "Draw";
		else if (win == none) cout << "Game has not completed";

		cout << endl;
	}
} 