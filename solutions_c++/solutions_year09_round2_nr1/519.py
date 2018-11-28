#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <set>
#include <algorithm>
#include <list>
#include <queue>
//#include <fstream>

using namespace std;

typedef struct _node {
	double p;
	string name;
	_node *left;
	_node *right;
}node;

string str_tree;

void trim(string &str)
{
	//cout << str << endl;
	if(str.length() > 0) {
		while(str[0] == ' ') {
			str = str.substr(1);
		}
	}
}

void build_tree( node *head )
{
	//head = new node;

	trim( str_tree );
	// '('
	if( str_tree[0] == '(' ) {
		str_tree = str_tree.substr(1);
		trim( str_tree );

		int len;
		
		// p
		len = str_tree.find_first_of(" )");
		head->p = atof( str_tree.substr(0, len).c_str() );
		str_tree = str_tree.substr(len);
		trim( str_tree );

		if( str_tree[0] == ')' ) {
			str_tree = str_tree.substr(1);
			trim( str_tree );

			head->name = "";
			head->left = NULL;
			head->right = NULL;
		}
		else {

			// name
			len = str_tree.find_first_of(" ");
			head->name = str_tree.substr(0, len);
			str_tree = str_tree.substr(len);
			trim( str_tree );

			// tow node
			head->left = new node;
			head->right = new node;
			build_tree( head->left );
			build_tree( head->right );

			// ')'
			str_tree = str_tree.substr(1);
			trim( str_tree );
		}
	}
}

set <string> features;

double run_tree(node *cur, double x)
{
	//cout << x << endl;
	double res = x * (cur->p);

	if( cur->name.length() == 0 ) {
		return res;
	}
	else {
		if( features.count( cur->name ) == 0 ) {
			return run_tree( cur->right, res );
		}
		else {
			return run_tree( cur->left, res );
		}
	}
}

void solve()
{
	int L;
	string buffer;
	getline( cin, buffer );
	L = atoi( buffer.c_str() );
	str_tree = "";
	for(int i = 0; i < L; i++) {
		getline( cin, buffer );
		str_tree += " " + buffer;
	}

	//cout << str_tree << endl;
	node *head = new node;
	build_tree(head);

	//cout << "build success!" << endl;

	int A;
	getline( cin, buffer );
	A = atoi( buffer.c_str() );
	for(int i = 0; i < A; i++) {
		string animal;
		cin >> animal;
		int n;
		cin >> n;
		features.clear();
		string feature;
		for(int j = 0; j < n; j++) {
			cin >> feature;
			features.insert( feature );
		}
		//cout << head->right->p << endl;
		printf("%.6lf\n", run_tree(head, 1.0f));
		getline( cin, buffer );
	}
}

int main()
{
    int N;
    string Buffer;
    getline(cin, Buffer);
    N = atoi(Buffer.c_str());
    for(int i = 0; i < N; i++) {
        cout << "Case #" << i+1 << ": ";
        cout << endl;
		solve();
    }
    return 0;
}
