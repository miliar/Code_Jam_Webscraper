#include <iostream>
#include <map>
#include <string>
using namespace std;

int L, D, N;
string lang[5010];

int main()
{
  cin >> L >> D >> N;

  for (int i = 0; i < D; i++) {
    cin >> lang[i];
  }

  string pattern;
  int count;

  for (int i = 0; i < N; i++) {
    cin >> pattern;
    count = 0;

    for (int k = 0; k < D; k++) {
      for (int j = 0, ix = 0; j < (int) pattern.size(); j++, ix++) {
	
	if (pattern[j] == '(') {
	  bool match = false;

	  while (pattern[j] != ')') {
	   
	    if (pattern[j] == lang[k][ix]) {
	      match = true;

	      while (pattern[j] != ')') ++j;
	      break;
	    }
	    ++j;
	  }

	  if (! match) {
	    //cout << "didnt match 1" << endl;
	    break;
	  }

	} else {
	  if (pattern[j] != lang[k][ix]) {
	    // cout << "didnt match 2" << endl;
	    break;
	  }
	}

	if (ix == L-1) {
	  ++count;
	}
      }
    }

    cout << "Case " << "#" << i+1 << ": " <<  count << endl;
  }

  return 0;
}
