#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <set>
#include <map>
#include <algorithm>

#define PB push_back
#define MP make_pair

using namespace std;

int main () {
	int cases;
	cin >> cases;
	for(int case_i = 1; case_i <= cases; case_i++){
		int height; int width;
		cin >> height; cin >> width;
		
		char** space;
		space = new char*[height];
		for(int i = 0; i < height; i++) space[i] = new char[width];
		
		for(int i = 0; i < height; i++)
			for (int j = 0; j < width; j++) {
				cin >> space[i][j];
			}
		for(int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				if(j >= width - 1 || i >= height - 1) {
					continue;
				}
				if(space[i][j] == '#' && space[i][j+1] == '#' && space[i+1][j] == '#' && space[i+1][j+1] == '#' ){
					space[i][j] = '/';
					space[i][j+1] = '\\';
					space[i+1][j] = '\\';
					space[i+1][j+1] = '/';
				}
			}
		}
		bool pos = true;
		for(int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				if (space[i][j] == '#') {
					pos = false;
				}
			}
		}
		
		cout << "Case #" << case_i << ":" << endl;
		if(pos)
			for(int i = 0; i < height; i++) {
				for (int j = 0; j < width; j++) {
					cout << space[i][j];
				}
				cout << endl;
			}
		else{
			cout << "Impossible";
			cout << endl;
		}
		for(int i = 0; i < height; i++) delete(space[i]);
		delete(space);

	}
    return 0;
}
