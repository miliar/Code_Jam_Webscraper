#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <list>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <stack>
using namespace std;

struct form {
  char c1, c2, f;
};

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    vector<form> combine;
    int C;
    cin >> C;
    for (int i = 0; i < C; i++) {
      form element;
      string str;
      cin >> str;
      element.c1 = str[0];
      element.c2 = str[1];
      element.f = str[2];
      combine.push_back(element);
    }

    vector<pair<char, char> > oppose;
    int D;
    cin >> D;
    for (int i = 0; i < D; i++) {
      pair<char, char> element;
      string str;
      cin >> str;
      element.first = str[0];
      element.second = str[1];
      oppose.push_back(element);
    }

    vector<char> magic;
    int N;
    cin >> N;
    string input;
    cin >> input;
    for (int i = 0; i < N; i++) {
      if (magic.size() == 0) {
	magic.push_back(input[i]);
      } else {
	// check combine
	char c = magic[magic.size() - 1];
	int j;
	for (j = 0; j < C; j++) 
	  if ( (combine[j].c1 == c &&
		combine[j].c2 == input[i]) ||
	       (combine[j].c2 == c &&
		combine[j].c1 == input[i])) {
	    magic[magic.size() - 1] = combine[j].f;
	    break;
	  }
	// check oppose
	int k;
	bool opp = 0;
	if (j == C) {
	  for (k = 0; k < D; k++) {
	    for (int pos = 0; pos < (int)magic.size(); pos++)
	      if ( (oppose[k].first == magic[pos] &&
		    oppose[k].second == input[i]) ||
		   (oppose[k].second == magic[pos] &&
		    oppose[k].first == input[i])) {
		magic.clear();
		opp = 1;
		break;
	      }
	    if (opp)
	      break;
	  }
	}
	if (j == C && !opp)
	  magic.push_back(input[i]);
      }
    }
    cout << "Case #" << t << ": [";
    for (int i = 0; i < (int) magic.size() - 1; i++)
      cout << magic[i] << ", ";
    if (magic.size() > 0)
      cout << magic[magic.size() - 1];
    cout << "]" << endl;
  }
  return 0;
}
