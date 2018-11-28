#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <list>
#include <string>
#include <vector>

using namespace std;

int N, L, A;

class Tree {
 public:
  double p;
	string feature;
	Tree *parent;
	Tree *left;
	Tree *right;

	Tree(Tree *_parent) {
		left = right = NULL;
		parent = _parent;
		feature = "";
	}

  ~Tree() {
		delete left;
		delete right;
	}
};

void Solve(const map<string, bool> &animal, Tree *tree) {
	double answer = tree->p;
	Tree *current = tree;
	while (current->feature != ")") {
		//cout << answer << " " << current->feature << endl;
		if (animal.find(current->feature) != animal.end()) {
			current = current->left;
		} else {
			current = current->right;
		}
		answer *= current->p;
	}
	printf("%10.9lf\r\n", answer);
}

void Init() {
  cin >> N;
	for(int i = 0; i < N; ++i) {
		Tree *tree = new Tree(NULL);
		Tree *current = tree;
		cout << "Case #" << i + 1 << ":" << endl;
		cin >> L;
		//cout << L;
		while (current != NULL) {
			char c;
			scanf("%c", &c);
			while (c != '(' && c != ')') {
				scanf("%c", &c);
			}
			if (c == ')') {
				if (current->parent != NULL && current->parent->left == current) {
					//cout << "right" << endl;
					current = current->parent->right;
					continue;
				}
				//cout << ")" << "parent" << endl;
				current = current->parent;
				continue;
			}
			scanf("%lf", &(current->p));
			scanf("%c", &c);
			while (c == ' ' || c == '\n' || c == '\r' || c == '\t') {
				scanf("%c", &c);
			}
			current->feature = c;
			if (c != ')') {
				current->feature = "";
				while (c != ' ' && c != '\n' && c != '\r' || c == '\t') {
					current->feature += c;
					scanf("%c", &c);
				}
			}
			//cout << current->p << " " << current->feature << endl;
			if (current->feature == ")") {
				if (current->parent != NULL && current->parent->left == current) {
					//cout << "right" << endl;
					current = current->parent->right;
					continue;
				}
				//cout << "parent" << endl;
				current = current->parent;
			} else {
				//cout << "left" << endl;
				current->left = new Tree(current);
				current->right = new Tree(current);
				current = current->left;
			}
		}
		cin >> A;
		//cout << A << endl;
		for(int k = 0; k < A; ++k) {
			string name;
			int n;
			cin >> name >> n;
			map<string, bool> animal;
			for(int j = 0; j < n; ++j) {
				string feature;
				cin >> feature;
				animal[feature] = true;
			}
			Solve(animal, tree);
		}
	}
}


int main() {
	Init();
	return 0;
}
