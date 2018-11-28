#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int testCount, fromA, fromB, iTime, countA, countB, needA, needB, turnover;
int changeA[1440], changeB[1440];
string sTime;

int main()
{
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);

   cin >> testCount;
   for (int i=0; i<testCount; i++){
      countA = 0;
      countB = 0;
      needA = 0;
      needB = 0;
      memset(changeA, 0, sizeof(changeA));
      memset(changeB, 0, sizeof(changeB));
      cin >> turnover;
      cin >> fromA >> fromB;
      for (int j=0; j<fromA; j++){
         cin >> sTime;
         iTime = ((sTime[0]-'0')*10+(sTime[1]-'0'))*60 + (sTime[3]-'0')*10+(sTime[4]-'0');
         changeA[iTime]--;
         cin >> sTime;
         iTime = ((sTime[0]-'0')*10+(sTime[1]-'0'))*60 + (sTime[3]-'0')*10+(sTime[4]-'0');
         if (iTime+turnover<1440)
            changeB[iTime+turnover]++;
      }
      for (int j=0; j<fromB; j++){
         cin >> sTime;
         iTime = ((sTime[0]-'0')*10+(sTime[1]-'0'))*60 + (sTime[3]-'0')*10+(sTime[4]-'0');
         changeB[iTime]--;
         cin >> sTime;
         iTime = ((sTime[0]-'0')*10+(sTime[1]-'0'))*60 + (sTime[3]-'0')*10+(sTime[4]-'0');
         if (iTime+turnover<1440)
            changeA[iTime+turnover]++;
      }

      for (int j=0; j<1440; j++){
         countA += changeA[j];
         if (countA<0){
            needA += -countA;
            countA = 0;
         }
         countB += changeB[j];
         if (countB<0){
            needB += -countB;
            countB = 0;
         }
      }

      cout << "Case #" << (i+1) << ": " << needA << " " << needB << endl;
   }

   return 0;
}

