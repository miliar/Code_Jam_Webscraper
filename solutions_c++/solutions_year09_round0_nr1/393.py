//#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

ifstream cin("A-large.in",ios::in);
ofstream cout("A-large.out",ios::out);

class node {
public:
	char key;
	vector <node*> children;
	node() {key='-'; children.clear();}
	node(char k) {key=k; children.clear();}
	~node() {}
	void add(char k) {node* n = new node(k); children.push_back(n);}
};

node dic('0');
vector<char>* word;

void startDic (int D, int L) {
	char ch;
	node* n;
	bool found;
	for (int i=0; i<D; i++) {
		ws(cin);
		n = &dic;
		for (int j=0; j<L; j++) {
			cin>>ch;
			found = 0;
			for (int k=0; k<(n->children.size()); k++) {
				if (n->children[k]->key == ch) {
					n = n->children[k];
					found = 1;
					break;
				}
			}
			if (!found) {
				n->add(ch);
				n = n->children[n->children.size()-1];
			}
		}
	}
}

int recCount (int L, int i, node* n) {
	if (i==L) return 1;
	int c=0;
	for (int j=0; j<(n->children.size()); j++) {
		for (int k=0; k<word[i].size(); k++) {
			if (n->children[j]->key == word[i][k]) {
				c += recCount(L,i+1,n->children[j]);
				break;
			}
		}
	}
	return c;
}


int count (int L) {
	char ch;
	word = new vector<char>[L];
	ws(cin);
	for (int i=0; i<L; i++) {
		cin>>ch;
		if (ch=='(') {
			cin>>ch;
			while (ch!=')') {
				word[i].push_back(ch);
				cin>>ch;
			}
		}
		else word[i].push_back(ch);
	}
	return recCount (L, 0, &dic);
	delete [] word;
}

void main() {
	int L, D, N;
	cin>>L>>D>>N;
	startDic(D,L);
	for (int i=1; i<=N; i++)
		cout<<"Case #"<<i<<": "<<count(L)<<endl;
}