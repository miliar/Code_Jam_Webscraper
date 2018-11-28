/*
 * main.cpp
 *
 *  Created on: 2009-9-3
 *      Author: megatang
 */

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>
using namespace std;

struct tree_node {
	bool end;
	map<char, tree_node*> next;
	bool used[256];
	tree_node() :
		end(false) {
		memset(used, 0, sizeof(used));
	}
};

void add_word(tree_node *root, const char *word) {
	if (*word == '\0')
		root->end = true;
	else {
		if (!root->used[(int)*word]) {
			tree_node *next = new tree_node();
			root->next[*word] = next;
			root->used[(int)*word] = true;
		}
		add_word(root->next[*word], word + 1);
	}
}

int calc_possibilities(tree_node *root, const char *word) {
	if (*word == '\0')
		return root->end ? 1 : 0;
	else {
		const char *next_word = word + 1;
		if (*word == '(') {
			while (*next_word != ')')
				next_word++;
			word++;
			next_word++;
		}
		int ret = 0;
		while (word < next_word) {
			if (*word == ')')
				break;
			if (!root->used[(int)*word]) {
				word++;
				continue;
			}
			ret += calc_possibilities(root->next[*word], next_word);
			word++;
		}
		return ret;
	}
}

int main() {
	int L, D, N;
	ifstream fin("input.txt");
	fin >> L >> D >> N;
	tree_node *root = new tree_node();
	for (int i = 0; i < D; i++) {
		string temp;
		fin >> temp;
		add_word(root, temp.c_str());
	}
	ofstream fout("output.txt");
	for (int i = 1; i <= N; i++) {
		string temp;
		fin >> temp;
		int ans = calc_possibilities(root, temp.c_str());
		fout << "Case #" << i << ": " << ans << endl;
	}
	fout.close();

	return 0;
}
