// Template for code jam!
//
#include "stdafx.h"
//#include <math.h>
#include <fstream>
#include <string>
#include <vector>
//#include <map>
//#include <queque>
//#include <stack>
//#include <set>
#include <algorithm>

using namespace std;

//other functions may go here!

//main function!

void findWords(string word, int pos, vector<string>& wordsList, int vecBegin, int vecEnd, int& count)
{
  if(word[pos] != '(')
  {
      if(pos+1 < word.size())
	  {  
		  int x, y;
		  for(x=vecBegin; x<vecEnd && word[pos] != wordsList[x][pos]; x++);
          if(x == vecEnd) return;
		  for(y=x; y<vecEnd && word[pos] == wordsList[y][pos]; y++);
		  if(y>x)
		    findWords(word, ++pos, wordsList, x, y, count);
	  }
	  else if(word == wordsList[vecBegin])
	    count++;
  }
  else
  {
    int posEnd = pos+2;
	while(word[posEnd] != ')')
		posEnd++;
	for(int x=pos+1; x < (posEnd); x++)
	{
	  int a, b;
	  for(a=vecBegin; a<vecEnd && word[x] != wordsList[a][pos]; a++);
      if(a < vecEnd)
	  {
		for(b=a; b<vecEnd && word[x] == wordsList[b][pos]; b++);
	    findWords((word.substr(0, pos)+word[x]+word.substr(posEnd+1, word.size()-posEnd-1)), pos+1, wordsList, a, b, count);
	  }
	}
  }
}

int _tmain(int argc, _TCHAR* argv[])
{
    ifstream inputFile("A-large.txt");
    ofstream outputFile("A-largeout.txt", std::ios::trunc);
    if((!inputFile.is_open()) || (!outputFile.is_open()))
    {
      //error openning input/output file!
      return 0;
    }
    vector<string> wordsList;
	string word;
	int sizeWords, numWords, numCases;
	inputFile >> sizeWords;
	inputFile >> numWords;
	inputFile >> numCases;

		//parsing code goes here
        wordsList.clear();
		for(int x=0; x<numWords; x++)
		{
			inputFile >> word;
			wordsList.push_back(word);
		}
		sort(wordsList.begin(), wordsList.end());
     
		//problem code goes here
        for(int x=1; x<=numCases; x++)
		{
		  int count = 0;
		  inputFile >> word;
		  findWords(word, 0, wordsList, 0, numWords, count);
		  outputFile << "Case #" << x << ": " << count << endl;
		}
	return 0;
}

