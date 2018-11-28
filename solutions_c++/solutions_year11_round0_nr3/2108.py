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
         int numberItems;
         std::cin >> numberItems;
         std::vector<int> myValVector;
         int c;
         for (int i = 0; i < numberItems; i++) {
           std::cin >> c;
           myValVector.push_back(c);
         }
         ++curTestIdx;
         std::sort(myValVector.begin(), myValVector.end());
         int pile1_sum = 0;
         int pile1_xor = 0;
         for (int i = 0; i < numberItems; i++)
         {
           pile1_xor = pile1_xor ^ myValVector[i];
           if (i > 0)
             pile1_sum += myValVector[i];
         }

         std::cout << "Case #" << curTestIdx;
         if (pile1_xor == 0)
           std::cout << ": " << pile1_sum << std::endl;
         else
           std::cout << ": NO" << std::endl;
         state = S1;
         break;
       }
       default: break;
     }
   }
}
