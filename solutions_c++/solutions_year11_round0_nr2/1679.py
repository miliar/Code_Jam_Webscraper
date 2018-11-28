#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <vector>
#include <stdlib.h>
#include <cmath>

using namespace std;
 
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)

void detect(char input[], int& currpos, char curr, char com[][3], int comsize, char opp[][2], int oppsize){
	if(currpos == 0){
		input[currpos++] = curr;
		return;
	}
	for(int i = 0; i<comsize; i++){
		if((com[i][0] == input[currpos-1] && com[i][1] == curr) ||(com[i][1] == input[currpos-1] && com[i][0] == curr)){
			currpos -=1;
			curr = com[i][2];
			detect(input, currpos, curr, com, comsize, opp, oppsize);
			return;
		}
	}
	for(int i = 0; i<oppsize; i++){
		for(int j = 0; j< currpos; j++){
			if((input[j] == opp[i][0] && curr == opp[i][1]) || (input[j] == opp[i][1] && curr == opp[i][0])){
				currpos = 0;
				return;
			}
		}
	}
	input[currpos] = curr;
	currpos = currpos +1;
}

int main(){
	int ncase = 0;
	cin >> ncase;

	for(int icase = 0; icase<ncase; icase++){

		int comsize;
		int oppsize;
		int N;

		cin >> comsize;
		char com[comsize][3];
		for(int i = 0; i<comsize; i++){
			cin >> com[i][0] >> com[i][1] >> com[i][2];
		}

		cin >> oppsize;
		char opp[oppsize][2];
		for(int i = 0; i<oppsize; i++){
			cin >> opp[i][0] >> opp[i][1];
		}

		cin >> N;
		char input[N];
		char curr;
		int currpos = 0;
		for(int i = 0; i<N; i++){
			cin >> curr;
			if(currpos == 0){
				input[currpos++] = curr;
			}
			else{
				detect(input, currpos, curr, com, comsize, opp, oppsize);
			}
		}

		cout << "Case #" << icase+1 << ": "; 
		cout << "[";
		for(int i = 0; i<currpos; i++){
			cout << input[i];
			if(i != currpos-1)
				cout << ", ";
		}
		cout << "]";	
		cout << endl;
	}


	return 0;
}
