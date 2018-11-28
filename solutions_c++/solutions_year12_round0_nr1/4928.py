// Project : Code Jam
// Author: Shomit Dutta

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
//using namespace std;

typedef enum {S0=0, S1, S2, S3} E_ReadState_T;
typedef enum {Q=0, W, E, R, A, S, D, F, END_OF_BASE} Base_Elt_T;

char translate [] = {'y', 'h', 'e', 's', 'o',
                     'c', 'v', 'x', 'd', 'u',
                     'i', 'g', 'l', 'b', 'k',
                     'r', 'z', 't', 'n', 'w',
                     'j', 'p', 'f', 'm', 'a', 'q'};

int main()
{
   std::string line;
   int numTestcases = -1;
   E_ReadState_T state = S0;
   int curTestIdx = 0;
   int lineSize = 128;
   char inputLine[lineSize];
   char outputLine[lineSize];
   while (1)
   {
     if ((numTestcases == 0) || (curTestIdx == numTestcases))
       break;
     switch(state) {
       case S0 : {
         std::cin >> numTestcases;
         std::cin.getline(inputLine, lineSize);
         state = S1;
         break;
       }
       case S1 : {
         for (int i = 0; i < lineSize; i++)
         {
            inputLine[i] = '\0';
            outputLine[i] = '\0';
         }
         std::cin.getline(inputLine, lineSize);

         
         for (int i = 0; inputLine[i] != '\0'; i++)
         {
            if ((inputLine[i] >= 'a') && (inputLine[i] <= 'z')) {
               outputLine[i] = translate[inputLine[i] - 'a'];
            } else {
               outputLine[i] = inputLine[i];
            }
         }
         std::cout << "Case #" << ++curTestIdx << ": " << outputLine << std::endl;
         state = S1;
         break;
       }
       default: break;
     }
   }
}
