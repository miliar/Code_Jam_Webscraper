#include <iostream>

using namespace std;

inline int abs(int x){
	return (x>0)?x:-x;
}

int main(){
	int iCases, nCases, nMoves;
	cin >> nCases;
	
	int totalTime;
	int actTime;		// Time that the bot that needs to press the button is taking
	int oldAct;		// Last position in which the actual bot was at the start/ when it last pressed a button
	int oldOther;		// Last position in which the other bot was at the start/ when it last pressed a button
	char actBot='\0', tBot;
	int tLoc;
	for (iCases=1; iCases <= nCases; iCases++){
		cin >> nMoves;
		
		totalTime=0;
		actTime=0;
		oldOther=1;
		oldAct=1;
		
		cin >> actBot >> tLoc;
		actTime+=(tLoc-oldAct+1);
		oldAct=tLoc;
		nMoves--;
		
		while (nMoves--){
			cin >> tBot >> tLoc;
			if (tBot==actBot){
				actTime+=(abs(tLoc-oldAct)+1);
				oldAct=tLoc;
			}
			else{
				actBot=tBot;
				totalTime+=actTime;
				//cout << actTime << endl;
				
				if (abs(tLoc-oldOther)<=actTime)
					actTime=1; //time to press the button
				else
					actTime=1+abs(tLoc-oldOther)-actTime; // time to reach the button and press it
				
				oldOther=oldAct;
				oldAct=tLoc;
			}
		}
		//cout << actTime << endl;
		totalTime+=actTime;
		cout << "Case #" << iCases << ": " << totalTime << endl;
	}
	return 0;
}
