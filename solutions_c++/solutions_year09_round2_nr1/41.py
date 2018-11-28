#include <iostream>
#include <sstream>
#include <set>
#include <iomanip>
using namespace std;

struct node {
  double p;
  string f;
  node *left;
  node *right;

  node(double _p, string _f) : p(_p), f(_f) {
    left = right = NULL;
  }
};

node *parse(string& s, int low, int hi) {
  // cout << "\tparsing " << s.substr(low, hi - low) << endl;

  low++; hi--;
  bool has_sub = false;
  for (int i = low; i < hi; i++)
    if (s[i] == '(') {
      has_sub = true;
      break;
    }

  stringstream ss; ss << s.substr(low, hi - low);
  if (!has_sub) {
    double p; ss >> p;
    return new node(p, "");
  }
  else {
    double p; string f;
    ss >> p >> f;
    node *cur = new node(p, f);
    int last = -1, balance = 0;
    for (int i = low; i < hi; i++) {
      if (s[i] == '(') {
        balance++;
        if (last == -1) last = i;
      }
      else if (s[i] == ')') {
        balance--;
        if (balance == 0) {
          if (cur->left == NULL)
            cur->left = parse(s, last, i+1);
          else
            cur->right = parse(s, last, i+1);
          last = -1;
        }
      }
    }
    return cur;
  }
}

double get(node *cur, set<string>& fs) {
  if (cur->f.size() == 0) return cur->p;
  else if (fs.find(cur->f) != fs.end())
    return cur->p * get(cur->left, fs);
  return cur->p * get(cur->right, fs);
}

void release(node *cur) {
  if (cur->left) release(cur->left);
  if (cur->right) release(cur->right);
  delete cur;
}

void printtree(node *cur) {
  cout << "\t" << cur->p << " " << cur->f << endl;
  if (cur->left) printtree(cur->left);
  if (cur->right) printtree(cur->right);
}

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    string all;
    int L; cin >> L;
    string temp; getline(cin, temp);
    for (int i = 0; i < L; i++) {
      getline(cin, temp);
      all += temp;
    }
    node *root = parse(all, 0, all.size());
    // printtree(root);

    int N; cin >> N;
    getline(cin, temp);
    cout << "Case #" << c << ":" << endl;
    for (int i = 0; i < N; i++) {
      getline(cin, temp);
      stringstream ss; ss << temp;
      ss >> temp;
      int n; ss >> n;
      set<string> fs;
      for (int i = 0; i < n; i++) {
        ss >> temp;
        fs.insert(temp);
      }
      cout.setf(ios::fixed);
      cout << setprecision(7) << get(root, fs) << endl;
    }
    release(root);
  }
  return 0;
}
