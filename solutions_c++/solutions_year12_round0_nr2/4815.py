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

int surprise [] = {-1, -1, 2, 2, 2,
                   3, 3, 3, 4, 4,
                   4, 5, 5, 5, 6,
                   6, 6, 7, 7, 7,
                   8, 8, 8, 9, 9,
                   9, 10, 10, 100, 100, 100 };

int nonsurprise [] = {0, 1, 1, 1, 2,
                   2, 2, 3, 3, 3,
                   4, 4, 4, 5, 5,
                   5, 6, 6, 6, 7,
                   7, 7, 8, 8, 8,
                   9, 9, 9, 10, 10, 10};

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
         int numTriplets, numSurprise, numP;
         std::cin >> numTriplets;
         std::cin >> numSurprise;
         std::cin >> numP;
         int elements[128];
         for (int i = 0; i < numTriplets; i++)
         {
            std::cin >> elements[i]; 
         }

         int numOutput = 0;
         int currSurprise = 0;
         for (int i = 0; i < numTriplets; i++) {
             int entry = elements[i];
             int n = nonsurprise[entry];
             if (n >= numP) {
                ++numOutput;
             } else if (currSurprise < numSurprise) {
                int m = surprise[entry]; 
                if (m >= numP) {
                      currSurprise++;
                      ++numOutput;
                }
             }
         }

         std::cout << "Case #" << ++curTestIdx << ": " << numOutput << std::endl;
         state = S1;
         break;
       }
       default: break;
     }
   }
}
