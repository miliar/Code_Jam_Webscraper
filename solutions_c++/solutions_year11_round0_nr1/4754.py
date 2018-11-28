#include <iostream.h>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string>
using namespace std;

int main()
{
      unsigned int T, N, tCase;
      int i, prevOpos, prevBpos, totNoOfSecs, curButnPos;
      int moves, curOps;
      char prevRobot, curRobot;
      ifstream inFile;
      ofstream outFile;
      
      inFile.open("C:\\Documents and Settings\\Administrator\\Desktop\\A-large.in");
      outFile.open("C:\\Documents and Settings\\Administrator\\Desktop\\A-largeout.txt");

      inFile >> T;
      for (tCase=1; tCase <= T; tCase++)
      {
          inFile >> N;
          prevOpos = prevBpos = 1;
          totNoOfSecs = 0;
          curOps = 0;
          for (i=0; i<N;i++)
          {
              inFile >> curRobot;
              inFile >> curButnPos;
            
              if (i==0)
              { 
                curOps = curButnPos;
                prevRobot = curRobot;
                if (curRobot == 'O')
                    prevOpos = curButnPos;
                else
                   prevBpos = curButnPos;
              }
              else
              if (curRobot == 'O')
              {  
                 if (prevRobot == 'O')
                 {
                    moves = curButnPos-prevOpos;
                    if (moves < 0) moves = -moves;
                    curOps += moves+1;
                 }  
                 else 
                 {
                       totNoOfSecs += curOps;
                       moves = curButnPos-prevOpos;
                       if (moves < 0) moves = -moves;
                       if (moves <=curOps)
                          curOps = 1;
                       else
                          curOps = moves-curOps+1;
                 }       
                 prevRobot = 'O';
                 prevOpos = curButnPos;
              }                
              else
              {
                 if (prevRobot == 'B')
                 {
                    moves = curButnPos-prevBpos;
                    if (moves < 0) moves = -moves;
                    curOps += moves+1;
                 }    
                 else 
                 {
                       totNoOfSecs += curOps;
                       moves = curButnPos-prevBpos;
                       if (moves < 0) moves = -moves;
                       if (moves <=curOps)
                          curOps = 1;
                       else
                          curOps = moves-curOps+1;
                 }     
                 prevRobot = 'B';
                 prevBpos=curButnPos;
              }
             
            }
            totNoOfSecs += curOps;   
            outFile << "Case #" << tCase << ": " << totNoOfSecs << "\n";       
          } 
      inFile.close();
      outFile.close();
      //system("PAUSE");
      return 0;
}
