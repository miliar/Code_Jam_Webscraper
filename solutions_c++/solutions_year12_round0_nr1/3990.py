#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <fstream>

using namespace std;

#define FOR(i,n) for(int(i)=0;(i)<(int)(n);(i)++)
#define FOREACH(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

int main(void)
{
  string line;
  ifstream infile("input.txt");
  int cases;
  
  if(!infile.is_open())
  {
    return 0;
  }

  infile >> cases;
  // Get garbage
  getline(infile, line);
  
  FOR(currCase, cases)
  {
    getline(infile, line);
    cout << "Case #" << currCase + 1 << ": ";
    //FOREACH(line, currChar)
    for(string::iterator currChar = line.begin(); currChar != line.end(); ++currChar)
    {
      if(*currChar < 'a' || *currChar > 'z')
      {
        continue;
      }
      switch(*currChar)
      {
        case 'a':
          *currChar = 'y';
        break;
        case 'b':
          *currChar = 'h';
        break;
        case 'c':
          *currChar = 'e';
        break;
        case 'd':
          *currChar = 's';
        break;
        case 'e':
          *currChar = 'o';
        break;
        case 'f':
          *currChar = 'c';
        break;
        case 'g':
          *currChar = 'v';
        break;
        case 'h':
          *currChar = 'x';
        break;
        case 'i':
          *currChar = 'd';
        break;
        case 'j':
          *currChar = 'u';
        break;
        case 'k':
          *currChar = 'i';
        break;
        case 'l':
          *currChar = 'g';
        break;
        case 'm':
          *currChar = 'l';
        break;
        case 'n':
          *currChar = 'b';
        break;
        case 'o':
          *currChar = 'k';
        break;
        case 'p':
          *currChar = 'r';
        break;
        case 'q':
          *currChar = 'z';
        break;
        case 'r':
          *currChar = 't';
        break;
        case 's':
          *currChar = 'n';
        break;
        case 't':
          *currChar = 'w';
        break;
        case 'u':
          *currChar = 'j';
        break;
        case 'v':
          *currChar = 'p';
        break;
        case 'w':
          *currChar = 'f';
        break;
        case 'x':
          *currChar = 'm';
        break;
        case 'y':
          *currChar = 'a';
        break;
        case 'z':
          *currChar = 'q';
        break;
        default:
        break;
      }
    }
    cout << line << endl;
  }
  
  return 0;
}