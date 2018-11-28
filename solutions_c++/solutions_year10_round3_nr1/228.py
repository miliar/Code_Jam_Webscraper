#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <fstream>

using namespace std;

struct Wire {
	int Left;
	int Right;
};

int main() {

	ofstream myFile;
	myFile.open ("out.out");
	ifstream input("A-large.in");

	int turns;
	input >> turns;

	for (int t = 1; t <= turns; t++) {

		int N;
		input >> N;
		Wire* w = new Wire[N];
	
		int total = 0;
		for (int i = 0; i < N; i++) { input >> w[i].Left >> w[i].Right; }

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (i == j) continue;
				if (w[j].Left > w[i].Left && w[j].Right < w[i].Right) total++;
				else if (w[j].Left < w[i].Left && w[j].Right > w[i].Right) total++;
			}
		}
		cout << t << endl;
		myFile << "Case #" << t << ": " << total / 2 << endl;
	}

	

}