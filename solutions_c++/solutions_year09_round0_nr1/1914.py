
#include <iostream>
#include <set>
#include <string>

using namespace std;

int L, D, N;

class Pat {
public:
  string* tok;
  Pat(string p) {
    tok = new string[L];
    bool inside = false;
    int tnum = 0;
    for (int i=0; i<p.size(); i++) {
      if (p[i] == '(') inside = true;
      else if (p[i] == ')') inside = false, tnum ++;
      else {
        tok[tnum] += p[i];
        if (!inside) tnum +=1;
      }
    }
  }
  bool match_char(int num, char c) {
    return tok[num].find(c) != string::npos;
  }
  int match_count(const set<string>& dict) {
    int match = 0;
    string last = "";
    for (set<string>::const_iterator i = dict.begin();
        i != dict.end();
        i++) 
    {
      string d = *i;
      int p = 0;
      // skip same chars
      while (p < L && d[p] == last[p]) p++;
      // match remaining chars
      while (p < L && match_char(p,d[p])) p++;
      
      match += (p>=L);
    }
    return match;
  }
};

int main()
{
  cin >> L >> D >> N;
  set<string> dict;
  for (int i = 0; i < D; i ++) {
    string d;
    cin >> d;
    dict.insert(d);
  }
  for (int i= 0; i < N; i ++) {
    string p_str;
    cin >> p_str;
    Pat p(p_str);
    cout << "Case #"<<i+1<<": "<< p.match_count(dict)
      << endl;
  }
}
