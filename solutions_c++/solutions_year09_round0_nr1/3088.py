#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int findIn(char ch, char *array, int length) {
  for(int i = 0; i < length; i++)
    if(array[i] == ch)
      return i;
  return -1;
}

int main(int argc, char **argv) {
  char *infile = argv[1], *outfile = argv[2];
  ifstream fin(infile);
  ofstream fout(outfile);
  
  int length, nWords, nCases;
  fin >> length >> nWords >> nCases;
  
  string words[nWords];
  
  for(int i = 0; i < nWords; i++) {
    fin >> words[i];
    //    cout << words[i] << "\n";
  }
  
  for(int caseNum = 1; caseNum <= nCases; caseNum++) {
    string trans;
    fin >> trans;
    //    cout << "\n" << trans << "\n";
    int ind = 0, end = 0;
    int *lengths = new int[length];
    char **letters = new char*[length];     //012345678
    for(int i = 0; i < length; i++) {       //(ab)d(cd)
      if(trans[ind] == '(') {
	ind++;
	end = ind;
	while(trans[end] != ')')
	  end++;
	letters[i] = new char[end-ind];
	lengths[i] = end-ind;
	for(int j = 0; j < end-ind; j++)
	  letters[i][j] = trans[ind+j];
      }
      else {
	letters[i] = new char[1];
	letters[i][0] = trans[ind];
	lengths[i] = 1;
	end = ind;
      }
      ind = end+1;
    }
    
    /*    for(int i = 0; i < length; i++) {
	  for(int j = 0; j < length; j++) {
	  cout << letters[i][j];
	  }
	  cout << "\t" << lengths[i] << "\n";
	  }
    */

    int nValid = 0;
    
    for(int j = 0; j < nWords; j++) {
      int valid = 1;
      string word = words[j];
      for(int i = 0; i < word.size(); i++) {
	if(findIn(word[i], letters[i], lengths[i]) == -1)
	  valid = 0;
      }
      if(valid)
	nValid++;
    }

    fout << "Case #" << caseNum << ": " << nValid << "\n";
  }
}

