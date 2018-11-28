#include<iostream>
#include<vector>
#include<map>
using namespace std;

typedef vector<char> Vc;
typedef vector<Vc> Mc;
typedef vector<bool> Vb;
typedef vector<Vb> Mb;

int main() {
  int t,c,d,n;
  cin >> t;
  map<char,int> m;
  m['Q'] = 1;
  m['W'] = 2;
  m['E'] = 3;
  m['R'] = 4;
  m['A'] = 5;
  m['S'] = 6;
  m['D'] = 7;
  m['F'] = 8;
  for(int i = 0; i < t; ++i) {
	  Mc comb(9,Vc(9,'/'));
  Mb op(9,Vb(9,false));
    cin >> c;
    for(int j = 0; j < c; ++j) {
      char c1,c2,c3;
      cin >> c1 >> c2 >> c3;
      comb[m[c1]][m[c2]] = c3;
      comb[m[c2]][m[c1]] = c3;
    }
    cin >> d;
    for(int j = 0; j < d; ++j) {
      char c1,c2;
      cin >> c1 >> c2;
      op[m[c1]][m[c2]] = true;
      op[m[c2]][m[c1]] = true;
    }
    cin >> n;
    vector<char> v;
    for(int j = 0; j < n; ++j) {
      char c;
      cin >> c;
      if(not v.empty()) {
		char co;
		int size = v.size();
		co = comb[m[c]][m[v[size-1]]];
		if(co != '/') {
			v.pop_back();
			v.push_back(co);
		}
		else {
			bool oppo = false;
			for(int k = 0; k < size and not oppo; ++k) {
				if(op[m[c]][m[v[k]]]) oppo = true;
			}
			if(oppo){
				v.clear();
			}
			else {
				v.push_back(c);
			}
		}
      }
      else v.push_back(c);
    }
    int size = v.size();
    cout << "Case #"<< i+1 << ": [";
    if(size > 0) cout << v[0];
    for(int j = 1; j < size; ++j) {
      cout << ", " << v[j]; 
    }
    cout << "]" << endl;
  }
}