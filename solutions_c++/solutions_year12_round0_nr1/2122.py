 
#include <iostream>
 
using namespace std;

const char mapping[] = 
{
 /*'a' =>*/ 'y',
 /*'b' =>*/ 'h',
 /*'c' =>*/ 'e',
 /*'d' =>*/ 's',
 /*'e' =>*/ 'o',
 /*'f' =>*/ 'c',
 /*'g' =>*/ 'v',
 /*'h' =>*/ 'x',
 /*'i' =>*/ 'd',
 /*'j' =>*/ 'u',
 /*'k' =>*/ 'i',
 /*'l' =>*/ 'g',
 /*'m' =>*/ 'l',
 /*'n' =>*/ 'b',
 /*'o' =>*/ 'k',
 /*'p' =>*/ 'r',
 /*'q' =>*/ 'z',
 /*'r' =>*/ 't',
 /*'s' =>*/ 'n',
 /*'t' =>*/ 'w',
 /*'u' =>*/ 'j',
 /*'v' =>*/ 'p',
 /*'w' =>*/ 'f',
 /*'x' =>*/ 'm',
 /*'y' =>*/ 'a',
 /*'z' =>*/ 'q'
};

int main(int argc, char ** argv)
{
  int num;
  cin >> num;
  string temp;
  getline(cin, temp);
  for(int i = 0; i < num; i++)
  {
    string line;
    cout << "Case #" << i+1 << ": ";
    getline(cin, line);
    for(int j = 0; j < line.size(); j++)
    {
      char c = line[j];
      if(c == ' ')
        cout << " ";
      else if(c >= 'a' && c <= 'z')
      {
        string str = " ";
        str[0] = mapping[c-'a'];
        cout << str;
      }

    }
    cout << endl;
  }
  return 0;
}

