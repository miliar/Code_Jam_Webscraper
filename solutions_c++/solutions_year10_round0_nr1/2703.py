

#include <iostream>
#include <fstream>
#include <list>
#include <cmath>

using namespace std;
string resolver(int snaps, int boxes)
{
   string result = "OFF";
   bool res = true;
   int num = 1 << (boxes + 1);
   
   res = snaps > 0 &&  (snaps - num +1)  % (num >> 1) == 0;
   if(res)
   {
      result = "ON";
   }
   return result;
}
int main()
{
   ifstream input("A-small.in");
   ofstream output("output.out");
   int n;
   input >> n;
   for(int i(0); i < n; ++i)
   {
      int snaps, boxes;
      input >> boxes >> snaps;
      output << "Case #" << i+1 << ": " << resolver(snaps, boxes) << endl;
   }
}
