#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

int main() {
	int N;
	
	ifstream fin("a.in");
	ofstream fout("a.out");
	
	
	fin >> N;
	
	for(int n = 1; n <= N; n++) {
		int capKeys, numKeys, numLetters;
		
		fin >> numKeys >> capKeys >> numLetters;
		
		vector<int> freq(numLetters, 0);
		
		for(int i = 0; i < numLetters; i++) {
			fin >> freq[i];
		}
		sort(freq.begin(), freq.end(), greater<int>());
		
		unsigned long long int totalPresses = 0, pressesPerLetter = 0;
		
		for(int i = 0; i < numLetters; i++) {
			if(i % capKeys == 0) pressesPerLetter++;
			totalPresses += freq[i] * pressesPerLetter;
		}
		
		fout << "Case #" << n << ": " << totalPresses << endl;
	}
}
