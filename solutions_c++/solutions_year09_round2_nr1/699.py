#include <iostream>
#include <string>
#include <cstdio>
#include <sstream>
#include <set>
#include <iomanip>
using namespace std;

struct Node {
	double weight;
	string f;
	int c1, c2;
} nodes[5000];

struct Animal {
	set<string> f;
	int n;
	string name;
} animals[110];

int N, L, A;
int nNodes;
string line;
string treeStr;

void readInput()
{
	treeStr = "";

	getline(cin, line);
	istringstream ss(line);
	ss >> L;
	
	for (int i = 0; i < L; i++) {
		getline(cin, line);
		treeStr += line;
	}
	
	string temp = treeStr;
	treeStr = "";
	
	for (size_t i = 0; i < temp.size(); i++) {
		if (temp[i] == '(') {
			treeStr += " ";
			treeStr += temp[i];
			treeStr += " ";
		} else if (temp[i] == ')') {
			treeStr += " ";
			treeStr += temp[i];
			treeStr += " ";
		} else {
			treeStr += temp[i];
		}
	}

	getline(cin, line);
	istringstream ss2(line);
	ss2 >> A;
	
	for (int i = 0; i < A; i++) {
		getline(cin, line);
		istringstream ss3(line);
		ss3 >> animals[i].name;
		ss3 >> animals[i].n;
		animals[i].f.clear();
		
		for (int j = 0; j < animals[i].n; j++) {
			ss3 >> temp;
			animals[i].f.insert(temp);
		}
	}
}

int readNode(istringstream &iss)
{
	//cout << nNodes << endl;
	string temp;
	
	int num = nNodes++;
	
	iss >> nodes[num].weight;
	iss >> temp; //feature

	//tem filhos
	if (temp != ")") {
		nodes[num].f = temp;
		iss >> temp; //'('
		nodes[num].c1 = readNode(iss);
		iss >> temp; //'('
		nodes[num].c2 = readNode(iss);
		iss >> temp; // ')'
	} else {
		nodes[num].f = "";
		nodes[num].c1 = nodes[num].c2 = -1;
	}
	
	return num;
}

void buildTree()
{
	istringstream iss(treeStr);
	string temp;
	iss >> temp; //primeiro '('
	nNodes = 0;
	readNode(iss);
}

double visitTree(int a, int node, double p)
{
	//cout << "a visitar " << node << endl;
	p *= nodes[node].weight;
	
	if (animals[a].f.find(nodes[node].f) != animals[a].f.end()) {
		if (nodes[node].c1 != -1) {
			p = visitTree(a, nodes[node].c1, p);
		}
	} else {
		if (nodes[node].c2 != -1) {
			p = visitTree(a, nodes[node].c2, p);
		}
	}
	
	return p;
}

int main()
{
	getline(cin, line);
	istringstream ss(line);
	ss >> N;
	
	cout.setf(ios::fixed);
	
	for (int nCase = 1; nCase <= N; nCase++) {
		readInput();
		//cout << treeStr << endl;
		buildTree();
		printf("Case #%d:\n", nCase);
		
		for (int i = 0; i < A; i++) {
			cout << setprecision(7) << visitTree(i, 0, 1.) << endl;
		}
		
	}

	return 0;
}
