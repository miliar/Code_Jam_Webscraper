#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int read(int x){
	int numGooglers = 0;
	cin >> numGooglers;
	int numSurp = 0;
	cin >> numSurp;
	int p = 0;
	cin >> p;
	int counter = 0;
	for( int i = 0; i < numGooglers; i++ ){
		int score = 0;
		cin >> score;
		if( score  - p < 0 ){}
		else if( score - p >= 2*(p-1) ){
			 counter++;
		}
		else if( score - p >= 2*(p-2) && numSurp > 0 ){
			 numSurp--;
			 counter++;
		}
	}
	return counter;
}
int main(){
	int numSets = 0;
	cin >> numSets;
	getchar();
	for( int i = 0; i < numSets; i++ ){
		cout << "Case #" << i+1 << ": " << read(i+1) << endl;
	}
	return 0;
}
