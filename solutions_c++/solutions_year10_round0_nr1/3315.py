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


int main()
{
	ifstream fin;
	fin.open ("input.txt");

	ofstream fout;
	fout.open ("output.txt");

	int N; // num test cases
	fin >> N;

	for( int n = 0; n < N; n++ ) {
		int snappers;
		long snaps;
		long onState;
		string answer;

		fin >> snappers >> snaps;

		onState = (1 << snappers)-1;
		
		if( (snaps & onState) == onState ) {
			answer = "ON";
		}
		else {
			answer = "OFF";
		}

		cout << "Case #" << n+1 << ": " << answer << endl;
		fout << "Case #" << n+1 << ": " << answer << endl;
	}

	return 0;
}
