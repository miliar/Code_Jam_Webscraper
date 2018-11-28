//============================================================================
// Name        : fff.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

int main() {


	ifstream in;
	ofstream out;
	in.open("in.ini");
	out.open("out.ini");
	int casecount;
	in>>casecount;
	for(int i=0; i<casecount; ++i){
		int googlers;
		in>>googlers;

		int surprise;
		in >> surprise;

		int maxscore;
		in >> maxscore;
		int maxcount;
		if(maxscore == 0){
			maxcount = googlers;
			for(int j=0; j<googlers; ++j){
				int score;
				in >>  score;
			}
		}else if(maxscore == 1){
			int surecount = 0;
			for(int j=0; j<googlers; ++j){
				int score;
				in >>  score;
				if(score>0)
					++surecount;
			}
			maxcount = surecount;
		}else{
			int surescore = maxscore*3-2;
			int notsurescore = maxscore*3-4;
			//cout << "surescore " << surescore <<endl;
			int surecount = 0;
			int unsurecount = 0;
			for(int j=0; j<googlers; ++j){
				int score;
				in >>  score;
				//cout << "score " << score <<endl;
				if(score>=surescore){
					++surecount;
				}else if(score>=notsurescore){
					++unsurecount;
				}
			}
			//cout << "surecount " << surecount <<endl;
			int unsurelast = unsurecount>surprise?surprise:unsurecount;
			maxcount = unsurelast + surecount;
		}
		out << "Case #" << i+1 << ": "<<maxcount << "\n";

	}
	cout << "finish"<<endl;
	return 0;
}
