#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<vector<char> > FindPatterns(string p_pattern,int p_numCharsInPattern)
{
   vector<string> l_vecOfPossiblePatterns;
   stringstream l_strStream(p_pattern);
   string l_tokenString;
   int l_inumCharsRead = 0;
   vector< vector<char> > l_vecOfvecOfChar;

   while(l_inumCharsRead < p_numCharsInPattern)
   {
      getline(l_strStream, l_tokenString, '(');
      for (int l_i = 0; l_i < l_tokenString.size(); ++l_i, ++l_inumCharsRead)
      {
         vector<char> l_vecOfChar;

         l_vecOfChar.push_back(l_tokenString[l_i]);
         l_vecOfvecOfChar.push_back(l_vecOfChar);
      }

      if (l_inumCharsRead < p_numCharsInPattern)
      {
         vector<char> l_vecOfChar;
         getline(l_strStream, l_tokenString, ')');
         for (int l_i = 0; l_i < l_tokenString.size(); ++l_i)
            l_vecOfChar.push_back(l_tokenString[l_i]);

         l_vecOfvecOfChar.push_back(l_vecOfChar);
         ++l_inumCharsRead;
      }
   }

   return l_vecOfvecOfChar;
}

int CheckPossibleInterpretation4Pattern(vector<vector<char> > p_vecOfVecOfChar, vector<string> p_dictionary, 
                                        vector<int> p_vectorOfIndices)
{
   int l_numOccurrence = 0;
   bool l_found = false;
   vector<int> l_vecOfIndices;
   vector<int> l_tempVector;

   l_vecOfIndices.assign(p_vectorOfIndices.begin(), p_vectorOfIndices.end());

   for(int l_i = 0; l_i < p_vecOfVecOfChar.size(); ++l_i)
   {
      l_found = false;

      for (int l_j = 0; l_j < p_vecOfVecOfChar[l_i].size(); ++l_j)
      {
         char ch = p_vecOfVecOfChar[l_i][l_j];
         
         for (int l_k=0; l_k < l_vecOfIndices.size(); ++l_k)
         {
            if (ch == p_dictionary[l_vecOfIndices[l_k]][l_i])
            {
               l_found = true;
               l_tempVector.push_back(l_vecOfIndices[l_k]);
            }
         }
      }

      if (l_found == false)
         return 0;
      else
      {
         l_vecOfIndices.clear();
         l_vecOfIndices.assign(l_tempVector.begin(), l_tempVector.end());
         l_tempVector.clear();         
      }
   }

   return l_vecOfIndices.size();
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
         vector<string> l_dictionary;
         int l_numChars = -1;
         int l_numWords = -1;
         int l_numTestCases = -1;
         vector<int> l_vecOfIndices;

         getline(l_inFilesStream, l_readLine);

         stringstream l_stringStream(l_readLine);

         // Get the number of possible letters
         getline(l_stringStream, l_tokenString, ' ');
         l_numChars = atoi(l_tokenString.c_str());

         // Get the number of words in an Alien Dictionary
         getline(l_stringStream, l_tokenString, ' ');
         l_numWords = atoi(l_tokenString.c_str());

         for (int l_i=0; l_i<l_numWords; ++l_i)
            l_vecOfIndices.push_back(l_i);

         // Get the number of test cases
         getline(l_stringStream, l_tokenString, ' ');
         l_numTestCases = atoi(l_tokenString.c_str());

         // Store the words in a vector. Here vector represents the dictionary of alien words.
         for (int l_iword=0; l_iword < l_numWords && !l_inFilesStream.eof(); ++l_iword)
         {
            getline(l_inFilesStream, l_readLine);
            l_dictionary.push_back(l_readLine);
         }

         // Check the dictionary for each test case.
         for (int l_itest = 0; l_itest < l_numTestCases; ++l_itest)
         {
            getline(l_inFilesStream, l_readLine);

            if (l_readLine.empty())
            {
               --l_itest;
               continue;
            }

            vector<vector<char> > l_vecOfvecOfChar = FindPatterns(l_readLine, l_numChars);

            int l_numSuccess = CheckPossibleInterpretation4Pattern(l_vecOfvecOfChar, l_dictionary, l_vecOfIndices);

            l_outFileStream << "Case #" << (l_itest+1) << ": " << l_numSuccess << endl;
            cout << "Case #" << (l_itest+1) << ": " << l_numSuccess << endl;
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