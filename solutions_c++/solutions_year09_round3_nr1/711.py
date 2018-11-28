#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>
using namespace std;


typedef unsigned long long ullong;
typedef string::size_type ssize;

int get_char_kind(const string &str)
{
  bool flags[256] = {};

  for (int i = 0; i < (int)str.length(); i++)
  {
    flags[str[i]] = true;
  }


  int result = 0;
  for (int i = 0; i < 256; i++)
    if (flags[i])
      result++;

  if (result < 2)
    result = 2;
  return result;
}

ullong get_seconds(const string& str)
{
  ullong result = 0;

  const int length = (int)str.length();
  const int kind = get_char_kind(str);


  int num[256] = {};
  std::fill(num, num+256, -1);

  num[str[0]] = 1;

  ssize pos = str.find_first_not_of(str[0]);
  if (pos != str.npos)
    num[str[pos]] = 0;

  int c = 2;
  for (int i = 0; i < length; i++)
  {
    if (num[str[i]] == -1)
      num[str[i]] = c++;
  }

  ullong b = 1;
  for (int i = length - 1; i >= 0; i--)
  {
    result += b * num[str[i]];
    b *= kind;
  }

  return result;
}




int main(int argc, char *argv[])
{
  if (argc < 3)
    return 1;

  ifstream fin(argv[1]);
  ofstream fout(argv[2]);

  if (fin.fail() || fout.fail())
    return 1;


  string buf;

  int T;
  fin >> T;
  getline(fin, buf);

  for (int test = 0; test < T; test++)
  {
    getline(fin, buf);
    unsigned long long seconds = get_seconds(buf);

    if (test >0) fout << "\n";
    fout << "Case #" << test+1 << ": " << seconds;
  }

  fout << flush;

  return 0;
}
