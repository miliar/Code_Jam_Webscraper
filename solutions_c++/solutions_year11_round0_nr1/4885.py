#include <iostream>
#include <vector>
#include <cstdlib>
#include <cstdio>

using namespace std;

const char ORANGE = 'O';
const char BLUE = 'B';

int blPos;
int blEt;
int orPos;
int orEt;

int curTime;

void botTrust(vector<int> * buttonPos, vector<char> * buttonRobot){
	blPos = 1;
    blEt = 0;
    orPos = 1;
    orEt = 0;
    curTime = 0;
	
	for (int i = 0; i < buttonPos->size(); i++){
		int targetPos = (*buttonPos)[i];
		if ((*buttonRobot)[i] == ORANGE){
		    int deltaPos = (targetPos - orPos);
		    deltaPos =  deltaPos >= 0 ? deltaPos : -deltaPos;
			int walkTime = (deltaPos - orEt);

			if (walkTime < 0)
				walkTime = 0;

			orEt = 0;		
			orPos = targetPos;
			
			int consumedTime = 1 + walkTime;
			blEt += consumedTime;
			curTime += consumedTime;
		} else {
		    int deltaPos = (targetPos - blPos);
		    deltaPos =  deltaPos >= 0 ? deltaPos : -deltaPos;
			int walkTime = (deltaPos - blEt);	

			if (walkTime < 0)
				walkTime = 0;

            blEt = 0;		
			blPos = targetPos;	
			
			int consumedTime = 1 + walkTime;
			orEt += consumedTime;
			curTime += consumedTime;
		}	
	}
}

int main(){
	int testCases;
	cin >> testCases;
    cin.ignore(100, '\n');
    
	for (int testCase = 1; testCase <= testCases; testCase++){
		vector<int> * buttonPos = new vector<int>;
		vector<char> * buttonRobot = new vector<char>;
		
		int buttonCount;
		cin >> buttonCount;
                
        for (int i = 0; i < buttonCount; i++){
            int pos;
            char robot;
            
            cin.ignore(10, ' ');
            cin >> robot;
            cin >> pos;
            
            buttonPos->push_back(pos);
            buttonRobot->push_back(robot);            
        }
        
    	cin.ignore(100, '\n');	
    	
    	botTrust(buttonPos, buttonRobot);
    	
    	cout << "Case #" << testCase << ": " << curTime << endl;
    	
    	delete buttonPos;
    	delete buttonRobot;
	}

	return 0;
}

