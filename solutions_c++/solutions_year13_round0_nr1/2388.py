#include <iostream>
#include <sstream>
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <unordered_map>
#include <fstream>
#include <stdexcept>
#include <memory> // note: i will use memory leaks, if its easier

using namespace std;

void evalLine(int& xCount, int& yCount, bool& emptyExists, char a,  char b, char c,  char d)
{
   vector<char> data = {a, b, c, d};

   for(auto iter : data) {
      if(iter == 'X') xCount++;
      if(iter == 'O') yCount++;
      if(iter == 'T') xCount++;
      if(iter == 'T') yCount++;
      if(iter == '.') emptyExists = true;
   }
}

int main(int argc, char** argv) {

   // Read input
   if(argc != 2)
      throw invalid_argument("no input: ./a.out [filename]");
   string str(argv[1]);
   ifstream in(str);
   if(!in.good() || !in.is_open())
      throw invalid_argument("file not found");

   int numCases;
   in >> numCases;

   for(int c=1; c<=numCases; c++) {
      vector<char> data;

      // Read test
      for(int i=0; i<16;) {
         char sign = in.get();
         if(sign == '\n')
            continue;
         i++;
         data.push_back(sign);
      }

      // Evaluate
      bool emptyExists = false;

      // rows
      {
         int xCount = 0;
         int yCount = 0;
         evalLine(xCount, yCount, emptyExists, data[0], data[1], data[2], data[3]);
         if(xCount == 4) {
            cout << "Case #" << c << ": X won" << endl;
            continue;
         }
         if(yCount == 4) {
            cout << "Case #" << c << ": O won" << endl;
            continue;
         }
      }

      {
         int xCount = 0;
         int yCount = 0;
         evalLine(xCount, yCount, emptyExists, data[4], data[5], data[6], data[7]);
         if(xCount == 4) {
            cout << "Case #" << c << ": X won" << endl;
            continue;
         }
         if(yCount == 4) {
            cout << "Case #" << c << ": O won" << endl;
            continue;
         }
      }

      {
         int xCount = 0;
         int yCount = 0;
         evalLine(xCount, yCount, emptyExists, data[8], data[9], data[10], data[11]);
         if(xCount == 4) {
            cout << "Case #" << c << ": X won" << endl;
            continue;
         }
         if(yCount == 4) {
            cout << "Case #" << c << ": O won" << endl;
            continue;
         }
      }

      {
         int xCount = 0;
         int yCount = 0;
         evalLine(xCount, yCount, emptyExists, data[12], data[13], data[14], data[15]);
         if(xCount == 4) {
            cout << "Case #" << c << ": X won" << endl;
            continue;
         }
         if(yCount == 4) {
            cout << "Case #" << c << ": O won" << endl;
            continue;
         }
      }

      // coulomo
      {
         int xCount = 0;
         int yCount = 0;
         evalLine(xCount, yCount, emptyExists, data[0], data[4], data[8], data[12]);
         if(xCount == 4) {
            cout << "Case #" << c << ": X won" << endl;
            continue;
         }
         if(yCount == 4) {
            cout << "Case #" << c << ": O won" << endl;
            continue;
         }
      }

      {
         int xCount = 0;
         int yCount = 0;
         evalLine(xCount, yCount, emptyExists, data[1], data[5], data[9], data[13]);
         if(xCount == 4) {
            cout << "Case #" << c << ": X won" << endl;
            continue;
         }
         if(yCount == 4) {
            cout << "Case #" << c << ": O won" << endl;
            continue;
         }
      }

      {
         int xCount = 0;
         int yCount = 0;
         evalLine(xCount, yCount, emptyExists, data[2], data[6], data[10], data[14]);
         if(xCount == 4) {
            cout << "Case #" << c << ": X won" << endl;
            continue;
         }
         if(yCount == 4) {
            cout << "Case #" << c << ": O won" << endl;
            continue;
         }
      }

      {
         int xCount = 0;
         int yCount = 0;
         evalLine(xCount, yCount, emptyExists, data[3], data[7], data[11], data[15]);
         if(xCount == 4) {
            cout << "Case #" << c << ": X won" << endl;
            continue;
         }
         if(yCount == 4) {
            cout << "Case #" << c << ": O won" << endl;
            continue;
         }
      }

      // diag
      {
         int xCount = 0;
         int yCount = 0;
         evalLine(xCount, yCount, emptyExists, data[0], data[5], data[10], data[15]);
         if(xCount == 4) {
            cout << "Case #" << c << ": X won" << endl;
            continue;
         }
         if(yCount == 4) {
            cout << "Case #" << c << ": O won" << endl;
            continue;
         }
      }

      {
         int xCount = 0;
         int yCount = 0;
         evalLine(xCount, yCount, emptyExists, data[3], data[6], data[9], data[12]);
         if(xCount == 4) {
            cout << "Case #" << c << ": X won" << endl;
            continue;
         }
         if(yCount == 4) {
            cout << "Case #" << c << ": O won" << endl;
            continue;
         }
      }

      if(emptyExists)
         cout << "Case #" << c << ": Game has not completed" << endl; else
         cout << "Case #" << c << ": Draw" << endl;
   }

   return 0;
}
