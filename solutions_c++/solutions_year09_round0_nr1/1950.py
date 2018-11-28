#include <fstream>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <list>

using namespace std;

int main()
{
  int L, D, N;
  list <string> dict;
  list<char> *comb;
  string word;
  string::iterator it;
  list<string>::iterator it2;
  char c;
  
  cin >> L;
  cin >> D;
  cin >> N;

  // store words in linked list
  for (int i = 0; i < D; i++ ) {
    cin >> word;
	dict.push_back(word);
  }
  // sort dictionary
  dict.sort();

  // loop through all cases
  for (int i = 0; i < N; i++) {
    int K = 0;
    // get word
	cin >> word;
	comb = new list<char>[L];
	int ind = 0;
	// loop through chars in word storing in comb
	for (it = word.begin(); it < word.end(); it++) {
	  c = *it;
      // no uncertainty
	  if (c != *("("))
	    comb[ind].push_back(c);
	  // "("
	  else {
	    while (*it != *(")")) {
		  it ++;
		  c = *it;
		  comb[ind].push_back(c);
		}
      }
	  ind ++;
    }
	// check all words in dict
	for (it2 = dict.begin(); it2 != dict.end(); it2++) {
	  word = *it2;
	  // compare letters of word with possible letters
	  bool next = false;
	  int k = 0;
	  it = word.begin();
	  while (next == false) {
	    // no matching letter
	    if (find(comb[k].begin(),comb[k].end(),*it) == comb[k].end()) {
		  next = true;
		} 
		// matched letter
		else {
		  it ++;
		  k ++;
          // finished matching word
		  if (k == L) {
		    next = true;
			K++;
		  }
		}
      }
	}
	cout << "Case #" << i+1 << ": " << K << endl;
  }
  
  return 0;
}
