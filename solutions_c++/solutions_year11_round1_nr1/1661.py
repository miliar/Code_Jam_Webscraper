#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
   string filename = "A-small-attempt5.in.txt";
   string filenameOut = filename + ".out";
   ifstream inFile(filename.c_str());
   ofstream outFile(filenameOut.c_str());

   int cases = 0;
   inFile >> cases;

   for (int c = 1; c <= cases; c++)
   {
      long long maxGamesPlayedToday = 0;
      int percentWonTodayPd = 0;
      int percentWonTotalPg = 0;
      inFile >> maxGamesPlayedToday >> percentWonTodayPd >> percentWonTotalPg;

      string result = "Broken";
      long long gamesPlayedToday = 0;
      long long gamesPlayedTotal = 0;

      if ((percentWonTotalPg == 100 && percentWonTodayPd == 100)) {
         result = "Possible";
         goto done;
      }
      else if ((percentWonTotalPg == 100 && percentWonTodayPd != 100)) {
         goto done;
      }
      else if ((percentWonTotalPg == 0 && percentWonTodayPd == 0)) {
         result = "Possible";
         goto done;
      }
      else if ((percentWonTotalPg == 0 && percentWonTodayPd != 0)) {
         goto done;
      }

      for (gamesPlayedTotal = 1; gamesPlayedTotal <= 10000000ll; gamesPlayedTotal++)
      {
         if ((gamesPlayedTotal * percentWonTotalPg) % 100 != 0) continue;
         long long gamesWonTotal = (gamesPlayedTotal * percentWonTotalPg) / 100;

         for (gamesPlayedToday = 1; gamesPlayedToday <= min(gamesPlayedTotal, maxGamesPlayedToday); gamesPlayedToday++)
         {
            if ((gamesPlayedToday * percentWonTodayPd) % 100 != 0) continue;
            long long gamesWonToday = (gamesPlayedToday * percentWonTodayPd) / 100;

            result = "Possible";
            goto done;
         }
      }

      done:;
      cout << "Case #" << c << ": " << result << endl;
      outFile << "Case #" << c << ": " << result << endl;
   }

   return 0;
}