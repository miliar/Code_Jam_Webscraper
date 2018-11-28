#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <map>

using namespace std;

long long GetMinNumberSeconds(string p_tokenString)
{
   map<char,int> l_map;
   int l_charCode=2;
   int l_first = false;
   int l_second = false;
   int numSize = p_tokenString.size();

   for(int i=0; i<p_tokenString.length(); ++i)
   {
      if(l_map.find(p_tokenString[i]) == l_map.end())
      {
         if(numSize == 1)
         {
            if (!l_first)
               l_map.insert(std::pair<char,int>(p_tokenString[i], 1));
            break;
         }
         else
         {
            if (!l_first)
            {
               l_map.insert(std::pair<char,int>(p_tokenString[i], 1));
               l_first = true;
            }
            else if(!l_second)
            {
               l_map.insert(std::pair<char,int>(p_tokenString[i], 0));
               l_second = true;
            }
            else
            {
               l_map.insert(std::pair<char,int>(p_tokenString[i], l_charCode));
               ++l_charCode;
            }
         }
      }
   }

   int base = l_map.size();
   long long result = 0;

   base = base > 1 ? base : 2;

   for (int i=0; i<p_tokenString.length(); ++i)
   {
      result = result * base + l_map.find(p_tokenString[i])->second;
   }

   return result;
}

int main()
{
   string l_inFileName = "./Debug/A-large.in";
   string l_outFileName = "./Debug/A-large.out";
   ifstream l_inFilesStream;
   ofstream l_outFileStream;

   l_inFilesStream.open(l_inFileName.c_str());
   l_outFileStream.open(l_outFileName.c_str());

   if (l_inFilesStream && l_outFileStream)
   {
      if (!l_inFilesStream.eof())
      {
         string l_readLine;
         string l_tokenString;
         int l_numTestCases = -1;

         getline(l_inFilesStream, l_readLine);

         stringstream l_stringStream(l_readLine);

          // Get the number of test cases
         getline(l_stringStream, l_tokenString, ' ');
         l_numTestCases = atoi(l_tokenString.c_str());

         // Check the minimum number of seconds for each test case.
         for (int l_itest = 0; l_itest < l_numTestCases; ++l_itest)
         {
            getline(l_inFilesStream, l_tokenString);

            long long result = GetMinNumberSeconds(l_tokenString);
            l_outFileStream << "Case #" << (l_itest+1) << ": " << result << endl;
            cout << "Case #" << (l_itest+1) << ": " << result << endl;
         }
      }
      else
      {
         cout << "File is empty" << endl;
      }
   }
   else
   {
      if (!l_inFilesStream)
         cout << "Input file couldn't be opened" << endl;
      else
         cout << "Output file couldn't be opened" << endl;

      return -1;
   }

   return 0;
}
