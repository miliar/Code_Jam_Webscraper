#include <iostream>
#include <fstream>
#include <map>
using namespace std;

int main()
{
  ifstream fin("A-small-attempt2.in");
  ofstream fout("output.txt");

  map<char, char> mapping;

  mapping['y'] = 'a';
  mapping['e'] = 'o';
  mapping['q'] = 'z';
  mapping['z'] = 'q';

  // get the mapping
  string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
  string s2 = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

  for (string::size_type index = 0; index != s1.size(); ++index) {
    if (s1.at(index) == ' ' || mapping.count(s1.at(index)) > 0)
      continue;
    else {
      mapping[s1.at(index)] = s2.at(index);
    }
  }

  //for (map<char, char>::iterator iter = mapping.begin(); iter != mapping.end(); ++iter)
    //cout << iter->first << " " << iter->second << endl;

  int test_cases;
  fin >> test_cases;
  string line;
  getline(fin, line);

  for (int round = 1; round <= test_cases; ++round) {
    getline(fin, line);
    for (string::size_type ix = 0; ix != line.size(); ++ix) {
      if (line.at(ix) != ' ' && mapping.count(line.at(ix)) > 0)
        line.at(ix) = mapping[line.at(ix)];
    }

    fout << "Case #" << round << ": " << line << endl;
  }
  return 0;
}

