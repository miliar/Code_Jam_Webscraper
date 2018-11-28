/* Google Code Jam 2009: Round 1B: Problem A: "Decision Tree". */
// Sat. Sept. 12, 2009, By: Samuel Tien-Chieh Huang.
// Last update: Sat. Sept. 12, 2009.
#include <cstdio>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
using namespace std;


class t_tree {
public:
  double w;
  string q;
  t_tree *yes, *no;
  t_tree (double w, string q, t_tree *yes, t_tree *no):
      w (w), q (q), yes (yes), no (no) {
  }
  double get_cute (set <string> &attr) {
    if (yes == NULL) return w;
    return w * (attr.count (q) ? yes : no)->get_cute (attr);
  }
  ~t_tree () {
    delete yes;
    delete no;
  }
};

double get_num (string &s, int &pos) {
  while (s [pos] == ' ') pos ++;
  string t = "";
  for (;; pos ++) {
    char ch = s [pos];
    if ((ch != '.') && ((ch < '0') || (ch > '9'))) break;
    t += ch;
  }
  double ret;
  sscanf (t.c_str (), "%lf", &ret);
  return ret;
}

string get_string (string &s, int &pos) {
  while (s [pos] == ' ') pos ++;
  string ret;
  for (;; pos ++) {
    char ch = s [pos];
    if ((ch == ' ') || (ch == ')') || (ch == '(')) break;
    ret += ch;
  }
  return ret;
}

t_tree *parse (string &s, int &pos) {
  while (s [pos] == ' ') pos ++;
  if (s [pos ++] != '(') throw "Bad form";
  double w = get_num (s, pos);
  while (s [pos] == ' ') pos ++;
  t_tree *ret = NULL;
  if (s [pos] != ')') {
    string q = get_string (s, pos);
    t_tree *yes = parse (s, pos);
    t_tree *no = parse (s, pos);
    ret = new t_tree (w, q, yes, no);
  } else {
    ret = new t_tree (w, "", NULL, NULL);
  }
  while (s [pos] == ' ') pos ++;
  if (s [pos ++] != ')') throw "Bad form";
  return ret;
}

int main (void) {
  string line;
  int nc;
  getline (cin, line);
  sscanf (line.c_str (), "%d", &nc);
  try {
    for (int ca = 1; ca <= nc; ca ++) {
      printf ("Case #%d:\n", ca);
      int l, a;
      getline (cin, line);
      sscanf (line.c_str (), "%d", &l);
      string s;
      for (int i = 0; i < l; i ++) {
        getline (cin, line);
        s += line;
      }
      int pos = 0;
      t_tree *dec = parse (s, pos);
      getline (cin, line);
      sscanf (line.c_str (), "%d", &a);
      for (int i = 0; i < a; i ++) {
        getline (cin, line);
        istringstream iss (line);
        string name, q;
        int nat;
        set <string> attr;
        iss >> name >> nat;
        for (int j = 0; j < nat; j ++) {
          iss >> q;
          attr.insert (q);
        }
        printf ("%.7f\n", dec->get_cute (attr));
      }
      delete dec;
    }
  } catch (string e) {
    cerr << e << endl;
  }
  return 0;
}
