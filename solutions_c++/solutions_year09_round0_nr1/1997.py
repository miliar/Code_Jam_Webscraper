#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

int NumberOfMatchingWords(vector<string> &dict, char pattern[15][27]) {
  int retval = 0;
  for(int i = 0; i < dict.size(); i++) {
    bool ismember = true;
    for(int j = 0; j < dict[i].size(); j++) {
      int k = 0;
      while(pattern[j][k] != 0 && pattern[j][k] != dict[i][j]) k++;
      if(pattern[j][k] == 0) {
	ismember = false;
	break;
      }
    }
    if(ismember) retval++;
  }
  return retval;
}

void ShowPattern(char pattern[][27], int rows) {
  cout << "====================" << endl;
  for(int i = 0; i < rows; i++) cout << pattern[i] << ":";
  cout << endl << "====================" << endl;
}

int main(int argc, char *argv[]) {
  if(argc < 2) return -1;
  
  ifstream infile(argv[1]);
  int wordlen = 0, diclen = 0, testcases = 0;
  infile >> wordlen;
  infile >> diclen;
  infile >> testcases;
  vector<string> words;
  string str;
  for(int i = 0; i < diclen; i++) {
    infile >> str; 
    words.push_back(str);
  }
  
  char pattern[15][27];
  for(int i = 0; i < testcases; i++) {
    memset(pattern, 0, 15*27*sizeof(char));
    infile >> str;
    int j = 0, k = 0;
    while(j < str.size()) {
      if(str[j] == '(') {
	j++;
	int counter = 0;
	while(str[j] != ')') pattern[k][counter++] = str[j++];
	j++;
      } else {
	pattern[k][0] = str[j++];
      }
      k++;
    }
    //ShowPattern(pattern, 15);
    cout << "Case #" << (i+1) << ": " << NumberOfMatchingWords(words, pattern) << endl;
  }

  infile.close();
  return 0;
}
