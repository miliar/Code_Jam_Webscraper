#include <cassert>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>

#define UINT unsigned long long

#define MAX 50000000
int buffer[9][MAX];

using namespace std;

int main(int argc, char* argv[])
{
  ifstream input(argv[1]);

  UINT C;
  input >> C;

  for(UINT c = 0; c < C; c++)
  {
    string x; input >> x;

    std::vector<UINT> str;

    for (UINT i = 0; i < x.size(); i++)
    {
      str.push_back(x[i] - '0');
    }


    bool b = next_permutation (str.begin(),
			       str.end());
    if (b)
    {
      std::cout << "Case #" << (c+1) << ": ";
      for(UINT i = 0; i < str.size(); i++)
              std::cout << str[i];
      cout << endl;
    }
    else
    {
      str.insert(str.begin(), 0);
      UINT k = 0;
      while (str[k] == 0) k++;
      std::swap(str[k], str[0]);

      std::cout << "Case #" << (c+1) << ": ";
      for(UINT i = 0; i < str.size(); i++)
              std::cout << str[i];
      cout << endl;
    }
  }
}
