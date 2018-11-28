#include <climits>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <set>
#include <map>
#include <vector>
#include <sstream>

struct Node {
  double weight;
  std::string feature;
  Node* left;
  Node* right;

  Node(double weight, const std::string& feature = "", Node* left = 0, Node* right = 0):
    weight(weight),feature(feature), left(left),right(right) {}
};

static void printNode(const Node* node)
{
  std::cerr << "Node: weight=" << node->weight << ", feature=" << node->feature << std::endl;
  if(node->left) {
    std::cerr << "Left::" << std::endl;
    printNode(node->left);
  }
  if(node->right) {
    std::cerr << "Right::" << std::endl;
    printNode(node->right);
  }    
}


static Node* createNode(std::istream& in)
{
  while(1) {
    char c;
    in >> c;
    if(c == '(') break;
  }
  double weight;
  in >> weight;
  std::string featureOrParen;
  in >> featureOrParen;
  if(featureOrParen == ")") {
    return new Node(weight);
  }
  Node* left = createNode(in);
  Node* right = createNode(in);
  return new Node(weight, featureOrParen, left, right);
}

static double compute(const std::set<std::string>& features, const Node* node)
{
  if(node->feature.empty()) {
    return node->weight;
  }
  if(features.find(node->feature) == features.end()) {
    return node->weight*compute(features, node->right);
  } else {
    return node->weight*compute(features, node->left);
  }
}

int main() {
  int C;
  std::cin >> C;

  for(int c = 1; c <= C; ++c) {
    int L;
    std::cin >> L;
    std::cin.ignore();
    std::stringstream s;
    for(int i = 0; i < L; ++i) {
      std::string l;
      getline(std::cin, l);
      std::string ll;
      for(size_t j = 0; j < l.size(); ++j) {
	if(l[j] == ')') {
	  ll += " ";
	}
	ll += l[j];
      }
      s << ll << " ";
    }
    Node* root = createNode(s);
    //printNode(root);
    printf("Case #%d:\n", c);

    int N;
    std::cin >> N;
    for(int i = 0; i < N; ++i) {
      std::string animal;
      std::cin >> animal;
      int fn;
      std::cin >> fn;
      std::set<std::string> features;
      for(int f = 0; f < fn; ++f) {
	std::string feature;
	std::cin >> feature;
	features.insert(feature);
      }
      printf("%.7f\n", compute(features, root));
    }

    //std::cout << "Case #" << c << ": " << ANSWER << std::endl;
  }
}
