#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

typedef struct{
  char robot;
  short button;
} task;

long Absolute( long num )
{
  if (num >= 0)
    return num;
  return (-1*num);
}

void makeOneStep( long& time, long& robotTime, short& robotPos, short robotDest)
{
    int distance = Absolute(robotDest - robotPos); //distance to move to next position

    int timeToAdd = distance -
      (time - robotTime); //spare time while the other robot finished previous task;
      
    if (timeToAdd < 0)
      timeToAdd = 0; //spare time was enough for the move
      
    time = time + timeToAdd + 1; //+1 to push the button
    robotTime = time;
    robotPos = robotDest;
}

long simulate(vector<task> plan)
{
  long time = 0;
  long tO = 0;
  long tB = 0;
  short posO = 1;
  short posB = 1;
  for (int i = 0; i < plan.size(); i++)
  {
    task tsk = plan[i];
    
/*    cout << "State\nCurrent Time = " << time << endl <<
	    "Orange Pos = " << posO <<
	    " Orange Time = " << tO << endl <<
	    "Blue Pos = " << posB << 
	    " Blue Time = " << tB << endl <<
	    "NEXT TASK: robot = " << plan[i].robot << " button = " << plan[i].button <<endl << endl;
*/	    
    if (tsk.robot == 'O')
      makeOneStep( time, tO, posO, tsk.button);
    else
      makeOneStep( time, tB, posB, tsk.button);

  }

return time;
}

int main(int argc, const char* argv[])
{

	if ( argc < 3 )
		cout << "wrong param" << endl;

	string filename(argv[1]);
	cout << filename << endl;

	ifstream inFile(argv[1]);
	ofstream outFile(argv[2]); 

	if (!inFile.is_open())
	{
		cout << "failed to open file" << endl;
		return 1;
	}
	
	int c;
	inFile >> c;
	int n;
	vector<task> plan;
	int i = 1;
	for ( ; c > 0; c--)
	{
		plan.clear();
		inFile >> n;
		for( ; n > 0; n--)
		{
		  task tsk;
		  inFile >> tsk.robot;
		  inFile >> tsk.button;
		  plan.push_back( tsk );
		}
		cout << "Case #" << i << ": " <<  simulate(plan) << endl;
		outFile << "Case #" << i++ << ": " << simulate(plan) << endl;

	}	
	outFile << endl;
	outFile.close();
	inFile.close();

	return 0;
}



