#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
  int T;
  cin >> T;
  for(int tcase=1;tcase<=T;tcase++) {
    cout << "Case #" << tcase << ": ";
    string cur;
    cin >> cur;
    //std::cerr << "\"" << cur << "\"";
    bool done = false;
    for(int i=cur.size()-1;i>=1;i--)
      if(cur[i] > cur[i-1]) {
	for(int j=cur.size()-1;j>=i;j--)
	  if(cur[j] > cur[i-1]){
	    swap(cur[j], cur[i-1]);
	    break;
	  }
	//std::cerr << i << "!\n";
	if(i+1!=cur.size())
	  sort(cur.begin()+i, cur.end());
	done = true;
	break;
      }
    if(done) cout << cur << '\n';
    else {
      cur.push_back('0');
      sort(cur.begin(), cur.end());
      if(cur[0] == '0') {
	for(size_t i=0;i<cur.size();i++)
	  if(cur[i] != '0') {
	    swap(cur[i], cur[0]);
	    break;
	  }
      }
      cout << cur << '\n';
    }
  }
  return 0;
}
