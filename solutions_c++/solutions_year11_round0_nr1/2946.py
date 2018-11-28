#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
using namespace std;


int solveEachCase();

void main(){
	int testNum;
	cin >> testNum;
	for(int i = 0;i<testNum;i++){
		int timeEclapsed = solveEachCase();
		cout << "Case #" << i+1<<": " << timeEclapsed;
		if(i < testNum - 1)
			cout << "\n";
	}
}

static int solveEachCase(){
	int buttonNum;
	cin >> buttonNum;
	
	int* robotInd =(int*) malloc(buttonNum* sizeof(int));
	int* buttonPos = (int*) malloc(buttonNum*sizeof(int));
	for(int i = 0; i < buttonNum; i++){
		string robot;
		int buttonP;
		cin >> robot;
		//1 represent Orange robot
		//2 represent Bule robot
		if(robot.compare("O") == 0)
			robotInd[i] = 1;
		else if(robot.compare("B") ==0)
			robotInd[i] = 2;
		else
			;
		
		cin >> buttonP;
		buttonPos[i] = buttonP;

	}


	int currentOMax =1, currentOMin =1;
	int currentBMax =1, currentBMin =1; //robots O and B's current position ranges
	int timeEclapsed = 0;
	int goalFinished = 0;

	do{
		if(robotInd[goalFinished] == 1){
			if(currentOMax >= buttonPos[goalFinished] && currentOMin <=buttonPos[goalFinished]){// in O's range
				currentOMax = buttonPos[goalFinished];//reset to the button position
				currentOMin = buttonPos[goalFinished];
				currentBMax ++;
				currentBMin --;
				goalFinished ++;
			}else{
				currentOMax++;
				currentOMin--;
				currentBMax++;
				currentBMin--;
			}
		}else if(robotInd[goalFinished] == 2){
			if(currentBMax >= buttonPos[goalFinished] && currentBMin <= buttonPos[goalFinished]){
				currentBMax = buttonPos[goalFinished];
				currentBMin = buttonPos[goalFinished];
				currentOMax ++;
				currentOMin --;
				goalFinished ++;	
			}else{
				currentOMax++;
				currentOMin--;
				currentBMax++;
				currentBMin--;
			}
		}else exit(2);

		timeEclapsed ++;
	}while(goalFinished < buttonNum);
	
	return timeEclapsed;
}