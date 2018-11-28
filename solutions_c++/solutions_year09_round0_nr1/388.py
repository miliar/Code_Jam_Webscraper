
#include <iostream>
#include <algorithm>
#include <vector>
#include <stdlib.h>
using namespace std;

int l,d;


class Node {
public:
	struct Node *branch[26];
	int count[26];
	int cache;
	Node() {
		for (int i=0; i<26; i++) {
			branch[i]=NULL;
			count[i]=0;
			cache=-1;
		}
	}
};

Node *root;

void clearCache(Node *node) {
	if (node!=NULL) {
		node->cache=-1;
		for (int i=0; i<26; i++) clearCache(node->branch[i]);
	}
}

int solve(Node *node, string a[], int index) {
	if (index==l) {return 1;}
	if (node->cache!=-1) {return node->cache;}

	node->cache=0;
	for (int i=0; i<a[index].size(); i++) {
		int c = a[index][i]-'a';
		if (node->branch[c]!=NULL) {
			node->cache += solve(node->branch[c], a, index+1);
		}
	}

	return node->cache;
}

int solveCase() {
	string str;
	getline(cin,str);

	string a[l];
	for (int i=0; i<l; i++) a[i]="";

	bool opened=false;
	int j=0;
	for (int i=0; i<str.size(); i++) {
		if (str[i]=='(') {opened=true;continue;}
		if (str[i]==')') {opened=false;j++;continue;}
		a[j]+=str[i];
		if (!opened) j++;
	}

	clearCache(root);
	return solve(root,a,0);
}


int main() {
	int ncases;

	scanf("%d %d %d",&l,&d,&ncases);
	cin.ignore();

	root = new Node();

	for (int i=0; i<d; i++) {
		string str;
		getline(cin,str);
		Node *node = root;
		for (int i=0; i<l; i++) {
			int c = str[i]-'a';
			if (node->branch[c]==NULL) {
				node->branch[c] = new Node();
			}
			node->count[c]++;
			node = node->branch[c];
		}
	}

	for (int i=0; i<ncases; i++) {
		cout<<"Case #"<<i+1<<": "<<solveCase()<<"\n";
	}
	return 0;
}

