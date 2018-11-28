// Train Timetable.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>
#include "stdafx.h"

using namespace std;

typedef struct {
	int deph;
	int depm;
	int arrh;
	int arrm;
} deptime;

int _tmain(int argc, _TCHAR* argv[])
{
	int numCases, caseIter;
	int iter;
	ifstream fin;
	fin.open("C:\\B-large.in", ifstream::in);
	fin>>numCases;
	int t;
	int na, nb;
	deptime input;
	vector<deptime> AB;
	vector<deptime> BA;
	int hour, minute, done, redo;
	int startA, startB;
	int numA, numB;
	for(caseIter=1; caseIter <= numCases; caseIter++) {
		fin >> t;
		fin >> na >> nb;
		AB.resize(0);
		BA.resize(0);
		for(iter = 1; iter <= na; iter++) {
			fin >> input.deph;
			fin.ignore(255, ':');
			fin >> input.depm;
			fin.ignore(255, ' ');
			fin >> input.arrh;
			fin.ignore(255, ':');
			fin >> input.arrm;
			if((input.arrm + t) >= 60) {
				input.arrh += (input.arrm + t)/60;
				input.arrm = (input.arrm + t) % 60;
			}
			else {
				input.arrm += t;
			}
			AB.push_back(input);
		}
		for(iter = 1; iter <= nb; iter++) {
			fin >> input.deph;
			fin.ignore(255, ':');
			fin >> input.depm;
			fin.ignore(255, ' ');
			fin >> input.arrh;
			fin.ignore(255, ':');
			fin >> input.arrm;
			if((input.arrm + t) >= 60) {
				input.arrh += (input.arrm + t)/60;
				input.arrm = (input.arrm + t) % 60;
			}
			else {
				input.arrm += t;
			}
			BA.push_back(input);
		}
		done = 0;
		startA = 0;
		startB = 0;
		redo = 0;
		while(!done) {
			numA = startA;
			numB = startB;
			redo = 0;
			for(hour = 0; hour < 24; hour++) {
				for(minute = 0; minute < 60; minute++) {
					//schedule arrivals
					for(iter = 0; iter < BA.size(); iter++) {
						if(minute == BA[iter].arrm && hour == BA[iter].arrh) {
							numA++;
						}				
					}
					for(iter = 0; iter < AB.size(); iter++) {
						if(minute == AB[iter].arrm && hour == AB[iter].arrh) {
							numB++;
						}				
					}
					//schedule departures
					for(iter = 0; iter < AB.size(); iter++) {
						if(minute == AB[iter].depm && hour == AB[iter].deph) {
							if(numA == 0) {
								startA++;
								redo = 1;
							}
							else {
								numA--;
							}
						}				
					}
					for(iter = 0; iter < BA.size(); iter++) {
						if(minute == BA[iter].depm && hour == BA[iter].deph) {
							if(numB == 0) {
								startB++;
								redo = 1;
							}else {
								numB--;
							}
						}				
					}
					if(redo) break;
				}
				if(redo)break;
			}
			if(redo)continue;
			done = 1;
		}
		cout << "Case #" << caseIter << ": " << startA << " " << startB << "\n";
	}
	return 0;
}

