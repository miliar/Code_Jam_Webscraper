#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <map>
#include <cstring>
#include <set>
#include <sstream>
#include <cstdlib>
using namespace std;

static const size_t npos = -1;


int main()
{
	ifstream fin;
	fin.open ("input.txt");

	ofstream fout;
	fout.open ("output.txt");

	int N; // num test cases
	fin >> N;
	cout << N << " num cases" << endl;

	for( int n = 0; n < N; n++ ) {
		int orangePos = 1;
		int orangeTime = 0;
		int bluePos = 1;
		int blueTime = 0;

		int totalTime = 0;

		int numButtons;
		fin >> numButtons;

		for( int i = 0; i < numButtons; i++ ) {
			string color;
			int button;

			fin >> color;
			fin >> button;

			if( color[0] == 'O' ) {
				int timeForOrange = abs(orangePos-button) + orangeTime + 1;
				if( timeForOrange <= totalTime )
					totalTime++;
				else
					totalTime = timeForOrange;
				orangeTime = totalTime;
				orangePos = button;
			}
			else {
				int timeForBlue = abs(bluePos-button) + blueTime + 1;
				if( timeForBlue <= totalTime )
					totalTime++;
				else
					totalTime = timeForBlue;
				blueTime = totalTime;
				bluePos = button;
			}
		}
			
		cout << "Case #" << n+1 << ": " << totalTime << endl;
		fout << "Case #" << n+1 << ": " << totalTime << endl;
	}

	return 0;
}
