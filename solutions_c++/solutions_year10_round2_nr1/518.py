//#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

ifstream cin("A-large.in",ios::in);
ofstream cout("A-large.out",ios::out);

struct node {
	string val;
	bool mark;
	vector <node> child;
};

int bfs(node cur) {
	int ans = 0;
	if (cur.mark == 0)
		ans ++;
	for (int i=0; i<cur.child.size(); i++)
		ans += bfs(cur.child[i]);
	return ans;
}

void go() {
	int N, M;
	cin >> N >> M;
	node root;
	root.val = "";
	root.mark = 1;
	string temp1, temp2;
	for (int c=0; c<N; c++) {
		cin >> temp1;
		node* current = &root;
		for (int i=1; i<temp1.length(); i++) {
			temp2 = "";
			for (;i<temp1.length() && temp1[i]!='/'; i++)
				temp2.push_back(temp1[i]);
			int j;
			for (j=0; j<current->child.size(); j++)
				if (current->child[j].val == temp2)
					break;
			if (j==current->child.size()) {
				node temp;
				temp.val = temp2;
				temp.mark = 1;
				current->child.push_back(temp);
				current = &(current->child[current->child.size()-1]);
			}
			else
				current = &(current->child[j]);
		}
	}
	for (int c=0; c<M; c++) {
		cin >> temp1;
		node* current = &root;
		for (int i = 1; i<temp1.length(); i++) {
			temp2 = "";
			for (;i<temp1.length() && temp1[i]!='/'; i++)
				temp2.push_back(temp1[i]);
			int j;
			for (j=0; j<current->child.size(); j++)
				if (current->child[j].val == temp2)
					break;
			if (j==current->child.size()) {
				node temp;
				temp.val = temp2;
				temp.mark = 0;
				current->child.push_back(temp);
				current = &(current->child[current->child.size()-1]);
			}
			else
				current = &(current->child[j]);
		}
	}
	cout << bfs(root);
}

int main() {
	int T;
	cin>>T;
	for (int i=1; i<=T; i++) {
		cout<<"Case #"<<i<<": ";
		go();
		cout<<endl;
	}
	return 0;
}