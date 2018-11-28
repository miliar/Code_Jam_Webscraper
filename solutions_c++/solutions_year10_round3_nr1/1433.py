#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
using namespace std;

int getIntersections(vector<pair<int,int> > &lines)
{
	int count = 0;
	for (int i = 0; i < lines.size(); i++) {
		for (int j = 0; j < lines.size(); j++) {
			if (i != j) {
				if (lines[i].first < lines[j].first && lines[i].second > lines[j].second) {
					count++;
				}
			}
		}
	}
	return count;
}

int main(int argc, char **argv)
{
	vector<pair<int,int> > lines;
	int cases, lineCount;
	
	ifstream input(argv[1]);
	ofstream output(argv[2]);

	input >> cases;
	
	for (int i = 0; i < cases; i++) {
		input >> lineCount;
		lines.clear();
		pair<int,int> ab;
		for (int j = 0; j < lineCount; j++) {
			input >> ab.first >> ab.second;
			lines.push_back(ab);
		}
		output << "Case #" << i+1 << ": " << getIntersections(lines) << endl;
	}
	
	input.close();
	output.close();
	return 0;
}