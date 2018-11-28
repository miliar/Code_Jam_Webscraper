#include <iostream>
#include <string>

using namespace std;

const int N_SAMPLE = 3;

string sampin[N_SAMPLE] = {
  "ejp mysljylc kd kxveddknmc re jsicpdrysi",
  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
  "de kr kd eoya kw aej tysr re ujdr lkgc jv",
};
string sampout[N_SAMPLE] = {
  "our language is impossible to understand",
  "there are twenty six factorial possibilities",
  "so it is okay if you want to just give up",
};

int main(void){
  char map[26];
  fill_n(map, 26, '\0');
  for(int i = 0; i < N_SAMPLE; ++i)
    for(int j = 0; j < sampin[i].size(); ++j)
      if(sampin[i][j] != ' ')
        map[sampin[i][j]-'a'] = sampout[i][j];
  map['q'-'a'] = 'z';
  map['z'-'a'] = 'q';

  int t;
  string line;
  cin >> t;
  getline(cin, line);
  for(int k = 0; k < t; ++k){
    getline(cin, line);
    cout << "Case #" << k+1 << ": ";
    for(int i = 0; i < line.size(); ++i)
      if(line[i] == ' ')
        cout << ' ';
      else if(map[line[i]-'a'] == '\0')
        cout << "#";
      else
        cout << map[line[i]-'a'];
    cout << endl;
  }
  return 0;
}
