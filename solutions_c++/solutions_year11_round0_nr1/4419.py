#include <iostream>
#include <fstream>

using namespace std;

unsigned int solve(const unsigned int size, const char* robot, const unsigned int* pos);
unsigned int max(unsigned int a, unsigned int b);
unsigned int absdiff(unsigned int a, unsigned int b);

int main(/*int argc, char** argv*/) {
	char** robot = NULL;
	unsigned int** pos = NULL;
	unsigned int T = 0;
	
	cin >> T;
	robot = new char*[T];
	pos = new unsigned int*[T];
	for(unsigned int i=0;i<T;++i) {
		unsigned int nSteps;
		char c;

		cin >> nSteps;
		robot[i] = new char[nSteps];
		pos[i] = new unsigned int[nSteps];
		for (unsigned int j=0;j<nSteps;++j) {
			cin >> c;
			while (c == ' ') cin >> c;
			robot[i][j] = c;
			cin >> pos[i][j];
		}
		
		unsigned int nSeconds = solve(nSteps,robot[i],pos[i]);
		cout << "Case #" << (i+1) << ": " << nSeconds << endl;
	}
	
	for (unsigned int i=0;i<T;++i) {
		delete[] robot[i]; robot[i] = NULL;
		delete[] pos[i]; pos[i] = NULL;
	}
	delete robot; robot = NULL;
	delete pos; pos = NULL;
	
	return 0;
}

unsigned int max(unsigned int a, unsigned int b) {
	return (a>b)?a:b;
}

unsigned int absdiff(unsigned int a, unsigned int b) {
	return (a>b)?a-b:b-a;
}

unsigned int solve(const unsigned int size, const char* robot, const unsigned int* pos) {
	unsigned int tO = 0;
	unsigned int tB = 0;
	
	unsigned int prevO = 1;
	unsigned int prevB = 1;
	
	for (unsigned int i=0;i<size;++i) {
		if (robot[i] == 'O') {
			tO = max(tB,tO+absdiff(pos[i],prevO))+1;
			prevO = pos[i];
		} else {
			tB = max(tO,tB+absdiff(pos[i],prevB))+1;
			prevB = pos[i];
		}
	}
	return max(tO,tB);
}
