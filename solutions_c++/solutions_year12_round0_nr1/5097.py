#include <fstream>
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
  ifstream inFile(argv[1]);
  map<char, char> ref;

  ref[' '] = ' ';
  ref['a'] = 'y';
  ref['b'] = 'h';
  ref['c'] = 'e';
  ref['d'] = 's';
  ref['e'] = 'o';
  ref['f'] = 'c';
  ref['g'] = 'v';
  ref['h'] = 'x';
  ref['i'] = 'd';
  ref['j'] = 'u';
  ref['k'] = 'i';
  ref['l'] = 'g';
  ref['m'] = 'l';
  ref['n'] = 'b';
  ref['o'] = 'k';
  ref['p'] = 'r';
  ref['q'] = 'z'; //
  ref['r'] = 't';
  ref['s'] = 'n';
  ref['t'] = 'w';
  ref['u'] = 'j';
  ref['v'] = 'p';
  ref['w'] = 'f';
  ref['x'] = 'm';
  ref['y'] = 'a';
  ref['z'] = 'q'; //
  if (inFile.good())
  {
    int nCases;
    string strA;
    inFile >> nCases;
    getline(inFile, strA);
    for (int i = 0; i < nCases; i++)
    {
      string strB;
      getline(inFile, strA);
      for (int j = 0; j < strA.size(); j++)
      {
        strB += ref[strA[j]];
      }
      cout << "Case #" << (i + 1) << ": " << strB << endl;
    }
  }
  inFile.close();

  return 0;
}
