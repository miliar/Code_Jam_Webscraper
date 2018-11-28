/* 0:10 -> 1:50
   Rafael Schimassek 
*/

#define MAX_LETTERS 20
#define MAX_WORDS 5100
#define MAX_CASES 600

#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string dict [MAX_WORDS];
char word [MAX_LETTERS][30];
int countword [MAX_LETTERS];
char inputword [512];
int countcases [MAX_CASES];
int num_letters, num_words, num_cases;

/*int pos;
void searchThrough(int cc, int tier, char lastchar) {
  if ((tier + 1) >= num_letters) {
    ++countcases[cc];
    //cout << countcases[cc] << ".."<<dict[pos]<<'\n';
    ++pos;
    //return ++pos;
  }
        
  //search through all letters
  //cout << cc << " | " << tier << " | " << pos << " | " << lastchar << '\n';
  int a; bool match;
  for (; dict[pos][tier - 1] == lastchar && pos < num_words;) {
    match = false;
    for (a = 0; a < countword[tier]; ++a) {
      //cout << "WORD: " << word[tier][a]<<'\n';
      if (dict[pos][tier] == word[tier][a]) {
        //cout << "MATCH: "<<word[tier][a] << '\n';
        match = true;
        searchThrough(cc, tier + 1, word[tier][a]);
        break;
      }
    }
    if (!match) ++pos;
  }
  //cout << "POS: " << pos << '\n';
  //return pos;
}*/


int main () {
  
  int a, b, c, cc, tier, pos, casecount;
  bool found;
  
  //get initial data
  cin >> num_letters >> num_words >> num_cases;
  //get words
  for (a = 0; a < num_words; ++a)
    cin >> dict[a];
  sort(dict, dict + num_words);
  
  /*cout << "DICT:\n";
  for (a = 0; a < num_words; ++a)
    cout << dict[a] << '\n';*/
  
  //get cases
  for (cc = 0; cc < num_cases; ++cc) {
    cin >> inputword;
    
    for (a = 0; a < num_letters; ++a)
      countword[a] = 0;
    
    //break input word
    a = 0; tier = 0;
    while (inputword[a] != '\0') {
      if (inputword[a] == '(') {
        for (a += 1; inputword[a] != ')'; ++a) {
          word[tier][countword[tier]] = inputword[a];
          ++countword[tier];
        }
      }
      else {
        word[tier][countword[tier]] = inputword[a];
        ++countword[tier];
      }
      //sort(word[tier], word[tier] + countword[tier]);
      ++a; ++tier;
    }
    
    //output test
    /*cout << "CASE " << cc << '\n';
    for (a = 0; a < num_letters; ++a) {
      cout << a << ": ";
      for (int b = 0; b < countword[a]; ++b)
        cout << word[a][b];
      cout << "(" << countword[a] << ")" << '\n';
    }*/
    
    //count the possibilities
    tier = 0; pos = 0, casecount = 0;
    for (a = 0; a < num_words; ++a) {
      for (b = 0; b <= num_letters; ++b) {
        if (b == num_letters) {
          found = true;
          break;
        }
        found = false;
        for (c = 0; c < countword[b]; ++c) {
          if (dict[a][b] == word[b][c]) {
            found = true;
            break;
          }
        }
        if (found == false) {
          //cout << "Broke at "<<dict[a]<<": "<<b<<dict[a][b]<<" not found\n";
          break;
        }
      }
      if (found == true)
        ++casecount;
    }
    
    cout << "Case #" << (cc+1) << ": "<<casecount<<'\n';
    
  }
  
  /*/output results
  for (cc = 0; cc < num_cases; ++cc)
    cout << "Case #" << (cc + 1) << ": "<<countcases[cc]<<'\n';*/
  
  return 0;
}
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
