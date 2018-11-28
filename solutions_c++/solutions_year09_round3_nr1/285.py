#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::sort;

using std::map;

int main() {

  int T;

  cin >> T;
  cin.ignore();

  string N;

  for (int i=0; i < T; ++i) {
    cin >> N;
    cin.ignore();

    int len=N.length();
    vector<int> number(len);

    map<char, int> meaning_count;
    map<char, int> meaning;

    meaning_count[N[0]]=1;
    meaning[N[0]]=1;
    number[0]=1;
    int next_meaning=0;
    for (int j=1; j < len; ++j) {
      if ( meaning_count[N[j]] == 0) {
	meaning_count[N[j]]++;
	meaning[N[j]] = next_meaning;
	number[j]= next_meaning;
	next_meaning++;
	if ( next_meaning == 1 )
	  next_meaning++;
      }
      else {
	number[j] = meaning[N[j]];
	meaning_count[N[j]]++;
      }
    }

    long long ans = 0;
    long base;
    long factor;
    if ( next_meaning == 0 ) {
      base = 2;
    }
    else {
      base = next_meaning;
    }
    factor = 1;
    for (int j=len-1; j >= 0; --j) {
      ans += factor * number[j];
      factor *= base;
    }
    cout << "Case #" << i+1 << ": " << ans << endl;
  }

  return 0;
}
