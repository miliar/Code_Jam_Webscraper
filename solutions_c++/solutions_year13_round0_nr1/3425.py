#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

char judge(char s[4])
{
  char c = s[0];
  if (c == 'T')
    c = s[1];
  
  for (int i = 0; i < 4; ++i)
    if (s[i] != 'T' && s[i] != c)
      return '\0';

  return c;
}

int main(int argc, char *argv[])
{
  ifstream fin("A-large.in.txt");
  int cases;
  int cnt = 0;

  fin >> cases;
  while (++cnt <= cases) {
    bool dot = false;
    bool xw = false;
    bool ow = false;

    char p[4] = { 0, 0, 0, 0 };
    string str;
    stringstream ss;

    for (int i = 0; i < 4; ++i) {
      fin >> str;
      ss << str;
    }
    str = ss.str();
    dot = (str.find('.') != string::npos);

    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
	p[j] = str[i * 4 + j];
      }
      char r = judge(p);
      if (r == 'X') xw = true;
      else if (r == 'O') ow = true;
    }
    if (dot) {
      if (xw) {
	cout << "Case #" << cnt << ": X won" << endl;
	continue;
      } else if (ow) {
	cout << "Case #" << cnt << ": O won" << endl;
	continue;
      }
    }

    for (int i = 0; i < 4; ++i) {
      for (int j = 0; j < 4; ++j) {
	p[j] = str[j * 4 + i];
      }
      char r = judge(p);
      if (r == 'X') xw = true;
      else if (r == 'O') ow = true;
    }
    if (dot) {
      if (xw) {
	cout << "Case #" << cnt << ": X won" << endl;
	continue;
      } else if (ow) {
	cout << "Case #" << cnt << ": O won" << endl;
	continue;
      }
    }

    p[0] = str[0]; p[1] = str[5]; p[2] = str[10]; p[3] = str[15];
    char r = judge(p);
    if (r == 'X') xw = true;
    else if (r == 'O') ow = true;
    if (dot) {
      if (xw) {
	cout << "Case #" << cnt << ": X won" << endl;
	continue;
      } else if (ow) {
	cout << "Case #" << cnt << ": O won" << endl;
	continue;
      }
    }

    p[0] = str[3]; p[1] = str[6]; p[2] = str[9]; p[3] = str[12];
    r = judge(p);
    if (r == 'X') xw = true;
    else if (r == 'O') ow = true;
    if (dot) {
      if (xw) {
	cout << "Case #" << cnt << ": X won" << endl;
	continue;
      } else if (ow) {
	cout << "Case #" << cnt << ": O won" << endl;
	continue;
      } else {
	cout << "Case #" << cnt << ": Game has not completed" << endl;
	continue;
      }
    }

    if (! dot) {
      if (xw) {
	cout << "Case #" << cnt << ": X won" << endl;
	continue;
      } else if (ow) {
	cout << "Case #" << cnt << ": O won" << endl;
	continue;
      } else {
	cout << "Case #" << cnt << ": Draw" << endl;
	continue;
      }
    }
    // cout << "Case #" << cnt << ": " << str << endl;
  }
  fin.close();
  return 0;
}
