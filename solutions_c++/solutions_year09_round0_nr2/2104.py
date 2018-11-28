#include <vector>
#include <iostream>
using namespace std;

int T;
char least = 'a';

void receive(vector<vector<int> > &mapa, int y, int x) {
	for(int a = 0; a < y; ++a) {
		for(int b = 0; b < x; ++b) {
			cin >> mapa[a][b];
		}
	}	
}

void ouput(vector<vector<char> > &drain, int y, int x) {
	for(int a = 0; a < y; ++a) {
		for(int b = 0; b < x; ++b) {
			if (b == 0) 
				cout << drain[a][b];
			else
				cout << " " << drain[a][b];
		}
		cout << endl;
	}	
}


char get_lowest_cell(vector< vector<int> > &mapa, int a, int b, int *miny, int *minx, int limy, int limx) {
	int current_value = mapa[a][b];
	int min = current_value;
	
	if (a != 0) {
		if (mapa[a-1][b]< min) { // NORTH
	        min = mapa[a-1][b];
	        *miny = a-1;
	        *minx = b;
		}
	}
	
	if (b != 0) {
		if (mapa[a][b-1] < min) { //WEST
			min = mapa[a][b-1];
			*miny = a; *minx = b-1;
		}
	}
	
	
	if (b != limx-1) {
		if (mapa[a][b+1] < min) {// EAST 
			min = mapa[a][b+1];
			*miny = a; *minx = b+1;
		}
	}
	
	if (a != limy-1) {
		if (mapa[a+1][b] < min) { // SOUTH
			min = mapa[a+1][b];
			*miny = a+1; *minx = b;
		}
	}
	
	if (min == current_value) 
		return 0;
	else
		return 1;
}


void solve(int a, int b, vector< vector<int> > &mapa, vector< vector<char> > &drain, int limy, int limx) {
	int miny, minx;
	if (get_lowest_cell(mapa,a,b,&miny,&minx, limy, limx)) {
		// it means this is current cell is not a sink
		if (drain[miny][minx] == 0) {
			solve(miny,minx, mapa, drain, limy, limx);
		}
		drain[a][b] = drain[miny][minx];
	}
	else {
		drain[a][b] = least++;
	}
}

int main () {
	cin >> T;
	for(int i = 1; i <= T; ++i) {
		int x,y;
		cin >> y >> x;
		
		vector <vector <int>  > mapa (y, vector<int>(x));
		vector <vector <char> > drain (y, vector <char>(x,0));
		
		receive(mapa, y, x);

		for(int a = 0; a < y; ++a) {
			for(int b = 0; b < x; ++b) {
				if (drain[a][b] == 0)
					solve(a, b, mapa, drain, y, x);
			}
		}
		cout << "Case #" << i << ":" << endl;
		ouput(drain,y,x);
		least = 'a';
	}
}