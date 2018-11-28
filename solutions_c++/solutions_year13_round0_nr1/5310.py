//by Lilli Christoph
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
// #include <algorithm>
// #include <map>
// #include <cstdlib>
// #include <cmath>

using namespace std;

int main(void)
{
  int numCases, gameSize=4;
  vector < vector <string> > toeGrid(gameSize, vector <string> (gameSize, "L"));
  vector < vector <int> > myRow(gameSize, vector <int> (2,0)), myCol(gameSize, vector <int> (2,0));
  vector <int> myDiagUp(2,0), myDiagDown(2,0);
  int winner=-1, emptySquares=0;

  string inputfile = "A-large.in", toeString;
 
  //Load input from file
  ifstream inputFile(inputfile.c_str());
  inputFile >> numCases;
 
  //Get case data
  for(int c=1; c<numCases+1; c++)
    {
      for(int i=0; i<gameSize; i++)
	{
	  inputFile >> toeString;
	  for(int j=0; j<gameSize; j++)
	    toeGrid[i][j]=toeString[j];
	}

      // cout << "This is your final game array, which is " << toeGrid.size();
      // cout << " by " << toeGrid[0].size() << " in dimension" << endl;
      // for(int i=0; i<gameSize; i++)
      // 	{
      // 	  for(int j=0; j<gameSize; j++)
      // 	    cout << toeGrid[i][j] << " ";
      // 	  cout << endl;
      // 	}

      //Analyze this case/game
      //make sure variable are initialized first
     
      for(int i=0; i<gameSize; i++)
	for(int j=0; j<gameSize; j++)
	  {
	    if(toeGrid[i][j]=="O" || toeGrid[i][j]=="T")
	      {
		myRow[i][0]++;
		myCol[j][0]++;
		if( i+j==3)
		  myDiagUp[0]++;
		if(i==j)
		  myDiagDown[0]++;
	      }
	    if(toeGrid[i][j]=="X" | toeGrid[i][j]=="T")
	      {
		myRow[i][1]++;
		myCol[j][1]++;
		if(i+j==3)
		  myDiagUp[1]++;
		if(i==j)
		  myDiagDown[1]++;
	      }
	    if(toeGrid[i][j]==".")
	      emptySquares++;
	    
	      for(int player=0; player<2; player ++)
		{
		  if(myRow[i][player]==gameSize || myCol[j][player]==gameSize || myDiagUp[player]==gameSize
		     || myDiagDown[player]==gameSize)
		    winner=player;
		}
	  }


      //OutputResults
      if(winner==0)
	cout << "Case #" << c << ": O won" << endl;
      if(winner==1)
	cout << "Case #" << c << ": X won" << endl;
      if(winner<0 && emptySquares<=0)
	cout << "Case #" << c << ": Draw" << endl;
      if(winner<0 && emptySquares>0)
	cout << "Case #" << c << ": Game has not completed" << endl;

      for(int i=0; i<gameSize; i++)
	for(int player=0; player<2; player++)
	  {
	    myRow[i][player]=0;
	    myCol[i][player]=0;
	    myDiagUp[player]=0;
	    myDiagDown[player]=0;
	  }
      winner=-1;
      emptySquares=0;
    }

  return 0;
}
