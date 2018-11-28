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

int findElmtIdx(char c)
{
  switch(c) {
     case 'Q' : return 0;
     case 'W' : return 1;
     case 'E' : return 2;
     case 'R' : return 3;
     case 'A' : return 4;
     case 'S' : return 5;
     case 'D' : return 6;
     case 'F' : return 7;
     default: return -1;
  }
}

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
         int numberCombineItems;
         std::cin >> numberCombineItems;
         std::map<char, char> combineMap[END_OF_BASE];
         for (int i = 0; i < numberCombineItems; i++)
         {
            char c1, c2, c3;
            std::cin >> c1 >> c2 >> c3;
            int c1Elmt = findElmtIdx(c1);
            int c2Elmt = findElmtIdx(c2);
            combineMap[c1Elmt][c2] = c3;
            combineMap[c2Elmt][c1] = c3;
         }

         int numberOpposeItems;
         std::cin >> numberOpposeItems;
         std::set<char> opposeSet[END_OF_BASE];
         for (int i = 0; i < numberOpposeItems; i++)
         {
            char c1, c2;
            std::cin >> c1 >> c2;
            int c1Elmt = findElmtIdx(c1);
            int c2Elmt = findElmtIdx(c2);
            opposeSet[c1Elmt].insert(c2);
            opposeSet[c2Elmt].insert(c1);
         }

         int numberItems;
         std::cin >> numberItems;
         std::vector<char> outputElements;
         char c;
         for (int i = 0; i < numberItems; i++) {
           std::cin >> c;
           if (outputElements.size() == 0)
           {
             outputElements.push_back(c);
           }
           else
           {
             /* check for oppose elements */
             int cElmt = findElmtIdx(c);
             bool done = false;

             /* check for combine elements */
             if (combineMap[cElmt].size() > 0)
             {
               char c4 = outputElements.back();
               std::map<char, char>::const_iterator iter3 = combineMap[cElmt].find(c4);
               if (iter3 != combineMap[cElmt].end())
               {
                  outputElements.pop_back();
                  outputElements.push_back((iter3->second));
                  done = true;
               }
             }

             if ((done == false) && (opposeSet[cElmt].size() > 0))
             {
               std::vector<char>::const_iterator iter1 = outputElements.begin();
               while(iter1 != outputElements.end())
               {
                 std::set<char>::const_iterator iter2 = opposeSet[cElmt].find((*iter1));
                 if (iter2 != opposeSet[cElmt].end())
                 {
                   outputElements.resize(0);
                   done = true;
                   break;
                 }
                 ++iter1;
               }
             }

             // if neither oppose nor combine
             if (done == false)
               outputElements.push_back(c);
           }
         }
         ++curTestIdx;
         std::cout << "Case #" << curTestIdx << ": [";
         std::vector<char>::const_iterator iter = outputElements.begin();
         while (iter != outputElements.end())
         {
           std::cout << "" << (*iter);
           ++iter;
           if (iter != outputElements.end())
              std::cout << ", ";
           else
              break;
         }
         std::cout << "]" << std::endl;
         state = S1;
         break;
       }
       default: break;
     }
   }
}
