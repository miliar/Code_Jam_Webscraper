#include <iostream>
#include <string>

using namespace std;

char convert(char in)
{
  switch(in)
    {
    case 'a':
      return 'y';
    case 'b':
      return 'h';
    case 'c':
      return 'e';
    case 'd':
      return 's';
    case 'e':
      return 'o';
    case 'f':
      return 'c';
    case 'g':
      return 'v';
    case 'h':
      return 'x';
    case 'i':
      return 'd';
    case 'j':
      return 'u';
    case 'k':
      return 'i';
    case 'l':
      return 'g';
    case 'm':
      return 'l';
    case 'n':
      return 'b';
    case 'o':
      return 'k';
    case 'p':
      return 'r';
    case 'q':
      return 'z'; //LKAFJKSDFJSDJGLSDJGKJ
    case 'r':
      return 't';
    case 's':
      return 'n';
    case 't':
      return 'w';
    case 'u':
      return 'j';
    case 'v':
      return 'p';
    case 'w':
      return 'f';
    case 'x':
      return 'm';
    case 'y':
      return 'a';
    case 'z':
      return 'q'; //;DFJALKSFJASFJ;ASDFJAS;DFJ
    }
}

int main()
{
  int t;
  char c;
  cin >> t;
  cin >> noskipws >> c;
  for (int i = 0; i < t; i++)
    {
      cout << "Case #" << i+1 << ": ";
      cin >> noskipws >> c;
      while (c != '\n')
	{
	  if (c == ' ')
	    {
	      cout << ' ';
	    }
	  else
	    {
	      cout << convert(c);
	    }
	  cin >> noskipws >> c;
	}
      cout << endl;
    }
}
