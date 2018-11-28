#include <algorithm>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <set>
#include <vector>

using namespace std;

namespace {

  struct Node {
    double weight;
    std::string name;
    Node *yes;
    Node *no;
  };
  
  template<typename T>
  T convert(const std::string& s) {
    std::istringstream iss(s);
    T out;
    iss >> out;
    return out;
  }
  
  const char digits[] = "1234567890.";
  const char ws[] = " \n\t";
  const char alpha[] = "qwertyuiopasdfghjklzxcvbnm";
  
  int parse(const std::string& tree, Node& root, int start) {
    root.yes = NULL;
    root.no = NULL;
    int a = tree.find_first_of(digits, start);
    int b = tree.find_first_not_of(digits, a);
    root.weight = convert<double>(tree.substr(a, b-a));
    //std::cerr << "Weight is " << root.weight << endl;
    int c = tree.find_first_not_of(ws, b);
    if (tree[c] == ')') return c+1;
    // need to parse subtree
    int d = tree.find_first_of(ws, c);
    root.name = tree.substr(c, d-c);
    //std::cerr << "Name is " << root.name << endl;
    root.yes = new Node;
    root.no = new Node();
    int start2 = parse(tree, *root.yes, d+1);
    parse(tree, *root.no, start2);
  }
}

int main(int argc, char *argv[]) {
  int ntrials = 0;
  cin >> ntrials;
  std::string line;
  getline(cin, line);
  for (int i = 1; i <= ntrials; ++i) {
    int nlines = 0;
    cin >> nlines;
    getline(cin, line);
    std::ostringstream os;
    for (int j = 0; j < nlines; ++j) {
      getline(cin, line);
      os << line;
    }
    std::string tree = os.str();
    Node root;
    //int start = 0;
    //while (tree[start] != '(') ++start;
    parse(tree, root, 0);
    
    cin >> nlines;
    cout << "Case #" << i << ":\n";
    for (int j = 0; j < nlines; ++j) {
      cin >> line; // ignore
      int natts;
      cin >> natts;
      set<string> atts;
      for (int k = 0; k < natts; ++k) {
        cin >> line;
        atts.insert(line);
      }
      double p = 1.0;
      Node *x = &root;
      do {
        p *= x->weight;
        if (atts.find(x->name) != atts.end())
          x = x->yes;
        else
          x = x->no;
      } while (x != NULL);
      cout << fixed << setprecision(6) << p << '\n';
    }

  }
  return 0;
}

