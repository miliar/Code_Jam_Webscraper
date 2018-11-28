#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char *argv[])
{
   string filename = "B-large";
   ifstream inFile(filename + ".in");
   ofstream outFile(filename + ".out");
   int cases = 0;
   inFile >> cases;

   for (int c = 0; c < cases; c++)
   {
      int numCombines = 0;
      inFile >> numCombines;

      vector<string> combinations;
      vector<string> oppositions;

      for (int n = 0; n < numCombines; n++)
      {
         string combine;
         inFile >> combine;
         combinations.push_back(combine);
      }

      int numOpposed = 0;
      inFile >> numOpposed;
      for (int n = 0; n < numOpposed; n++)
      {
         string opposed;
         inFile >> opposed;
         oppositions.push_back(opposed);
      }

      int dummy;
      inFile >> dummy;

      string invokeString;
      inFile >> invokeString;

      string resultString = "";
      resultString += invokeString[0];

      for (size_t i = 1; i < invokeString.length(); i++)
      {
         char currChar = invokeString[i];
         char prevChar = resultString[resultString.length()-1];
         bool combined = false;
         for (size_t j = 0; j < combinations.size(); j++)
         {
            if ((combinations[j][0] == currChar && combinations[j][1] == prevChar) || (combinations[j][0] == prevChar && combinations[j][1] == currChar))
            {
               resultString[resultString.length()-1] = combinations[j][2];
               combined = true;
               break;
            }
         }

         if (!combined) resultString += currChar;

         for (size_t j = 0; j < oppositions.size(); j++)
         {
            if (resultString.find(oppositions[j][0]) != string::npos && resultString.find(oppositions[j][1]) != string::npos)
            {
               resultString.clear();
               break;
            }
         }
      }

      string str = "";
      for (size_t j = 0; j < resultString.length(); j++)
      {
         if (!str.empty()) str += ", ";
         str += resultString[j];
      }
      cout << "Case #" << c+1 << ": [" << str << "]" << endl;
      outFile << "Case #" << c+1 << ": [" << str << "]" << endl;
   }
}