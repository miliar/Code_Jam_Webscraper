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

	long groups[1000];

	for( int n = 0; n < N; n++ ) {
		long runs;
		long people;
		int numGroups;
		int qFront = 0;
		long answer = 0;

		fin >> runs >> people >> numGroups;

		for( int i = 0; i < numGroups; i++ ) {
			fin >> groups[i];
		}

		for( long i = 0; i < runs; i++ ) {
			long size = 0;
			int start = qFront;
			while( size + groups[qFront] <= people ) {
				size += groups[qFront];
				qFront = (qFront+1)%numGroups;
				if( qFront == start ) break;
			}
			answer += size;
		}

		cout << "Case #" << n+1 << ": " << answer << endl;
		fout << "Case #" << n+1 << ": " << answer << endl;
	}

	return 0;
}
