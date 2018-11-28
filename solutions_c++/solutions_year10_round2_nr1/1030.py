#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>

using namespace std;

int output = 0;

class Node {
	public:
	string name;
	vector<Node*> children;
	
	Node(string name) { 
		this->name = name;
	}
	
	~Node() {
		for (int i=0;i<children.size();i++)
			delete children[i];
	}
	bool tryToAdd(string toBeAdded,bool increment); // return false if node already exists, true otherwise
};

bool Node::tryToAdd(string toBeAdded,bool increment) {
	bool exists = false;
	int cut = toBeAdded.find('/',0);
	string dir = toBeAdded.substr(0,cut);
	Node *fresh;
	for (int i=0;i<children.size();i++)
		if (children[i]->name == dir) {
			exists = true;
			fresh = children[i];
			break;
		}
//	cout<<"GELGEL "<<toBeAdded<<" "<<output<<endl;
	if (!exists) {
		if (increment) output++;
		fresh = new Node(dir);
		children.push_back(fresh);
	}
	if (cut==-1) return false;
	string freshStr = toBeAdded.substr(cut+1,toBeAdded.size()-cut);
	fresh->tryToAdd(freshStr,increment);
}

int main() {
	int T,N,M;
	cin>>T;
	for (int i=0;i<T;i++) {
		string rootName = "/";
		Node root(rootName);
		cin>>N>>M;
		output = 0;
		for (int j=0;j<N;j++) {
			string dir;
			cin>>dir;
			dir = dir.substr(1,dir.size()-1);
			root.tryToAdd(dir,false);
		}
		for (int j=0;j<M;j++) {
			string dir;
			cin>>dir;
			dir = dir.substr(1,dir.size()-1);
			root.tryToAdd(dir,true);
		}
		cout<<"Case #"<<i+1<<": "<<output<<endl;
	}
}