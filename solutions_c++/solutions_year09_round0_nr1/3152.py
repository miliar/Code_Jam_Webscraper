#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <cstdlib>

using namespace std;

int readFile(vector<string> &dictionary, vector<string> &cases, int &numLetter, string fileName) {
  ifstream inFile;
  inFile.open(fileName.c_str());
  if (!inFile){
    cerr << "unable to open file " << fileName;
    exit(1);
  }
  inFile >> numLetter;
  int numWords;
  inFile >> numWords;
  int numCases;
  inFile >> numCases;
  string word;
  string combination;

  for (int i=0; i < numWords ; i++ ) {
    inFile >> word;
    dictionary.push_back(word);
  }

  for (int j=0; j < numCases; j++) {
    inFile >> combination;
    cases.push_back(combination);
  }
  inFile.close();
}


vector<string> readCase(string combination){
  vector<string> choices;
  if (combination.length() == 0 )
    return choices;
  int curr =0;
  while (curr < combination.length()){
    int pos = combination.find('(',curr);
    if (pos == -1) {
      for (int i=curr; i< combination.length() ;i++)
	choices.push_back(combination.substr(i,1));
      return choices;
    }
    else {
      for (int i= curr; i <pos; i++)
	choices.push_back(combination.substr(i,1));
      int posr = combination.find(')',curr);
      choices.push_back(combination.substr(pos+1,posr - pos -1));
      curr = posr +1;
    }
  }
  return choices;
}

 

bool testWord(vector<string> &choices, string word, int numLetter){
  for (int i=0; i < numLetter;i++){
    int pos = choices[i].find(word[i]);
    if (pos == -1) return false;
  }
  return true;
}

int countWords(string combination, vector<string> &dictionary, int numLetter){
  int count =0;
  vector<string> choices = readCase(combination);
  for (int i=0; i < dictionary.size();i++)
    if (testWord(choices, dictionary[i],numLetter)) count++;
  return count;
}

int main (){
  string fileName = "A-large.in";
  vector<string> dictionary;
  vector<string> cases;
  int numLetter;
  readFile(dictionary, cases, numLetter, fileName);
  for (int i=0; i<cases.size();i++)
    cout << "case #" << i+1 << ": " <<  countWords(cases[i], dictionary, numLetter) << endl; 
  return 0;
}
