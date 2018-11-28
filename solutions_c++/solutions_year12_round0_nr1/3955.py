#include <iostream>
#include <string>

using namespace std;

char map[26];



char mapper(char c)
{
  if ((c >= 'a') and (c <= 'z')) c = map[c-'a'];
  return c;
}

int main()
{
  map[0] = 'y';
map[1] = 'h';
map[2] = 'e';
map[3] = 's';
map[4] = 'o';
map[5] = 'c';
map[6] = 'v';
map[7] = 'x';
map[8] = 'd';
map[9] = 'u';
map[10] = 'i';
map[11] = 'g';
map[12] = 'l';
map[13] = 'b';
map[14] = 'k';
map[15] = 'r';
map[16] = 'z';
map[17] = 't';
map[18] = 'n';
map[19] = 'w';
map[20] = 'j';
map[21] = 'p';
map[22] = 'f';
map[23] = 'm';
map[24] = 'a';
map[25] = 'q';
  int t;
  cin >> t;
  for (int i =1 ; i <= t; i++)
  {
    string s;
    getline(cin >> ws, s);
    for (int j = 0; j < s.size(); j++)
      s[j] = mapper(s[j]);
    cout << "Case #" << i << ": " << s << endl;
  }
}