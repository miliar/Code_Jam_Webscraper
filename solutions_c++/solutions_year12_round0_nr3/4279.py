#include <iostream>
#include <string.h>
#include <string>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

bool canrotate(string N, string M){
	//go through N for the number of rotations possible,
	//if it ever equals M then return true
	int NUMROTATIONS = N.size();
	string::iterator iter;
	for (int i = 0; i < NUMROTATIONS;i++){
		if (N == M){
			return true;
		}
		else{
			//rotate, move the back element to the front
			//get a copy of the front character
			//erase the front character
			//append it to the back
			char temp = N[0];
			N.erase(N.begin() + 0);
			N.push_back(temp);
		}
	}


}


int main(){
	int rounds = 0;
	int lowerbound,upperbound;
	string N;
	string M;
	char buffer[30];
	char buffer2[30];
	int swaps = 0;
	cin >> rounds;

	for (int game = 0; game < rounds; game++){
		swaps = 0; //new game reset the counter
		cin >> lowerbound >> upperbound;

		for (int i = lowerbound; i < upperbound ;i++){
			itoa(i,buffer,10);
			for (int j = i + 1;(j <= upperbound);j++){
				itoa(j,buffer2,10);
				if (canrotate(buffer,buffer2)){
				//	cout << i << " " << j << endl;
					swaps++;
				}
			}

		}
		cout << "Case #" << game + 1  << ": " << swaps << endl;
	}

}
