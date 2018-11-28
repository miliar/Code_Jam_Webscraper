#include <iostream>

using namespace std;

char translate(char c)
{
  switch(c)
    {
    case 'a': return 'y';
    case 'b': return 'h';
    case 'c': return 'e';
    case 'd': return 's';
    case 'e': return 'o';
    case 'f': return 'c';
    case 'g': return 'v';
    case 'h': return 'x';
    case 'i': return 'd';
    case 'j': return 'u';
    case 'k': return 'i';
    case 'l': return 'g';
    case 'm': return 'l';
    case 'n': return 'b';
    case 'o': return 'k';
    case 'p': return 'r';
    case 'q': return 'z';
    case 'r': return 't';
    case 's': return 'n';
    case 't': return 'w';
    case 'u': return 'j';
    case 'v': return 'p';
    case 'w': return 'f';
    case 'x': return 'm';
    case 'y': return 'a';
    case 'z': return 'q';
    case ' ': return ' ';
    case '\n': return '\n';
    }
}

int main()
{
  ios_base::sync_with_stdio(0);
  int t;
  cin >> t;
  string x;
  getline(cin,x);
  for(int j = 1; j <= t; j++)
    {
      string tmp;
      getline(cin,tmp);
      cout << "Case #" << j << ": ";
      for(int i = 0; i < tmp.length(); i++)
	cout << translate(tmp[i]);
      cout << endl;
    }
  return 0;
}

  
