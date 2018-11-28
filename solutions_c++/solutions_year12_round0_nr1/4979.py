#include <iostream>
#include <string>

using namespace std;

int translate(std::string& phrase, int nb)
{
  cout << "Case #"<< nb << ": ";
  for(int i = 0; i < phrase.size(); i++)
    {
      switch(phrase[i])
	{
	case 'y':
	  cout << 'a';
	  break;
	case 'n':
	  cout << 'b';
	  break;
	case 'f':
	  cout << 'c';
	  break;
	case 'i':
	  cout << 'd';
	  break;
	case 'c':
	  cout << 'e';
	  break;
	case 'w':
	  cout << 'f';
	  break;
	case 'l':
	  cout << 'g';
	  break;
	case 'b':
	  cout << 'h';
	  break;
	case 'k':
	  cout << 'i';
	  break;
	case 'u':
	  cout << 'j';
	  break;
	case 'o':
	  cout << 'k';
	  break;
	case 'm':
	  cout << 'l';
	  break;
	case 'x':
	  cout << 'm';
	  break;
	case 's':
	  cout << 'n';
	  break;
	case 'e':
	  cout << 'o';
	  break;
	case 'v':
	  cout << 'p';
	  break;
	case 'z':
	  cout << 'q';
	  break;
	case 'p':
	  cout << 'r';
	  break;
	case 'd':
	  cout << 's';
	  break;
	case 'r':
	  cout << 't';
	  break;
	case 'j':
	  cout << 'u';
	  break;
	case 'g':
	  cout << 'v';
	  break;
	case 't':
	  cout << 'w';
	  break;
	case 'h':
	  cout << 'x';
	  break;
	case 'a':
	  cout << 'y';
	  break;
	case 'q':
	  cout << 'z';
	  break;
	case ' ':
	  cout << ' ';
	  break;
	}
    }

  cout << endl;
}

int main()
{
  int n;
  std::string menu;

  std::cin >> n;
  std::cin.ignore();

  for(int i = 0; i < n; i++)
    {
      std::getline(std::cin, menu);
      translate(menu, i+1);
    }

  return 0;

}
