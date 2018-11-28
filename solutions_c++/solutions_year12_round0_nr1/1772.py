#include <iostream>
#include <string>

using namespace std;

char trans[] = "yhesocvxduiglbkrztnwjpfmaq";


string translate(string s)
{
  string ans;
  for (int i = 0; i < s.size(); ++i)
    if (s[i] >= 'a' && s[i] <= 'z')
      ans.push_back(trans[s[i] - 'a']);
    else
      ans.push_back(s[i]);
  return ans;
}

int main()
{
  int T;
  char line[256];
  cin >> T;
  cin.getline(line, 256);
  for (int i = 1; i <= T; ++i) {
    cin.getline(line, 256);
    cout << "Case #" << i << ": " << translate(line) << endl;
  }
  return 0;
}
