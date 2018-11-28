#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Node {
	Node() {
		children.resize(26);
		for (int i = 0; i < children.size(); i++)
			children[i] = 0;
	}
	char letter;
	vector<Node*> children;
};

void insert(Node* root, string dict_word);
int num_valid(Node* root, string pattern);

int main() {
	int L, D, N;
	cin >> L >> D >> N;
	string dict_word;
	Node root;
	for (int i = 0; i < D; i++) {
		cin >> dict_word;
		insert(&root, dict_word);
	}
	string pattern;
	int ret;
	for (int i = 0; i < N; i++) {
		cin >> pattern;
		ret = num_valid(&root, pattern);
		cout << "Case #" << i + 1 << ": " << ret << endl;
	}
}

string substring(string s, int start, int length = -1) {
	if (start >= s.length())
		return "";
	if (length == -1)
		return s.substr(start);
	return s.substr(start, length);
}

int num_valid(Node* root, string pattern) {
	if (pattern.length() == 0)
		return 1;
	int ret = 0;
	if (pattern[0] == '(') {
		int rb_i = 1;
		for (rb_i = 1; pattern[rb_i] != ')'; rb_i++);
		for (int i = 1; i < rb_i; i++) {
			if (root->children[pattern[i] - 'a'] != 0) {
				ret += num_valid(root->children[pattern[i] - 'a'], substring(pattern, rb_i + 1));
			}
		}
	} else {
		if (root->children[pattern[0] - 'a'] != 0)
			ret += num_valid(root->children[pattern[0] - 'a'], substring(pattern, 1));
	}
	return ret;
}

void insert(Node* root, string dict_word) {
	// base case
	if (dict_word.length() == 0)
		return;
	// recursive step
	Node* child = root->children[dict_word[0] - 'a'];
	if (child == 0) {
		Node* new_child = new Node();
		new_child->letter = dict_word[0];
		root->children[dict_word[0] - 'a'] = new_child;
	}
	insert(root->children[dict_word[0] - 'a'], substring(dict_word, 1));
}
