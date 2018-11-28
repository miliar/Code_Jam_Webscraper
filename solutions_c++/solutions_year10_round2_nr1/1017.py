#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <sstream>
using namespace std;

#define fout cout << "Case #" << ++iCase << ": "
char *inFile = "A-large.in";
char *outFile = "A-large.out";
int iCase = 0;

struct Node {
	string s;
	vector<Node*> branch;
	Node() {
		branch.clear();
	}
	inline void init() {
		branch.clear();
	}
}node[100000];
int nNode = 0;
Node* getNewNode() {
	return &node[nNode++];
}
int ret;


string word[100];
int nWord;

void show(Node *root, int depth) {
	if(root==NULL)return;
	for(int i=0; i<depth; ++i)
		cout << "---";
	cout << root->s << endl;
	for(int i=0; i<root->branch.size(); ++i)
		show(root->branch[i], depth+1);
}
void addNode(Node *root, bool add) {
	bool flag;
	for(int j=0; j<nWord; ++j) {
		flag = false;
		for(int i=0; i<root->branch.size(); ++i) {
			if(root->branch[i]->s == word[j]) {
				root = root->branch[i];
				flag = true;
				break;
			}
			
		}
		if(!flag) {
			(root->branch).push_back(getNewNode());
			root->branch[root->branch.size()-1]->s = word[j];
			root = root->branch[root->branch.size()-1];
			if(add) ++ret;
		}
	}
}

void split(string s) {
	for(int i=0; s[i]; ++i)
		if(s[i] == '/')
			s[i] = ' ';
	istringstream is(s);
	nWord = 0;
	while(is >> word[nWord]) {
		++nWord;
	}
}


void runTest() {
	int m, n;
	cin >> m >> n;
	string s;
	Node *root = getNewNode();
	for(int i=0; i<m; ++i) {
		cin >> s;
		split(s);
		addNode(root, false);
	}
	//show(root, 0);
	//cout << "-----" << endl;
	ret = 0;
	for(int i=0; i<n; ++i) {
		cin >> s;
		split(s);
		addNode(root, true);
	}
	fout << ret << endl;
	//show(root, 0);
	for(int i=0; i<nNode; ++i)
		node[i].init();
	nNode = 0;
}

int main(void)
{ 
	freopen(inFile, "r", stdin);
	freopen(outFile, "w", stdout);
	int k;
	for(cin>>k; k>0; --k)
		runTest();
//	system("pause");
}

