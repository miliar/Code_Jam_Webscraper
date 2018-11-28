// Project : Code Jam
// Author: Shomit Dutta

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <map>
//using namespace std;

typedef enum {S0=0, S1, S2, S3} E_ReadState_T;

int main()
{
   std::string line;
   int numTestcases = -1;
   E_ReadState_T state = S0;
   int curTestIdx = 0;
   while (1)
   {
     if ((numTestcases == 0) || (curTestIdx == numTestcases)) 
       break;
     switch(state) {
       case S0 : {
         std::cin >> numTestcases;
         state = S1;
         break;
       }
       case S1 : {
         int numberRows;
         std::cin >> numberRows;
         int numberColumns;
         std::cin >> numberColumns;
         char myValVector [numberRows][numberColumns];
         char c;
         for (int i = 0; i < numberRows; i++) {
           for (int j = 0; j < numberColumns; j++) {
             std::cin >> c;
             myValVector[i][j] = c;
           }
         }
      
         bool impossible = false;
         for (int i = 0; i < numberRows; i++) {
           for (int j = 0; j < numberColumns; j++) {
            if(myValVector[i][j] == '#') {
               // vereify if red can be made
              myValVector[i][j] = '/';
              if ((j+1) < numberColumns)
              {
                if (myValVector[i][j+1] == '#') 
                  myValVector[i][j+1] = '\\';
                else
                  impossible = true;

                if ((i+1) < numberRows)
                {
                  if (myValVector[i+1][j+1] == '#') 
                    myValVector[i+1][j+1] = '/';
                  else
                    impossible = true;
                }
                else {
                    impossible = true;
                }
              }
              else {
                  impossible = true;
              }

              if ((i+1) < numberRows)
              {
                if (myValVector[i+1][j] == '#') 
                  myValVector[i+1][j] = '\\';
                else
                  impossible = true;
              }
              else {
                  impossible = true;
              }
           }
         }
       }

         ++curTestIdx;
       if (impossible)
   {
     std::cout << "Case #" << (curTestIdx) << ": " << std::endl;
     std::cout << "Impossible" << std::endl;
   }
   else {
     std::cout << "Case #" << (curTestIdx) << ":" << std::endl;
         char c;
         for (int i = 0; i < numberRows; i++) {
           for (int j = 0; j < numberColumns; j++) {
             std::cout << myValVector[i][j];
           }
           std::cout << std::endl;
         }
   }
         state = S1;
         break;
       }
       default: break;
     }
   }
}

void ComputeAndWrite(std::vector<int> myValVector, int numberItems, int testNum)
{
   int pile1_sum = 0;
   int pile1_xor = 0;
   for (int i = 0; i < numberItems; i++)
   {
     pile1_xor = pile1_xor ^ myValVector[i];
     if (i > 0) 
       pile1_sum += myValVector[i];
   }

   if (pile1_xor == 0)
   {
     std::cout << "Case #" << (testNum) << ": " << pile1_sum << std::endl;
   }
   else {
     std::cout << "Case #" << (testNum) << ": NO" << std::endl;
   }
}
