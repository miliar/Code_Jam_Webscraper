#include <iostream>
#include <fstream>
using namespace std;

char translate(char c)
{
  switch(c)
  {
case 'y':		return 'a';		break;case 'n':		return 'b';		break;case 'f':		return 'c';		break;case 'i':		return 'd';		break;case 'c':		return 'e';		break;case 'w':		return 'f';		break;case 'l':		return 'g';		break;case 'b':		return 'h';		break;case 'k':		return 'i';		break;case 'u':		return 'j';		break;case 'o':		return 'k';		break;case 'm':		return 'l';		break;case 'x':		return 'm';		break;case 's':		return 'n';		break;case 'e':		return 'o';		break;case 'v':		return 'p';		break;case 'z':		return 'q';		break;case 'p':		return 'r';		break;case 'd':		return 's';		break;case 'r':		return 't';		break;case 'j':		return 'u';		break;case 'g':		return 'v';		break;case 't':		return 'w';		break;case 'h':		return 'x';		break;case 'a':		return 'y';		break;case 'q':		return 'z';		break;
case ' ':
  return ' ';
  break;


}
}

int main()
{
  ifstream infile;
  
  infile.open("A-small-attempt2.in");

  string dummy;
  
  int n;
  infile >> n;
  getline(infile, dummy);
  for (int i=1; i <= n; i++)
  {
    cout << "Case #" << i << ": ";
    string str;
    getline(infile, str);
    for (int j =0; j < str.length(); j++)
    {
      cout << translate(str[j]);
    }

    cout << endl;
  }
  return 0;
}