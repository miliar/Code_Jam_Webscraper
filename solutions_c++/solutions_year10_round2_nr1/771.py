#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int t,n,m;

struct Node{
	string name;
	Node* father;
	vector<Node*> childList;
	bool exist;
};

Node* root;

int count(Node* node){
	int total = 0;
	for(int i=0;i<(int)node->childList.size();++i){
		total += count(node->childList[i]);
	}
	total+=(node->exist ? 0 : 1);
	return total;
}

int main(){
	ifstream fin("test.in");
	ofstream fout("test.out");
	fin>>t;
	root = new Node;
	for(int time = 1; time<=t;++time){
		root->name = "";
		root->father = NULL;
		root->childList.clear();
		root->exist = true;
		fin>>n>>m;
		for(int i=0;i<n+m;++i){
			string tmp;
			fin>>tmp;
			int now = 0;
			Node* currentNode = root;
			while(now<tmp.length()){
				int pre = now;
				++now;
				while(now<tmp.length() && tmp[now]!='/') ++now;
				string dirName = tmp.substr(pre+1, now-pre-1);
				int nodePos = -1;
				for(int j = 0; j<(int)currentNode->childList.size();++j){
					if(currentNode->childList[j]->name == dirName){
						nodePos = j;
						break;
					}
				}
				if(nodePos == -1){
					Node* newNode = new Node;
					newNode->name = dirName;
					newNode->father = currentNode;
					newNode->exist = (i<n);
					newNode->childList.clear();
					currentNode->childList.push_back(newNode);
					nodePos = currentNode->childList.size()-1;
				}
				currentNode = currentNode->childList[nodePos];
			}
		}
		int result = count(root);
		fout<<"Case #"<<time<<": "<<result<<endl;
	}
	fin.close();
	fout.flush();
	fout.close();
	return 0;
}


