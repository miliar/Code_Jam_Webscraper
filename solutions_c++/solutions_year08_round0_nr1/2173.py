/**
* Author: Byte Freezer
* Created: July 17, 2008
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
string findOptimal(vector<string>, vector<string>, int);
string intToStr(int);

int main()
{
  int caseNum, caseCounter = 0, 
      engineNum, engineCounter = 0, 
      queryNum, queryCounter = 0,
      switchCounter = 0;
  ifstream inputFile;
  string tmpLine;
  vector<string> engineVector, queryVector, outputVector;
  
  inputFile.close();
  inputFile.clear();
  
  inputFile.open(FILENAME);
  
  //pre process
  getline(inputFile, tmpLine, DELIM_NL);
  caseNum = atoi(tmpLine.c_str());
  cout << caseNum << endl;
  
  while(caseCounter < caseNum)
  {
    getline(inputFile, tmpLine, DELIM_NL);
    engineNum = atoi(tmpLine.c_str());
    cout << engineNum << endl;
    
    while(engineCounter < engineNum)
    {
      getline(inputFile, tmpLine, DELIM_NL);
      engineVector.push_back(tmpLine);
      cout << tmpLine << endl;
      ++engineCounter;
    }
    
    getline(inputFile, tmpLine, DELIM_NL);
    queryNum = atoi(tmpLine.c_str());
    cout << queryNum << endl;
    
    while(queryCounter < queryNum)
    {
      getline(inputFile, tmpLine, DELIM_NL);
      queryVector.push_back(tmpLine);
      cout << tmpLine << endl;
      ++queryCounter;
    }
    
    //process
    string optimal = findOptimal(engineVector, queryVector, 0);
    cout << ">> OPTIMAL: " << optimal << endl;
    switchCounter = 0;
    string tmpOut = "";
    for(size_t i = 0; i < queryVector.size(); ++i)
    {
      if(optimal == queryVector.at(i))
      {
        optimal = findOptimal(engineVector, queryVector, i);
        --i;
        cout << ">> OPTIMAL: " << optimal << endl;
        ++switchCounter;
      }
    }
    tmpOut += "Case #";
    tmpOut += intToStr(caseCounter+1);
    tmpOut += ": ";
    tmpOut += intToStr(switchCounter);
    outputVector.push_back(tmpOut);
    
    //post process
    engineVector.clear();
    queryVector.clear();
    engineCounter = 0; 
    queryCounter = 0;
    ++caseCounter;
  }
  
  //write file
  ofstream outputFile;
  outputFile.open(OUTPUTFILE);
  
  for(size_t i = 0; i < outputVector.size(); ++i)
  {
    outputFile << outputVector.at(i) << endl;
  }
}

string findOptimal(vector<string> engines, vector<string> queries, int startPos)
{
  string optimalEngine;
  int max = 0, counter = 0;
  bool found = false;
  
  for(size_t i = 0; i < engines.size(); ++i)
  {
    counter = 0;
    found = false;
    for(size_t j = startPos; j < queries.size(); ++j)
    {
      if(engines.at(i) != queries.at(j))
        ++counter;
      else
      {
        if(counter > max)
        { 
          max = counter;
          optimalEngine = engines.at(i);
        }
        found = true;
        break;
      }
    }
    if(!found)
    {
      max = counter;
      optimalEngine = engines.at(i);
      found = false;
    }
  }
  
  return optimalEngine;
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