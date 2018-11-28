#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <stdlib.h> 

using namespace std;


char matrix [4][4] ;

bool CheckColumn(char type)
{
    for(int i=0;i<4;i++)
    {
        if ( ((matrix[i][0] == type) || (matrix[i][0] == 'T')) &&
            ((matrix[i][1] == type) || (matrix[i][1] == 'T')) &&
            ((matrix[i][2] == type) || (matrix[i][2] == 'T')) &&
            ((matrix[i][3] == type) || (matrix[i][3] == 'T')) 
            )
        {
            return true;
        }
    }
    return false;
}

bool CheckRow(char type)
{
    for (int i = 0; i < 4; i++)
    {
        if (((matrix[0][i] == type) || (matrix[0][i] == 'T')) &&
            ((matrix[1][i] == type) || (matrix[1][i] == 'T')) &&
            ((matrix[2][i] == type) || (matrix[2][i] == 'T')) &&
            ((matrix[3][i] == type) || (matrix[3][i] == 'T'))
            )
        {
            return true;
        }
    }
    return false;
}

bool CheckTransverse(char type)
{
    if(  
        (((matrix[0][0] == type) || (matrix[0][0] == 'T')) &&
            ((matrix[1][1] == type) || (matrix[1][1] == 'T')) &&
            ((matrix[2][2] == type) || (matrix[2][2] == 'T')) &&
            ((matrix[3][3] == type) || (matrix[3][3] == 'T'))
            )
        ||
        ( ((matrix[3][0] == type) || (matrix[3][0] == 'T')) &&
            ((matrix[2][1] == type) || (matrix[2][1] == 'T')) &&
            ((matrix[1][2] == type) || (matrix[1][2] == 'T')) &&
            ((matrix[0][3] == type) || (matrix[0][3] == 'T'))
            )
        )
    {
        return true;
    }
    return false;
}

/*string Solve(ifstream& fin){
    int emptyPlaceNumber = 0;
    for (int i = 0; i < 4; i++) {
        string line ;
		getline (fin,line);
        for (int j = 0; j < 4; j++) {
            matrix[i][j] = line[j];
            if(matrix[i][j]=='.')
            {
                emptyPlaceNumber++;
            }
        }
    }

}*/


int main () {
  string line1;
  ifstream infile;
  infile.open("c:\\cj2013\\A-large.in");
  ofstream outfile;
  outfile.open ("c:\\cj2013\\A-large.out");
  if (infile.is_open())
  {
      getline (infile,line1);
      cout << line1 << cout;
	  int numberOfTests = atoi(line1.c_str());
	  cout << numberOfTests << cout;
	  for (int t = 1; t <= numberOfTests; t++) {
          int emptyPlaceNumber = 0;
            for (int i = 0; i < 4; i++) {
                string line ;
        		getline (infile,line);
                for (int j = 0; j < 4; j++) {
                    matrix[i][j] = line[j];
                    if(line[j]=='.')
                    {
                        emptyPlaceNumber++;
                    }
                }
            }
            getline(infile,line1);
            // check line style
            if (CheckColumn('O') || CheckRow('O') || CheckTransverse('O')){
              outfile<< "Case #" << t << ": " << "O won" << endl;
              continue;
              }
          if (CheckColumn('X') || CheckRow('X') || CheckTransverse('X')) {
                         outfile<< "Case #" << t << ": " << "X won" << endl;
                         continue;
          }
          outfile<< "Case #" << t << ": " <<  ((emptyPlaceNumber == 0) ? "Draw" : "Game has not completed") << endl; ;
      }
  }

  infile.close();
  outfile.close();
  return 0;
}
