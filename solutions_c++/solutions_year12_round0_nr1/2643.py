#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cassert>


using namespace std;


int main()
{
    map<char, char> m;
    vector<string> train_input;
    vector<string> train_output;
    train_input.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
    train_output.push_back("our language is impossible to understand");

    train_input.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
    train_output.push_back("there are twenty six factorial possibilities");

    train_input.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");
    train_output.push_back("so it is okay if you want to just give up");

    for (int i = 0; i < 3; ++i) {
        assert(train_input[i].size() == train_output[i].size());
        for (int j = 0; j < train_input[i].size(); ++j) {
            if (train_input[i][j] != ' ') {
                m[train_input[i][j]] = train_output[i][j];
            }
        }
    }

    m['q'] = 'z';
    m['z'] = 'q';

    int T;
    cin >> T;

    string line;
    getline(cin, line);

    for (int t = 0; t < T; ++t) {
      getline(cin, line);
      for (int i = 0; i < line.size(); ++i) {
          if (line[i] != ' ') {
              line[i] = m[line[i]];
          }
      }
      cout << "Case #" <<  t + 1 << ": " << line << endl;
    }

    return 0;
}
