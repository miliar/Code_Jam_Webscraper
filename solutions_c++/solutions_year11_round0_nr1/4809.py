//Caitlin Derr
//Google Code Jam Qualification Round Problem A

#include<iostream>
#include<fstream>

using namespace std;

//struct to hold each button location and associated robot
struct steps
{
  char robot;
  short location;
};

int main(int argc, char *argv[])
{
  string inputFile, outputFile;
  short cases;
  
  
  if(argc != 3)
  { 
    cout << "\nIncorrect argument. Please enter in the following" 
	"format:" << endl;
	cout << "programName inputFile outputFile" << endl;
    return(0);
  }
  
  inputFile = argv[1];
  outputFile = argv[2];
  
  ifstream input;
  input.open(inputFile.c_str());
  
  ofstream out;
  out.open(outputFile.c_str());
  
  //check to make sure file was opened, exit if not opened
  if(!(input.is_open()))
  {
    cout << "File " << inputFile << " not opened." << endl;
	exit(1);
  }
  
  //check to make sure file was opened, exit if not opened
  if(!(out.is_open()))
  {
    cout << "File " << outputFile << " not opened." << endl;
	exit(1);
  }
  
  input >> cases;
  
  for(int i = 1; i<=cases; i++)
  {
	
	char robot; 
    short button, presses;
	short step = 1;
	short turn = 0;
	short pressed = 0;
	input >> presses;
	steps buttons[presses-1]; 
	for(int b = 0; b<presses; b++)
	{
	  input >> robot;
	  input >> button;  
	  buttons[b].robot = robot;
	  buttons[b].location = button;  
	}
    
    short oStep = 1;
    short bStep = 1;
	
	while(presses != pressed)
    {
      short oMoveTo, bMoveTo;
	  short oMin = 150;
	  short bMin = 150;
	  bool oAssigned = false;
	  bool bAssigned = false;

	  //find button for both robots
	  
	  short f = 0;
	  while((!oAssigned && !bAssigned) || f < presses)
	  {
	    if((buttons[f].robot == 'O') && (!oAssigned))
		{
		  oMoveTo = buttons[f].location;
		  oMin = f;
		  oAssigned = true;
		}
		else if((buttons[f].robot == 'B') && (!bAssigned))
		{
		  bMoveTo = buttons[f].location;
		  bMin = f;
		  bAssigned = true;
		}
		f++;
	  }	  
	  
	  //check if orange robot is at button position, if not, move toward it
	  if(oStep == oMoveTo)
	  {
	    if(oMin < bMin)
	    { 
		  pressed++;
		  buttons[oMin].robot = 'X';
	    }
      }		
	  else
	  {
         if(oStep < oMoveTo)
		   oStep++;
		 else
		   oStep--;
		   
	  }
	  
	  //check if blue robot is at button position, if not, move toward it
	  if(bStep == bMoveTo)
	  {
	    if(bMin < oMin)
	    { 
		  pressed++;
		  buttons[bMin].robot = 'X';
	    }
      }		
	  else
	  {
         if(bStep < bMoveTo)
		   bStep++;
		 else
		   bStep--;
		   
	  }
	  turn++;
    }	
    out << "Case #" << i << ": " << turn << endl;
  }
  input.close();
  return 0;
}
