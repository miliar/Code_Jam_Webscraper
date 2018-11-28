/**
* Author: Byte Freezer
* Created: July 27, 2008
* Usage: plz name the input file as input.txt
*/
#include <iostream>
using std::cout;
using std::endl;

#include <fstream>
using std::ifstream;
using std::ofstream;

#include <vector>
using std::vector;

#include <string>
using std::string;

const char DELIM_NL = '\n';
const char* FILENAME = "input.txt";
const char* OUTPUTFILE = "output.txt";
const int CHARBUFSIZE = 100;

//prototypes
string intToStr(int);
int findMax(vector<int>*);

int main()
{
  ifstream inputFile;
  ofstream outputFile;
  string tmpLine;
  vector<int> *freq = new vector<int>;
  int caseNum, caseCounter = 0,
      P, K, L,
      letterCounter = 0;
  
  inputFile.close();
  inputFile.clear();
  
  inputFile.open(FILENAME);
  //write file  
  outputFile.open(OUTPUTFILE);
  
  getline(inputFile, tmpLine, DELIM_NL);
  caseNum = atoi(tmpLine.c_str());
  cout << caseNum << endl;
  
  int tmpFreq, currentMax, keyPressedNum = 0;;
  
  while(caseCounter < caseNum)
  {
    outputFile << "Case #" << caseCounter+1 << ": ";
    keyPressedNum = 0;
    letterCounter = 0;
    inputFile >> P >> K >> L;
    inputFile.ignore();
    cout << P << " " << K << " " << L << endl;
    
    while(letterCounter < L)
    {
      inputFile >> tmpFreq;
      freq->push_back(tmpFreq);
      ++letterCounter;
    }
    inputFile.ignore();
    
    //process
    for(int i = 1; i <= P; ++i)
    {
      for(int j = 1; j <= K; ++j)
      {
        currentMax = findMax(freq);
        keyPressedNum += currentMax*i;
      }
    }
    cout << keyPressedNum << endl;
    outputFile << keyPressedNum << endl;
    freq->clear();
    ++caseCounter;
  } 
  
  
  
}

int findMax(vector<int> *freq)
{
  if(freq->size() == 0)
    return 0;
  int max = freq->at(0), maxLocale = 0;
  for(unsigned int i = 1; i < freq->size(); ++i)
  {
    if(freq->at(i) > max)
    {
      max = freq->at(i);
      maxLocale = i;
    }
  }
  
  freq->erase(freq->begin()+maxLocale);
  return max;
}

string intToStr(int val) 
{
  char *buf;
  string intInStr;

  // new array of char
  buf = new char[CHARBUFSIZE];
  // clear the buf
  memset(buf,'\0',CHARBUFSIZE);

  // convert
  itoa(val,buf,10);

  // put the buffer into string
  intInStr = buf;
  
  // clear buf
  delete[] buf;

  return(intInStr);
}