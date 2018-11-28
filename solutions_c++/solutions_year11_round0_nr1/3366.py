#include<fstream>
#include<iostream>
#include<math.h>
using namespace std;

int main(){
	ofstream fout("bot.out");
	ifstream fin ("bot.in");
	int test;
	int num;
	char bot;
	int n;
	int totTime;
	int currOTime;
	int currBTime;
	int currOLoc;
	int currBLoc;
	bool isO=false;
	fin >> test;
	for (int i=1;i<test+1;i++) {
		fin >> n;
		totTime = 0;
		currOTime = 0;
		currBTime = 0;
		currOLoc = 1;
		currBLoc = 1;
		for (int j=0;j<n;j++) {
			fin >> bot >> num;
			if (bot == 'O') {
				int time = abs(num-currOLoc);
				if(isO == false) {
					if(totTime - currOTime > 0)
							time -= totTime - currOTime;
					if(time < 0)
						time = 0;
				}
				time++;
				currOLoc = num;
				totTime += time;
				currOTime = totTime;
				isO = true;
			}
			else { //(bot == 'B') {
				int time = abs(num-currBLoc);
				if(isO == true) {
					if(totTime - currBTime > 0)
							time -= totTime - currBTime;
					if(time < 0)
						time = 0;
				}
				time++;
				currBLoc = num;
				totTime += time;
				currBTime = totTime;
				isO = false;
			}
		}
		fout << "Case #" << i << ": " << totTime << "\n";
	}
}