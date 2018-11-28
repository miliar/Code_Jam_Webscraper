#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <string>
#define SEARCH "welcome to code jam"
#define MAXDIGITS 4
#define MAXNUMPRINT 10000

using namespace std;

int main() {
   int numcases;
   string search(SEARCH);
   string sentence;
   
   cin >> numcases;
   getline(cin, sentence);
   
   for (int casenum = 1; casenum <= numcases; casenum++) {
      getline(cin, sentence);
      
      int possible[search.size() + 1][sentence.size() + 1];

      for (int i = 0; i <= search.size(); i++)
         possible[i][sentence.size()] = 0;

      for (int i = 0; i <= sentence.size(); i++)
         possible[search.size()][i] = 1;

      for (int firstlet = search.size() - 1; firstlet >= 0; firstlet--) {
         int countlet = 0;

         for (int substring = sentence.size() - 1; substring >= 0; substring--) {
            possible[firstlet][substring] = possible[firstlet][substring + 1];

            if (sentence[substring] == search[firstlet]) 
               possible[firstlet][substring] = (possible[firstlet][substring] +
                possible[firstlet + 1][substring]) % MAXNUMPRINT;
         }
      }
      
      cout << "Case #" << casenum << ": ";
      cout << setfill('0') << setw(MAXDIGITS);
      cout << possible[0][0] << endl;
   }

   return 0;
}
