#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

int get_number_of_intersections(int **heights, int N) {
	int count = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (heights[i][0] < heights[j][0] && heights[i][1] > heights[j][1]) {
				count++;
			}
		}
	}

	return count;

}

int main() {
	int T = 0;
	int N;
	string line;
	//ifstream myfile("example.txt");
	//ifstream myfile("A-small-attempt0.in");
	ifstream myfile("A-large.in");
	//ofstream out_file("A-small-attempt0.out");
	ofstream out_file("A-large.out");
	myfile >> T;
	int count = 0;
	while (count < T) {
		myfile >> N;
		int **heights = new int*[N];
		if (heights != NULL) {
			for (int i = 0; i < N; i++) {
				heights[i] = new int[2];
			}
		}

		for (int i = 0; i < N; i++) {
			myfile >> heights[i][0];
			myfile >> heights[i][1];
		}
		int res = get_number_of_intersections(heights, N);

		//cout << "CASE #" << (count + 1) << ": " << res << endl;
		out_file << "Case #" << (count + 1) << ": " << res << endl;
		count++;
	}
	return 0;
}
