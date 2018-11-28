#include <iostream>
#include <string>

using namespace std;

const int maxd = 5000;
const int maxl = 15;
const int maxn = 500;


int l, d, n;
string words[maxd];
bool current[maxl][26];

int main() {
  cin >> l >> d >> n;
  for(int i=0;i<d;i++)
    cin >> words[i];
  for(int curt=0;curt<n;curt++){
    string t;
    cin >> t;
    int size = 0;
    bool open = false;
    for(size_t j=0;j<t.size();j++)
      if(t[j]==')') {
	size++;
	open = false;
      } else if(t[j] =='('){
	open = true;
	for(int i=0;i<='z'-'a';i++)
	  current[size][i] = false;
      } else {
	if(!open) {
	  for(int i=0;i<='z'-'a';i++)
	    current[size][i] = false;
	}
	current[size][t[j]-'a'] = true;
	if(!open) size++;
      }
    int res = 0;
    for(int i=0;i<d;i++){
      if(words[i].size()!=size) continue;
      for(int j=0;j<size;j++)
	if(!current[j][words[i][j]-'a']) goto nope;
      res++;
    nope:;
    }
    cout << "Case #" << curt + 1 << ": " << res << '\n';
  }
}
