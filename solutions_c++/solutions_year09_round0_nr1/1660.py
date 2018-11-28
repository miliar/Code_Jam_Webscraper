/*
 *  trie.h
 *  Alien
 *
 *  Created by John Hiesey on 9/2/09.
 *  Copyright 2009 __MyCompanyName__. All rights reserved.
 *
 */

#include <string>
using namespace std;

class trie {
public:
	trie();
	~trie();
	
	void add(string word);
	
	bool contains(string word);
	
	bool containsPrefix(string word);
	

private:
	struct trieNode {
		trieNode* children[26];
		bool isWord;
	};
	
	trieNode* root;
	
	void addToNode(string word, trieNode* & node);
	bool recContains(string word, trieNode* node, bool complete);
	void recDelete(trieNode* node);

};