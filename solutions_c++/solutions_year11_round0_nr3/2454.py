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
	cout << N << " num cases" << endl;

	for( int n = 0; n < N; n++ ) {
		int numCandy;
		fin >> numCandy;

		int xor = 0;
		long long sum = 0;
		int smallest = 0;

		for( int i = 0; i < numCandy; i++) {
			int candyValue;
			fin >> candyValue;

			if (smallest == 0 || candyValue < smallest)
				smallest = candyValue;

			xor ^= candyValue;
			sum += candyValue;
		}
			
		cout << "Case #" << n+1 << ": ";
		fout << "Case #" << n+1 << ": ";
		
		if (xor == 0)
		{
			cout << (sum-smallest) << endl;
			fout << (sum-smallest) << endl;
		}
		else
		{
			cout << "NO" << endl;
			fout << "NO" << endl;
		}
	}

	return 0;
}
