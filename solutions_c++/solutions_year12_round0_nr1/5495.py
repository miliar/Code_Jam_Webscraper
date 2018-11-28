#include <iostream.h>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string>
using namespace std;


int main()
{
      unsigned int T, tCase;
      string gToeMap, inString, outString;
      size_t inLength;
      int i;
      char inChar;
      ifstream inFile;
      ofstream outFile;
      inFile.open("C:\\Documents and Settings\\Administrator\\Desktop\\A-small.in");
      outFile.open("C:\\Documents and Settings\\Administrator\\Desktop\\A-small-out.txt");
      gToeMap = "yhesocvxduiglbkrztnwjpfmaq";
      inFile >> T;
      inFile.get(inChar);
      for (tCase=1; tCase <= T; tCase++)
      {
          inString.clear();
          outString.clear();
          while(inFile.get(inChar))
          {
           if (inChar == '\n')  
              break; 
           else
              if (inChar != ' ')
                 outString += gToeMap[inChar-'a']; 
              else
                  outString += ' ';      
          }
          outFile << "Case #" << tCase << ": " << outString << "\n";
      }

}
