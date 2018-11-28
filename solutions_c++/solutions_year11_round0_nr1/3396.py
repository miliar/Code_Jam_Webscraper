#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

void problem1(string filename, string outFilename)
{
   int cases = 0;

   ifstream inFile(filename);
   ofstream outFile(outFilename);
   inFile >> cases;

   for (int c = 0; c < cases; c++)
   {
      int numButtons = 0;
      inFile >> numButtons;

      vector<int> oOrders;
      vector<int> bOrders;
      vector<char> orders;

      for (int j = 0; j < numButtons; j++)
      {
         char color;
         int buttonNum;
         inFile >> color;
         inFile >> buttonNum;

         orders.push_back(color);
         if (color == 'O') oOrders.push_back(buttonNum);
         else bOrders.push_back(buttonNum);
      }

      int oPos = 1;
      int bPos = 1;
      int time = 0;

      size_t orderPos = 0;
      size_t oOrderPos = 0;
      size_t bOrderPos = 0;

      while (true)
      {
         time++;
         bool oButtonPushed = false;
         bool bButtonPushed = false;

         if (orders[orderPos] == 'O' && oOrders.size() > 0 && oPos == oOrders[oOrderPos])
         {
            //cout << time << " O push button " << oPos << endl;
            oButtonPushed = true;
            orderPos++;
            oOrderPos++;
         }
         else if (orders[orderPos] == 'B' && bOrders.size() > 0 && bPos == bOrders[bOrderPos])
         {
            //cout << time << " B push button " << bPos << endl;
            bButtonPushed = true;
            orderPos++;
            bOrderPos++;
         }
         if (orderPos >= orders.size()) break;

         if (!oButtonPushed && oOrders.size() > 0)
         {
            if (oPos < oOrders[oOrderPos]) { oPos++; }
            else if (oPos > oOrders[oOrderPos]) { oPos--; }
            //else { cout << time << " O stay at button " << oPos << endl; }
         }

         if (!bButtonPushed && bOrders.size() > 0) 
         {
            if (bPos < bOrders[bOrderPos]) { bPos++; }
            else if (bPos > bOrders[bOrderPos]) { bPos--; }
            //else { cout << time << " B stay at button " << bPos << endl; }
         }

      }

      cout << "Case #" << c+1 << ": " << time << endl;
      outFile << "Case #" << c+1 << ": " << time << endl;
   }
}

int main(int argc, char *argv[])
{
   problem1("A-large.in", "A-large.out");
}