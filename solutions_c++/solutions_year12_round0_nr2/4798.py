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
		int answer = 0;
		int numGooglers, surprising, minScore;
		fin >> numGooglers >> surprising >> minScore;

		if (minScore == 0) {
			answer = numGooglers;
			
			for(int i = 0; i < numGooglers; i++) {
				int score;
				fin >> score;
			}
		}
		else if(minScore == 1)
		{
			for(int i = 0; i < numGooglers; i++) {
				int score;
				fin >> score;
				if(score >= 1)
					answer++;
			}
		}
		else 
		{
			int totalMin = minScore + (minScore-1)*2;
			int possibleMin = minScore + (minScore-2)*2;
			int possible = 0;
			for(int i = 0; i < numGooglers; i++) {
				int score;
				fin >> score;
				if(score >= totalMin)
					answer++;
				else if(score >= possibleMin)
					possible++;
			}
			if(possible <= surprising)
				answer += possible;
			else
				answer += surprising;
		}

		cout << "Case #" << n+1 << ": " << answer << endl;
		fout << "Case #" << n+1 << ": " << answer << endl;
	}

	return 0;
}
