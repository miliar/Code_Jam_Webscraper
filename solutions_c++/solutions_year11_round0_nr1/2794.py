#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main(){
  const char filein[] = "A-large.in";
  const char fileout[] = "A-large.out";
  ifstream i_file;
  ofstream o_file;
  int num_case = 0;

  i_file.open(filein);
  o_file.open(fileout);
  if(i_file.is_open())
    {
      i_file>>num_case;
      for(int i=0; i<num_case; i++)
	{
	  int N;
	  i_file>>N;
	  char * robots = new char[N];
	  int * positions = new int[N];
	  for(int j=0; j<N; j++) {
	    i_file>>robots[j];
	    i_file>>positions[j];
	    positions[j]--;
	  }
	  int pointerO = 0, pointerB = 0;
	  while(pointerO < N && robots[pointerO] != 'O')pointerO++;
	  while(pointerB < N && robots[pointerB] != 'B')pointerB++;
	  int positionO = 0, positionB = 0;
	  char currentRobot = robots[0];
	  int count = 0;
	  while(pointerO < N && pointerB < N) {
	    int stepsO = abs(positions[pointerO]-positionO);
	    int stepsB = abs(positions[pointerB]-positionB);
	    if(currentRobot == 'O') {
	      if(stepsO >= stepsB) {
		positionB = positions[pointerB];
	      }
	      else {
		if(positions[pointerB] > positionB)
		  positionB = positionB + stepsO + 1;
		else
		  positionB = positionB - stepsO - 1;
	      }
	      positionO = positions[pointerO];
	      count += stepsO + 1;
	      pointerO++;
	      while(pointerO < N && robots[pointerO] != 'O')pointerO++;
	      if(pointerO > pointerB)currentRobot = 'B';
	    }
	    else {
	      if(stepsB >= stepsO) {
		positionO = positions[pointerO];
	      }
	      else {
		if(positions[pointerO] > positionO)
		  positionO = positionO + stepsB + 1;
		else
		  positionO = positionO - stepsB - 1;
	      }
	      positionB = positions[pointerB];
	      count += stepsB + 1;
	      pointerB++;
	      while(pointerB < N && robots[pointerB] != 'B')pointerB++;
	      if(pointerB > pointerO)currentRobot = 'O';
	    }
	  }
	  while(pointerO < N) {
	    int stepsO = abs(positions[pointerO]-positionO);
	    count += stepsO + 1;
	    positionO = positions[pointerO];
	    pointerO++;
	  }
	  while(pointerB < N) {
	    int stepsB = abs(positions[pointerB]-positionB);
	    count += stepsB + 1;
	    positionB = positions[pointerB];
	    pointerB++;
	  }
	  o_file<<"Case #"<<(i+1)<<": "<<count<<endl;
	  delete robots;
	  delete positions;
	}
      i_file.close();
      o_file.close();
    }
  return 0;
}
