#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main () {
	ifstream myfile;
	myfile.open("B-large.in");
	ofstream outfile;
	outfile.open("B-large.out");
	string cases;
	getline(myfile,cases);
	int t = atoi(cases.c_str());

	string googlers;
	int n;
	string surprising;
	int s;
	string atleast;
	int p;
	int scores[100] = {0x00};
	for(int j = 0; j < t; j++) {
		
		cout << "Case #" << j+1 << ":";
		outfile << "Case #" << j+1 << ":";
		
		getline(myfile,googlers, ' ');
		n = atoi(googlers.c_str());
		getline(myfile, surprising, ' ');
		s = atoi(surprising.c_str());
		getline(myfile, atleast, ' ');
		p = atoi(atleast.c_str());

		int i = 0;
		string score;
		while(i < n-1){
			getline(myfile, score, ' ');
			scores[i] = atoi(score.c_str());
			i++;
		}
		getline(myfile,score);
		scores[i] = atoi(score.c_str());
		i++;

		int possible = 0;
		for(int k = 0; k < i; k++) {
			if(s > 0) {
				/*int sc = scores[k];
				if((sc - (p+p-4)) == p ){possible++; s--; if(j==2) cout << "what"; }
				else if((sc - (p+p-4)) > p){possible++; if(j==2) cout <<"who";}*/
				if(scores[k] > (p-1)*3) {possible++; }
				else if((p!=1 && p!= 0) && (scores[k] == 3*p-3 || scores[k] == 3*p-4)){possible++; s--;}
				else if(p==1){if(scores[k] > 0) possible++;}
				else if(p==0){possible++;}
			}
			else {
				if(scores[k] > (p-1)*3) {possible++;}
			}
		}
		cout << " " << possible << endl;
		outfile << " " << possible << endl;
		memset(scores, 0x00, 30);
	}
	
	myfile.close();
	outfile.close();
	return 0;
}
