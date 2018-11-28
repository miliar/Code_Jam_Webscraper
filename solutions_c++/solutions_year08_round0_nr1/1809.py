#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int testCount, engineCount, queryCount, changeCount;
string s;
vector <string> engines;
int engineUsed[100];
int engineUsedCount;

int getEngineIndex(string name){
   for (int k=0; k<engines.size(); k++)
      if (engines[k]==name)
         return k;
   return -1;
}

int main()
{
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);

   cin >> testCount;
   for (int i=0; i<testCount; i++){
      engines.clear();
      memset(engineUsed, 0, 100);
      engineUsedCount = 0;
      changeCount = 0;
      
      cin >> engineCount;
      getline(cin, s);
      for (int j=0; j<engineCount; j++){
         getline(cin, s);
         engines.push_back(s);
      }
      cin >> queryCount;
      getline(cin, s);
      for (int j=0; j<queryCount; j++){
         getline(cin, s);
         int engineIndex = getEngineIndex(s);
         if (engineUsed[engineIndex]==0){
            engineUsed[engineIndex] = 1;
            engineUsedCount++;
            if (engineUsedCount == engineCount){
               changeCount++;
               memset(engineUsed, 0, 100);
               engineUsed[engineIndex] = 1;
               engineUsedCount = 1;
            }
         }
      }
      cout << "Case #" << (i+1) << ": " << changeCount << endl;
   }

   return 0;
}

