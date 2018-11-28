#include <iostream>
#include <fstream>

using namespace std;

int main(){
  ifstream inputFile;
  char x[500];
  int Orange[101], Blue[101], Order[101];
  int OrangeCounter,BlueCounter;
  int blueButton, orangeButton;
  int T; // Test cases
  int N; // number of buttons to be pressed
  char Robot;
  int number;
  int ocurrent=0,bcurrent=0;
  int timeel =0;
  int j;
  
  inputFile.open("b.txt");

  inputFile >> T;
  blueButton =1;
  orangeButton =1;

  for (int i=0; i<T; i++){
    inputFile >> N ;
    OrangeCounter =0;
    BlueCounter = 0;
    for (j=0; j< N; j++){
      inputFile >> Robot >> number;
      if ( Robot == 'O'){
        Orange[OrangeCounter] = number;
        OrangeCounter++;
        Order[j] = 0;
      }
      else{
        Blue[BlueCounter] = number;
        BlueCounter++;
        Order[j] = 1;
      }
    }
    Order[j] = 2;
    // proceed
    timeel =0 ;
    j=0;
    ocurrent=0;
    bcurrent=0;
    blueButton =1;
    orangeButton =1;
    while ( Order[j]!=2){
      if (Order[j] == 0 && orangeButton == Orange[ocurrent]){
        ocurrent ++;
        if ( blueButton < Blue[bcurrent] ){
          blueButton++;
        }
        else if ( blueButton > Blue[bcurrent] ){
          blueButton--;
        }
        timeel++;
        j++;
      } 
      else if (Order[j] == 1 && blueButton == Blue[bcurrent]){
        bcurrent ++;
        if ( orangeButton < Orange[ocurrent] ){
          orangeButton++;
        }
        else if ( orangeButton > Orange[ocurrent] ){
          orangeButton--;
        }
        timeel++;
        j++;
      } 
      else {
        if ( blueButton < Blue[bcurrent] ){
          blueButton++;
        }
        else if ( blueButton > Blue[bcurrent] ){
          blueButton--;
        }

        if ( orangeButton < Orange[ocurrent] ){
          orangeButton++;
        }
        else if ( orangeButton > Orange[ocurrent] ){
          orangeButton--;
        }

        timeel++;
      } 
    }
    cout << "Case #" << i+1 << ": " << timeel << endl;


  }
}

