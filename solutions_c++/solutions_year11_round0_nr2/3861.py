#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>

using namespace std;

class Magicka {
 public:
  map<string, char> combos_;
  set<string> opposes_;

  void addCombo(string c) {
    string rev = "  ";
    rev[0] = c[1]; rev[1] = c[0];
    combos_[c.substr(0,2)] = c[2];
    combos_[rev] = c[2];
  }

  void addOppose(string o) {
    string rev = "  ";
    rev[0] = o[1]; rev[1] = o[0];
    opposes_.insert(o);
    opposes_.insert(rev);
  }

  string process(string input) {
    vector<char> stack;

    for (int i = 0; i < input.length(); ++i) {
      //cerr << "Char " << i + 1 << endl;
      string combo_cand = "  ";
      stack.push_back(input[i]);
      while (stack.size() >= 2) {
        combo_cand[0] = stack[stack.size() - 1];
        combo_cand[1] = stack[stack.size() - 2];
        //cerr << "testing combo " << combo_cand << endl;
        if (combos_.count(combo_cand)) {
          stack.pop_back();
          stack.pop_back();
          stack.push_back(combos_[combo_cand]);
        } else break;
      } // end searching for combos

      string opp_cand = "  ";
      opp_cand[0] = stack[stack.size() - 1];
      for (int j = 0; j < stack.size() - 1; ++j) {
        opp_cand[1] = stack[j];
        if (opposes_.count(opp_cand)) {
          stack.erase(stack.begin(), stack.end());
          break;
        }
      } // end searching for oppose

    } // end input

    string op = "[";
    for (int i = 0; i < stack.size(); ++i) {
      string ch = " ";
      ch[0] = stack[i];
      op += ch;
      if (i != stack.size() - 1) 
        op += ", ";
    }
    op += "]";
    return op;
  }
};

int main() {
  int n_cases;
  cin >> n_cases;
  for (int i = 0; i < n_cases; ++i) {
    Magicka m;
    int n_combos;
    cin >> n_combos;
    string combo;
    for (int j = 0; j < n_combos; ++j) {
      cin >> combo;
      m.addCombo(combo);
      //cerr << "Adding combo " << combo << endl;
    }
    int n_oppose;
    string oppose;
    cin >> n_oppose;
    for (int j = 0; j < n_oppose; ++j) {
      cin >> oppose;
      m.addOppose(oppose);
      //cerr << "Adding oppose " << oppose << endl;
    }
    int tmp;
    cin >> tmp;
    string invoke;
    cin >> invoke;
    //cerr << "Processing " << invoke << endl;
    cout << "Case #" << i + 1 << ": " << m.process(invoke) << "\n";
  }
  return 0;
}
