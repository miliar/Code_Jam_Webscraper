# include <iostream>
# include <sstream>
# include <fstream>
# include <stack>
# include <vector>
# include <string>
# include <limits>
# include <cstring>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

ofstream fout("output.txt");
ifstream fin ("input.txt");
#define CODEJAM 1
#ifdef CODEJAM
#define cout fout
#define cin  fin
#endif


int main()
{
  string strarr[10] = {"z", "q", "y qee", "a zoo", "ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand",
  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities", "de kr kd eoya kw aej tysr re ujdr lkgc jv",
  "so it is okay if you want to just give up"};
  
  map<char, char> Map;
  
  for (int i = 0; i < 10; i+=2)
    for (int j = 0; j < strarr[i].length(); j++)
      Map[strarr[i][j]] = strarr[i+1][j];

  //cout << Map.size() << endl;
  //string ss;
  //for (int i = 97; i < 97 + 26; i++)
  //{
  //  ss += Map[i];
    //cout << (char)i << "--" << (char)Map[i] << endl;
  //}

  //sort (ss.begin(), ss.end());
  //cout << ss;
  
  int Total = 0;
  cin >> Total;
  cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
  for (int i = 0; i < Total; i++)
  {
    string input, output = "";
    getline (cin, input);
    int len = input.length();
    for (int j = 0; j < len; j++)
    {
      output += Map[input[j]];
    }
    cout << "Case #" << i+1 << ": " << output << endl;
  }

  cin.ignore();
  cin.get();
  return 0;
}
