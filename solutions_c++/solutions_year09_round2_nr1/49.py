#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string> 
#include <vector>
#include <stack>
#include <stdexcept>

using namespace std;

template<typename T> T stoT (const string& in) {
  istringstream is (in);
  T ret;
  is >> ret;
  return ret;
}

template<typename T> string Ttos (T in) {
  ostringstream os;
  os << in;
  return os.str();
}

struct dec_tree {
  string feature;
  dec_tree* yes;
  dec_tree* no;
  double weight;
  dec_tree() 
    : yes (0),no (0), weight (0) {}
  ~dec_tree() {
    delete yes;
    delete no;
  }
  double get_prob (const set<string>& features) const {
    double ret = weight;
    if (!(yes && no && feature.size() > 0)) return ret;
    if (features.find (feature) == features.end()) return ret * no->get_prob (features);
    else return ret * yes->get_prob (features);
  }

};

dec_tree* parse_tree (const string& desc, size_t& pos) {
  dec_tree* root = new dec_tree;
  while (isspace (desc[pos])) ++pos;
  if (desc[pos] != '(') {
    cerr << "ouch1:";
    cerr << pos << " " << desc << "\n";
    cerr << desc.substr (pos);
    abort();
  }
  
  ++pos;
  while (isspace (desc[pos])) ++pos;
  string number;
  while(!isspace (desc[pos]) && desc[pos] != ')') {
    number += desc[pos];
    ++pos;
  }
//   cerr << "weight: '" << number << "'\n";
  root->weight = stoT<double> (number);
  
  while (isspace (desc[pos])) ++pos;

  if (desc[pos] == ')') {
    ++pos;
    return root;
  }
  string feature;
  while(!isspace (desc[pos]) && desc[pos] != '(' ) {
    feature += desc[pos];
    ++pos;
  }
  root->feature = feature;
//   cerr << "parsed: " << feature << "\n";
//   cerr << desc.substr (pos);
  root->yes = parse_tree (desc,pos);
  root->no = parse_tree (desc,pos);
  while (isspace (desc[pos])) ++pos;
  if (desc[pos]!=')') {
    cerr << "ouch2";
    abort();
  }
  
  ++pos;
  return root;

  
      
}


int main() {
  int num_cases;
  cin >> num_cases;
  cin.ignore();
  
  for (int case_num = 1; case_num <=  num_cases; ++case_num) {
    cout << "Case #" << case_num << ":";
    cout << "\n";
    
    int dec_lines;
    cin >> dec_lines;
    cin.ignore();
    string tree_desc;
    for (int i = 0; i < dec_lines; ++i) {
      string line;
      getline (cin,line);
      tree_desc += line;
    }
    size_t pos = 0;
    dec_tree* root = parse_tree (tree_desc,pos);
    int num_animals;
    cin >> num_animals;
    cin.ignore();
    for (int i = 0; i < num_animals;++i) {
      string line;
      getline (cin,line);
      istringstream sline (line);
      string name;
      sline >> name;
      int num_features;
      sline >> num_features;
      set<string> features;
      for (int j = 0; j < num_features; ++j) {
        string feature;
        sline >> feature;
        features.insert (feature);
      }
      printf ("%.7lf\n",root->get_prob (features));
      
//       cout << root->get_prob (features) << "\n";
    }
    delete root;
  }
  
}
