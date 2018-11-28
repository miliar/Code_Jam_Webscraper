#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int max(int num1, int num2);

int main(int argc, char* argv[]){
  if(argc!=3){
    cout << "format: ./main file1 file2" << endl;
    return 0;
  }

  ifstream fp_in(argv[1], ios::in);
  ofstream fp_out(argv[2], ios::out);
  int testCase;
  fp_in >> testCase;
  for (int i=1; i<=testCase; i++){
    int result=0;

    // read in the input;
    int ButtonNumber;
    fp_in >> ButtonNumber;
    int* pos=new int [ButtonNumber];
    char* robot=new char [ButtonNumber];
    for(int j=0; j<ButtonNumber; j++){
      fp_in >> robot[j];
      fp_in >> pos[j];
    }

    //calculate time;
    int tO0=0;
    int tB0=0;
    char lastColor='a';
    int OLastPos=1, BLastPos=1;
    for (int j=0; j<ButtonNumber; j++){
      if(robot[j]==lastColor){
	result=result+abs(pos[j-1]-pos[j])+1;
	if(lastColor=='O'){
	  OLastPos=pos[j];
	  tO0=result;
	} else {
	  BLastPos=pos[j];
	  tB0=result;
	}
      } else {
	lastColor=robot[j];
	if(robot[j]=='O'){
	  result=max( (abs(pos[j]-OLastPos)+tO0+1), (result+1) );
	  tO0=result;
	  OLastPos=pos[j];
	} else {
	  result=max( (abs(pos[j]-BLastPos)+tB0+1), (result+1) );
	  tB0=result;
	  BLastPos=pos[j];
	}
      }
    }
    fp_out << "Case #" << i << ": " << result << endl;
    delete pos;
    delete robot;
  }

  fp_in.close();
  fp_out.close();

  return 0;
}

int max(int num1, int num2){
  if(num1>num2)
    return num1;
  return num2;
}
