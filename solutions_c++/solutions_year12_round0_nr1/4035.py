#include<iostream>
#include<map>
using namespace std;

int main()
{
  map<char, char> M;
  string s1, s2;
  M[' '] = ' ';
  M['a'] = 'y';
  M['b'] = 'h';
  M['c'] = 'e';
  M['d'] = 's';
  M['e'] = 'o';
  M['f'] = 'c';
  M['g'] = 'v';
  M['h'] = 'x';
  M['i'] = 'd';
  M['j'] = 'u';
  M['k'] = 'i';
  M['l'] = 'g';
  M['m'] = 'l';
  M['n'] = 'b';
  M['o'] = 'k';
  M['p'] = 'r';
  M['q'] = 'z';
  M['r'] = 't';
  M['s'] = 'n';
  M['t'] = 'w';
  M['u'] = 'j';
  M['v'] = 'p';
  M['w'] = 'f';
  M['x'] = 'm';
  M['y'] = 'a';
  M['z'] = 'q';
  int n;
  cin >> n;
  getline(cin, s1);
  for(int i = 0; i < n; i++){
    getline(cin, s1);
    s2 = "";
    for(int j = 0; j < (int)s1.size(); j++){
      s2 += M[s1[j]];
    }
    cout << "Case #" << i+1 << ": " << s2 << endl;
  }
  return 0;
}
