#include <iostream>
#include <vector>
using namespace std;

int totalTime = 0;

void increaseTime(string color){
  totalTime++;
  //cout << "increase " << color << endl;
}

int runTestCase(int totalButtons, char bc[], int bp[]){
  bool buttonPressed[100];
  totalTime = 0;
  int orangePos = 1;
  int bluePos = 1;
  int orangeBuffer = 0;
  int blueBuffer = 0;
  int numButton = 0;
  char lastColor;

  while(!buttonPressed[totalButtons-1]){
    if(bc[numButton]=='O'){
      int moves = abs(bp[numButton] - orangePos);
      //Move Orange Robot
      while(moves>0){\
        if(orangeBuffer>0) orangeBuffer--;
        else{ blueBuffer++; increaseTime("orange"); }
        moves--;
      }
      orangePos = bp[numButton]; // Update Position
      //Press Button
      blueBuffer++;
      increaseTime("orange");
      if(lastColor!='O')orangeBuffer=0;
      lastColor='O';
    }
    else if(bc[numButton]=='B'){
      int moves = abs(bp[numButton] - bluePos);
      int moves2 = moves;
      //Move Blue Robot
      while(moves>0){
        if(blueBuffer>0) blueBuffer--;
        else{ orangeBuffer++; increaseTime("blue"); }
        moves--;
      }
      bluePos = bp[numButton]; // Update Position
      //Press Button
      orangeBuffer++;
      increaseTime("blue");
      if(lastColor!='B')blueBuffer=0;
      lastColor='B';
    }
    
    buttonPressed[numButton++] = true;
  }
  return totalTime;
}

int main(int argc, char *argv[]){
	int numTests;
  cin >> numTests;
  for(int i=1; i<=numTests; i++){
    char test[401];
    int totalButtons;
    cin >> totalButtons;
    
    char buttonColor[100];
    int buttonPosition[100];
    for(int j=0; j < totalButtons; j++){
      cin >> buttonColor[j];
      cin >> buttonPosition[j];
    }
    int seconds = runTestCase(totalButtons, buttonColor, buttonPosition);
    cout << "Case #" << i << ": " << seconds << endl;    
  }
  
  return 0;
}