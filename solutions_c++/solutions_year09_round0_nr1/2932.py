#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::sort;

int main() {

  int L, D, N;

  cin >> L;
  cin >> D;
  cin >> N;

  cin.ignore();

  vector<string> words(D);

  for (int i=0; i < D; ++i) {
    cin >> words[i];
    cin.ignore();
  }

  sort(words.begin(), words.end());

  vector<string> queries(N);

  for (int i=0; i < N; ++i) {
    cin >> queries[i];
    cin.ignore();
  }

  // generate answers

  vector<int>  answers(N, 0);

  for (int i=0; i < N; ++i) {

    // read pattern components
    vector<string> pattern(L);
    bool in_paren = false;
    int paren_start_index;
    int l= 0;
    for (int j=0; j < queries[i].length(); ++j) {
      if ( queries[i][j] == '(' ) {
	in_paren = true;
	paren_start_index = j+1;
      }
      if (!in_paren) {
	pattern[l++] = string(queries[i].begin() + j, queries[i].begin() + j+1);
      }
      else if ( queries[i][j] == ')') {
	in_paren = false;
	pattern[l++] = string(queries[i].begin() + paren_start_index,
			      queries[i].begin() + j);
      }
    }

    /*
    for (int j=0; j<L; ++j)
      cout << pattern[j] << " ";
    cout << endl;
    */

    for (int j = 0; j < D; ++j) {
      bool found = false;
      for (int k = 0; k < L; ++k) {
	found = false;
	for (int l=0; l < pattern[k].length(); ++l) {
	  if ( words[j][k] == pattern[k][l] ) {
	    found = true;
	    continue;
	  }
	}
	if (found == false) {
	  break;
	}
      }
      if (found == true) {
	++answers[i];
      }
    }

    /*
    vector<int> index(L, 0);

    string candidate(L, '0');

    vector<string> candidates;

    int c = L - 1;  // c is the current component of the pattern;
    while ( c >= 0 ) {

      for (int j=0; j<L; ++j) {
	candidate[j] = pattern[j][index[j]];
      }
      
      //cout << candidate << endl;
      //if ( find(words.begin(), words.end(), candidate) != words.end() )
      //answers[i]++;

      //candidates.push_back(candidate);
      
      if ( index[c] == pattern[c].length() - 1) {
	// we've hit the end
	// now go back, resetting indexes
	while ( c >= 0 && index[c] == pattern[c].length() - 1) {
	  index[c] = 0;
	  c--;
	}
	if ( c >= 0 ) {
	  index[c]++;
	  c = L - 1;
	}
      }
      else {
	index[c]++;
      }
    }
    */
  }
  

  for (int i=0; i < N; ++i) {
    cout << "Case #" << i+1 << ": " << answers[i] << endl;
  }

  return 1;
}
