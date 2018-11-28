#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string>
using namespace std;


int main()
{
      unsigned int T, N,C, D,  tCase, noOfDigits;
      unsigned long A, B, i, j, k, strToNum, recPairCnt;
      int duplicateFound;
      ifstream inFile;
      ofstream outFile;
      string  curNum, rotatedNum, rotArray[10];
      ostringstream numToStr;
      
      
      inFile.open("C:\\Documents and Settings\\Administrator\\Desktop\\A-small.in");
      outFile.open("C:\\Documents and Settings\\Administrator\\Desktop\\A-small-out.txt");

      inFile >> T;
      for (tCase=1; tCase <= T; tCase++)
      {
          //cout << "In test case " << tCase << "\n";
          //system("PAUSE");
          inFile >> A;
          inFile >> B;
          recPairCnt = 0;
          for (i=A; i <= B; i++)
          {
              //cout << "In outer for loop " << i << "\n";
              //system("PAUSE");
              numToStr.str("");
              numToStr << i;
              curNum =  numToStr.str();
              //cout << " the no. is" << curNum << "\n";
              //system("PAUSE");
              noOfDigits = curNum.length();
              rotArray[0] = curNum;  
              rotatedNum = curNum;
              for (k=1; k < noOfDigits; k++)
              {
                  //cout << "In rotation for loop " << k << "\n";
                  //system("PAUSE");
                  rotate(rotatedNum.rbegin(), rotatedNum.rbegin() + 1, rotatedNum.rend());
                  //cout << " the rotated no. is" << rotatedNum << "\n";
                  //system("PAUSE");
                  rotArray[k] = rotatedNum;
                  if (rotatedNum[0] == '0')
                     continue;
                  istringstream(rotatedNum) >> strToNum;
                  //cout << " the strToNum is" << strToNum << "\n";
                  //system("PAUSE");
                  if ((strToNum < i+1) || (strToNum > B))
                     continue;
                  duplicateFound = 0;
                  for (j=0; j < k; j++)
                  {
                      if (rotArray[j] == rotatedNum)
                      {
                         duplicateFound = 1;
                         break;
                      }        
                  }
                  if (duplicateFound == 0)
                     recPairCnt++;
                  //outFile << i << " " << strToNum << "\n";
                  //cout << " the recPairCnt is" << recPairCnt << "\n";
                  //system("PAUSE");
                          
              }
             
          }
          
          outFile << "Case #" << tCase << ": " << recPairCnt << "\n";
   
      }
      inFile.close();
      outFile.close();
      //system("PAUSE");
      return 0;
}
