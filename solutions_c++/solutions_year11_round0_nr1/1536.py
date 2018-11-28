#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

int main (int argc, char * const argv[]) {
    //ifstream in("..//..//sample.in.txt");
	//ifstream in("..//..//A-small-attempt0.in.txt");
	ifstream in("..//..//A-large.in.txt");
	
	if (!in) {
		cout << "Input file cannot be opened";
		return 1;
	}
	
	ofstream out("output.txt");
	if (!out) {
		cout << "Output file cannot be opened";
		in.close();
		return 1;
	}
	
	int T;
	in >> T;
	
	
	
	for (int t = 0; t < T; t++) {
		int N;
		in >> N;
		char color[N];
		int numButton[N];
		
		for (int n = 0; n < N; n++) {
			in >> color[n] >> numButton[n];
		}
		
		char lastColorMoved = ' ';
		int durationFromOtherMoved = 0;
		int totalTime = 0;
		
		int blueCurrent = 1;
		int orangeCurrent = 1;
		
		for (int n = 0; n < N; n++) {
			int distanceTravelled = 0;
			int timeOverlapped = 0;
			
			if (lastColorMoved != color[n])
			{
				lastColorMoved = color[n];
				timeOverlapped = durationFromOtherMoved;
				durationFromOtherMoved = 0;
			}
			
			if (color[n] == 'B') {
				distanceTravelled = abs(numButton[n] - blueCurrent);
				blueCurrent = numButton[n];
			}
			else {
				distanceTravelled = abs(numButton[n] - orangeCurrent);
				orangeCurrent = numButton[n];				
			}
			
			int timeConsumed = distanceTravelled + 1 - timeOverlapped;
			if (timeConsumed < 1)
				timeConsumed = 1;
			durationFromOtherMoved += timeConsumed;
			
			totalTime += timeConsumed;
		}
		
		cout << "Case #" << (t + 1) << ": " << totalTime << endl;
		out << "Case #" << (t + 1) << ": " << totalTime << endl;
	}
	
	in.close();
	out.close();
	
    return 0;
}
