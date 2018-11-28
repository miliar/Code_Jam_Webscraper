#include <iostream>
#include <string> 
#include <map>
using namespace std;

string input;

string solve();

string solve()
{
   string res;
   map<char, char> translate;

   translate.insert(pair<char, char>('a', 'y'));
   translate.insert(pair<char, char>('b', 'h'));
   translate.insert(pair<char, char>('c', 'e'));
   translate.insert(pair<char, char>('d', 's'));
   translate.insert(pair<char, char>('e', 'o'));
   translate.insert(pair<char, char>('f', 'c'));
   translate.insert(pair<char, char>('g', 'v'));
   translate.insert(pair<char, char>('h', 'x'));
   translate.insert(pair<char, char>('i', 'd'));
   translate.insert(pair<char, char>('j', 'u'));
   translate.insert(pair<char, char>('k', 'i'));
   translate.insert(pair<char, char>('l', 'g'));
   translate.insert(pair<char, char>('m', 'l'));
   translate.insert(pair<char, char>('n', 'b'));
   translate.insert(pair<char, char>('o', 'k'));
   translate.insert(pair<char, char>('p', 'r'));
   translate.insert(pair<char, char>('q', 'z'));
   translate.insert(pair<char, char>('r', 't'));
   translate.insert(pair<char, char>('s', 'n'));
   translate.insert(pair<char, char>('t', 'w'));
   translate.insert(pair<char, char>('u', 'j'));
   translate.insert(pair<char, char>('v', 'p'));
   translate.insert(pair<char, char>('w', 'f'));
   translate.insert(pair<char, char>('x', 'm'));
   translate.insert(pair<char, char>('y', 'a'));
   translate.insert(pair<char, char>('z', 'q'));
   translate.insert(pair<char, char>(' ', ' '));

   for (int i = 0; i < input.size(); i++)
   {
      char c = input[i];
      res.push_back(translate[c]);
   }

   return res;
}

int main(int argc, const char *argv[])
{
   int T;
   cin >> T;
   cin.get();

   for (int i = 1; i <= T; i++) 
   {
      getline(cin, input);
      input = solve();
      cout << "Case #" << i << ": " << input;
      cout << endl;
   }

   return 0;
}
