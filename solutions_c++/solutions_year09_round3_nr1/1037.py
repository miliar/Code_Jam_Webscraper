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
#include <cmath>
using namespace std;

ifstream fin;

ofstream fout;

int main()
{
	fin.open ("example.txt");
	fout.open ("output.txt");

	int N;
	fin >> N;

	for( int i = 0; i < N; i++ ) {
		long long num = 0;
		long long base;
		string word;
		fin >> word;

		char chArr[36] = {};
		int noArr[36] = {};
		int count = 0;
		for( int j = 0; j < word.length(); j++ ) {
			bool found = false;
			char ch = word[j];
			for( int k = 0; k < count; k++ ) {
				if( chArr[k] == ch )
					found = true;
			}

			if(!found) {
				chArr[count++] = ch;
			}
		}
		noArr[0] = 1;
		noArr[1] = 0;
		for( int j = 2; j < count; j++ ) {
			noArr[j] = j;
		}

		if( count == 1 ) {
			count = 2;
		}
		for( int j = 0; j < word.length(); j++ ) {
			long double hi = count;
			int yo = word.length()-1-j;
			long double exp = pow(hi,yo);
			base = exp;
			int index = -1;
			for( int k = 0; index < 0; k++ ) {
				if( chArr[k] == word[j] ) {
					index = k;
				}
			}
			//cout << index << endl;
			num += base * noArr[index];
		}
		
		cout << "Case #" << i+1 << ": " << num << endl;
		fout << "Case #" << i+1 << ": " << num << endl;
	}

	return 0;
}
