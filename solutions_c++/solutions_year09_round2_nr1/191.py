#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

int main(void)
{
  int C; cin >> C;
  for (int c = 1; c <= C; c++) {
    int L; cin >> L;
    string line; getline(cin, line);
    string tree;
    for (int i = 0; i < L; i++) {
      getline(cin, line);
      tree += line;
    }
    /*
    int nodes = 0;
    vector <string> feature; feature.push_back("");
    vecotr <double> prob; prob.push_back(0);
    vector <int> first_tree; first_tree.push_back(0);
    vector <int> second_tree; second_tree.push_back(0);
    vector <int> pos_stack; pos_stack.push_back(0);
    
    while (i < tree.length()) {
      if (tree[i] == '(') {
	i++;
	if (first_tree[pos_stack.back()]
	prob.push_back(0);
	feature.push_back("");
	first_tree.push_back(0);
	second_tree.push_back(0);
	pos_stack.push_back(nodes);
	nodes++;
	sscanf(tree[i].substr(i).c_str(), "%f", &prob[pos_stack.back()]);
	while (isdigit(tree[i]) || tree[i] == '.')
	  i++;
      }
      else if (isalpha(tree[i])) {
	while (isalpha(tree[i])) {
	  feature[pos_stack.back()] += tree[i];
	  i++;
	}
      }
      else if (tree[i] == ')') {
	i++;
	pos_stack.pop_back();
      }
      else { // space
	i++;
      }
    }
    */

    printf("Case #%d:\n", c);

    int A; cin >> A;
    for (int a = 0; a < A; a++) {
      double ans = 1;
      string animal; cin >> animal;
      int n; cin >> n;
      set <string> features; string feature;
      for (int f = 0; f < n; f++) {
	cin >> feature; features.insert(feature);
      }
      int pos = 0;
      while (pos < tree.length()) {
	if (tree[pos] == '(') {
	  pos++;
	  double prob;
	  sscanf(tree.substr(pos).c_str(), "%lf", &prob);
	  //cout << prob << endl;
	  ans *= prob;
	  while (isdigit(tree[pos]) || tree[pos] == '.')
	    pos++;
	}
	else if (isalpha(tree[pos])) {
	  feature = "";
	  while (isalpha(tree[pos])) {
	    feature += tree[pos];
	    pos++;
	  }
	  if (features.count(feature)) {
	    ; // keep going
	  }
	  else { // get rid of sub-tree
	    while (tree[pos] != '(')
	      pos++;
	    pos++;
	    int depth = 1;
	    while (depth != 0) {
	      if (tree[pos] == '(')
		depth++;
	      else if (tree[pos] == ')')
		depth--;
	      pos++;
	    }
	  }
	}
	else if (tree[pos] == ')')
	  break;
	else
	  pos++;
      }
      printf("%.7f\n", ans);
    }
  }
  return 0;
}
