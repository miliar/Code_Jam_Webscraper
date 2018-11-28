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

typedef struct {
  int button;
  int robot;
} MyValType;  

typedef enum {S0=0, S1, S2, S3} E_ReadState_T;

void ComputeAndWrite(MyValType myValVector[], int numberItems, int testNum);

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
         int numberItems;
         std::cin >> numberItems;
         MyValType myValVector[numberItems];
         char c;
         for (int i = 0; i < numberItems; i++) {
           std::cin >> c;
           if (c == 'O')
             myValVector[i].robot = 0;
           else
             myValVector[i].robot = 1;
           std::cin >> myValVector[i].button;
         }
         ++curTestIdx;
         ComputeAndWrite(myValVector, numberItems, curTestIdx);
         state = S1;
         break;
       }
       default: break;
     }
   }
}

void ComputeAndWrite(MyValType myValVector[], int numberItems, int testNum)
{
   // Find largest deviation...
   int allowed_P = 0;
   int allowed_O = 0;
   int current_Pos_P = 0;
   int current_Pos_O = 0;

   int totalTime = 0;
   for (int i = 0; i < numberItems; i++)
   {
      int P_or_O = myValVector[i].robot;
      int button = myValVector[i].button;
      int time = 0;
      if (P_or_O == 0) {
         if (allowed_O >= abs(button - current_Pos_O))
           time = 1;
         else 
           time = abs(button - current_Pos_O) + 1 - allowed_O;
         allowed_O = 0;
         allowed_P += time;
         current_Pos_O = button;
      }
      else {
         if (allowed_P >= abs(button - current_Pos_P))
           time = 1;
         else
           time = abs(button - current_Pos_P) + 1 - allowed_P;
         allowed_P = 0;
         allowed_O += time;
         current_Pos_P = button;
      }
      totalTime += time;
   }
   totalTime -= 1;

   std::cout << "Case #" << (testNum) << ": " << totalTime << std::endl;
}
