#include <iostream>
#include <string>
#include <vector>

using namespace std;

int N, K;
vector<string> table;

void gravity() {
	for(vector<string>::iterator i = table.begin(); i != table.end(); i++) {
		int p = N;
		for(int j=N-1; j>=0; j--) {
			char c = i->at(j);
			i->at(j) = '.';
			if(c != '.')
				i->at(--p) = c;
		}
	}
}

string count() {
	int dx[4] = {0, 1, 1, 1};
	int dy[4] = {1, 0, 1, -1};
	bool red = false, blue = false;
	for(int x=0; x<N; x++)
		for(int y=0; y<N; y++) {
			if(table.at(x).at(y) == '.')
				continue;
			for(int d=0; d<4; d++) {
				int x1=x, y1=y;
				bool yes = true;
				for(int step=0; step<K; step++) {
					if(x1<0 || x1>=N || y1<0 || y1>=N || table.at(x1).at(y1) != table.at(x).at(y)) {
						yes = false;
						break;
					}
					x1 += dx[d];
					y1 += dy[d];
				}
				if(yes)
					switch(table.at(x).at(y)) {
					case 'R': red = true; break;
					case 'B': blue = true; break;
					}
			}
		}
	if(red)
		if(blue)
			return "Both";
		else
			return "Red";
	else
		if(blue)
			return "Blue";
		else
			return "Neither";
}

int main(int argc, char* argv) {
	int T;
	cin >>T;
	for(int i=0; i<T; i++) {
		cin >>N >>K;
		table.clear();
		for(int j=0; j<N; j++) {
			string s;
			cin >>s;
			table.push_back(s);
		}
		gravity();
		cout <<"Case #" <<i+1 <<": " <<count() <<endl;
	}
	return 0;
}
