#include <iostream>
#include <map>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
  map<char, char> trans_m;
  trans_m['a'] = 'y'; trans_m['b'] = 'h'; trans_m['c'] = 'e'; trans_m['d'] = 's';
  trans_m['e'] = 'o'; trans_m['f'] = 'c'; trans_m['g'] = 'v'; trans_m['h'] = 'x';
  trans_m['i'] = 'd'; trans_m['j'] = 'u'; trans_m['k'] = 'i'; trans_m['l'] = 'g';
  trans_m['m'] = 'l'; trans_m['n'] = 'b'; trans_m['o'] = 'k'; trans_m['p'] = 'r';
  trans_m['q'] = 'z'; trans_m['r'] = 't'; trans_m['s'] = 'n'; trans_m['t'] = 'w';
  trans_m['u'] = 'j'; trans_m['v'] = 'p'; trans_m['w'] = 'f'; trans_m['x'] = 'm';
  trans_m['y'] = 'a'; trans_m['z'] = 'q';

  int t;
  cin >> t;
  cin.get(); // To capture newline before getline()

  vector<string> cases;
  for (int i = 0; i < t; ++i){
    string input;
    getline(cin, input);
    cases.push_back(input);
  }

  for (int i = 0; i < t; ++i)
  {
    for(int j = 0; j < cases[i].length(); ++j){
      if(cases[i][j] != ' ')
        cases[i][j] = trans_m[cases[i][j]];
    }
    cout << "Case #"<< i+1 <<": " << cases[i] << endl;
  }
  return 0;
}


