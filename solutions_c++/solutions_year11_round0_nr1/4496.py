#include <iostream>
#include <fstream>
#include <cmath>
#include <string>

#define filename "blah.in"

using namespace std;

void openFile(ifstream& , ofstream&, int& cases);
int calculateTime(bool, int, int&);

int main(){

	ifstream fin;
	ofstream fout;
	int cases;
	int buttons;
	int curposO = 1, curposB = 1;
	bool curGoal; //false = blue, true = orange
	int curButton;
	int totalTime = 0;
	int runningTime = 0;
	int tempTime = 0;
	string curReadColor;

	openFile(fin, fout, cases);
	//cout << cases;

	for(int i = 0; i < cases; i++){
		fin >> buttons;
		//cout << endl << buttons;
		for(int j = 0; j < buttons; j++){
			fin >> curReadColor >> curButton;
			//cout << " " << curReadColor << " " << curButton;
			if(j !=0 && ((curReadColor == "O" && curGoal == false) ||(curReadColor == "B" && curGoal == true))){
				if(curReadColor == "O"){
					curGoal = true;
					tempTime = calculateTime(curGoal, curButton, curposO);
				}else{
					curGoal = false;
					tempTime = calculateTime(curGoal, curButton, curposB);
				}
				tempTime = tempTime - runningTime;
				if(tempTime < 0){
					runningTime = 1;
					totalTime += 1;
				}else{
					runningTime = tempTime + 1;
					totalTime += (tempTime + 1);
				}
			}else{
				if(curReadColor == "O"){
					curGoal = true;
					tempTime = calculateTime(curGoal, curButton, curposO);
				}else{
					curGoal = false;
					tempTime = calculateTime(curGoal, curButton, curposB);
				}
				totalTime  += (1+tempTime);
				runningTime  += (1+tempTime);
			}
		}
		//write to ouput file totaltime and set it back to 0...
		fout << "Case #" << (i+1) << ": " << totalTime << endl;
		totalTime = 0;
		runningTime = 0;
		tempTime = 0;
		curposO = 1;
		curposB = 1;
	}



	fin.close();
	fout.close();

	return 0;
}


void openFile(ifstream& fin, ofstream& fout, int& cases){

	fin.open(filename);
	fout.open("output.txt");

	fin >> cases;


}

int calculateTime(bool curGoal, int curButton, int& curpos){
	int temptime = abs(curButton - curpos);
	curpos = curButton;
	return temptime;
}
