#include <iostream>
#include <vector>
#include <sstream>
#include <set>
using namespace std;

struct node {
	string feature;
	double weight;
	node *next[2];
	node(string f, double w) {
		feature = f;
		weight = w;
		memset( next, 0, sizeof next );
	}
	~node() {
		for(int i=0;i<2;++i) if( next[i] != NULL ) delete next[i];
	}

};

stringstream in;
set<string> Set;
node *makeDT() {
	string x, t;
	double weight;
	in >> weight;
	in >> t;
	if( t == ")" ) {
		return new node( "", weight );
	}
	else {
		node *newNode = new node( t, weight );
		int i = 0;
		in >> t;
		newNode->next[0] = makeDT();
		in >> t;
		newNode->next[1] = makeDT();
		in >> t;
		return newNode;
	}
}

double calc( node *now ) {
	if( now->feature == "" ) return now->weight;
	if( Set.find(now->feature) != Set.end() ) {
		return now->weight * calc( now->next[0] );
	}
	else {
		return now->weight * calc( now->next[1] );
	}

}

int main() {
	int tn;
	cin >> tn;
	int numLine, numQuery;
	string s;
	for(int cc=1;cc<=tn;++cc) {
		cin >> numLine;
		getline(cin,s);
		string t;
		for(int i=0;i<numLine;++i) {
			getline(cin,s);
			t += s;
		}
		s.clear();
		for(int i=0;i<t.size();++i) 
			if( t[i] == '(' || t[i] == ')' ) s += " " + string(1,t[i]) + " ";
			else s += t[i];
		in.clear();
		in << s;
		in >> s;
		node *head = makeDT();
		cin >> numQuery;
		string name;
		int numFeature;
		printf("Case #%d:\n", cc);
		for(int i=0;i<numQuery;++i) {
			cin >> name >> numFeature;
			string temp;
			Set.clear();
			for(int j=0;j<numFeature;++j) {
				cin >> temp;
				Set.insert(temp);
			}
			printf("%.7lf\n", calc( head ));
		}
		delete head;
	}

}

