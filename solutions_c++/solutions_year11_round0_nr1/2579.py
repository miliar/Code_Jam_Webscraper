#include<iostream>
using namespace std;

int main() {
  int t,n;
  cin >> t;
  for(int i = 0; i < t; ++i) {
    cin >> n;
    int s = 0;
    int to = 0;
    int tb = 0;
    int po = 1;
    int pb = 1;
    for(int j = 0; j < n; ++j) {
      char c;
      int b;
      cin >> c >> b;
      if(c == 'O') {
	int p = b-po;
	if(p < 0) p = -p;
	p -= to;
	if(p < 0) p = 0;
	++p;
	s +=p;
	to = 0;
	tb += p;
	po = b;
      }else {
	int p = b-pb;
	if(p < 0) p = -p;
	p -= tb;
	if(p < 0) p = 0;
	++p;
	s +=p;
	tb = 0;
	to += p;
	pb = b;
      }
    }
    cout << "Case #"<< i+1 << ": " << s << endl;
  }
}