#include <iostream>
#include <cassert>
#include <vector>
#define ALP 256
#define PB push_back
using namespace std;
char form[ALP][ALP];
bool opos[ALP][ALP];
void mix(vector<char>& v) {
    while(v.size() > 1) {
        char c1 = v.back(); v.pop_back();
        char c2 = v.back(); v.pop_back();
        if(form[c1][c2])
	  v.PB(form[c1][c2]);
        else {
	  v.PB(c2);
	  v.PB(c1);
	  break;
        }
    }
}

void check(vector<char>& v) {
    for(int i=0; i<v.size(); i++)
        for(int j=i+1; j<v.size(); j++) {
	  if(opos[v[i]][v[j]]) {
	      v.clear();
	      return;
	  }
        }
}

int main() {
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    for(int z=1; z<=T; z++) {
        for(int i=0; i<ALP; i++)
	  for(int j=0; j<ALP; j++) {
	      form[i][j] = 0;
	      opos[i][j] = false;
	  }
        int ilef;
        cin >> ilef;
        while(ilef--) {
	  string s;
	  cin >> s;
	  assert(s.size() == 3);
	  form[s[0]][s[1]] = s[2];
	  form[s[1]][s[0]] = s[2];
        }
        
        int ileo;
        cin >> ileo;
        while(ileo--) {
	  string s;
	  cin >> s;
	  assert(s.size() == 2);
	  opos[s[0]][s[1]] =  true;
	  opos[s[1]][s[0]] =  true;
        }
        
        cin >> ileo;
        vector<char> v;
        while(ileo--) {
	  char c;
	  cin >> c;
	  v.PB(c);
	  mix(v);
	  check(v);
        }
        cout << "Case #" << z << ": [";
        for(int i=0; i<(int)v.size()-1; i++) {
	  cout << v[i] << ", ";
        }
        if(!v.empty())
	  cout << v.back();
        cout << "]" << endl;
    }
    return 0;
}