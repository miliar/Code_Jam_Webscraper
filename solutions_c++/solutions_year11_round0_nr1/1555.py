#include <iostream>
#include <vector>
#include <fstream>
#include <stdlib.h>

using namespace std;

int solve(vector<int> &colors, vector<int> positions){
	int lastPos[2] = {1, 1};
	int lastTime[2] = {0, 0};
	int currentTime = 0;
	for (int i = 0; i < colors.size(); i++){
		int addedTime = abs(lastPos[colors[i]] - positions[i]) - (currentTime - lastTime[colors[i]]);
		addedTime = (addedTime > 0)?addedTime:0;
		currentTime += (addedTime + 1);
		lastPos[colors[i]] = positions[i];
		lastTime[colors[i]] = currentTime;
	}
	return currentTime;
}

int main(int argc, char *argv[]){
	if (argc != 2){
		cerr << "Error: " << argv[0] << " file" << endl;
		exit(-1);
	}
	ifstream file(argv[1]);
	if (!file.is_open()){
		cerr << "Error: file " << argv[0] << " could not be opened" << endl;
	}
	int T;
	file >> T;
	for (int i = 0; i < T; i++){
		vector<int> colors;
		vector<int> positions;
		int N;
		file >> N;
		for (int j = 0; j < N; j++){
			char color;
			int colorIndex;
			file >> color;
			if (color == 'B'){
				colorIndex = 0;
			} else {
				colorIndex = 1;
			}
			int position;
			file >> position;
			colors.push_back(colorIndex);
			positions.push_back(position);
		}
		int solution = solve(colors, positions);
		cout << "Case #" << (i+1) << ": " << solution << endl;
	}
}
