/**
 * Round 1B, 2009
 * g++ 3.4.5
 */
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <algorithm>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef vector<II> VII;

template<typename T> inline int sz(const T& x) { return (int)x.size(); }


struct Node {
	double weight;
	string feature;
	Node *left, *right;

	Node() { left = 0; right = 0; }
	~Node() { delete left; delete right; }
};



Node* make_tree( string& str, int begin, int end ) {
	Node *n = new Node();

	stringstream ss( str.substr( begin, end-begin+1 ) );
	//cout << "[" << str.substr( begin, end-begin+1 ) << "]" << endl;

	//double weight;
	ss >> n->weight;

	string feat;
	ss >> feat;

	if( feat.size() > 0 ) {
		//cout << "read feature: [" << feat << "]" << endl;
		n->feature = feat;

		begin = str.find_first_of( '(', begin ) + 1;
		end = begin;

		int cnt = 1;
		while( cnt ) {

			if( str[end] == '(' )
				++cnt;
			else if( str[end] == ')' )
				--cnt;

			++end;
		}

		n->left = make_tree( str, begin, end-2 );

		begin = str.find_first_of( '(', end ) + 1;
		end = begin;

		cnt = 1;
		while( cnt ) {

			if( str[end] == '(' )
				++cnt;
			else if( str[end] == ')' )
				--cnt;

			++end;
		}

		n->right = make_tree( str, begin, end-2 );
	} else {
		n->left = n->right = 0;
	}

	return n;
}


struct Animal {
	set<string> features;
};


double query( Node* tree, Animal& animal ) {
	double p = tree->weight;

	if(tree->left) {

		if( animal.features.count( tree->feature ) ) {
			p *= query( tree->left, animal );
		} else {
			p *= query( tree->right, animal );
		}

	}

	return p;
}


void print_tree( Node *tree ) {
	//cout << "(" << tree->weight;

	if( tree->feature.size() > 0 ) {
		cout << " " << tree->feature << endl;
		print_tree( tree->left );
		print_tree( tree->right);
	}

	//cout << ")" << endl;
}

int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	char buf[256];

	int N;
	cin >> N;
	//cin.ignore(100, '\n');
	cin >> ws;

	for(int tc = 1; tc <= N; ++tc) {
		cout << "Case #" << tc << ":\n";

		int L; cin >> L; cin >> ws;

		string tree_string;
		for(int i = 0; i < L; ++i) {
			string line;
			getline(cin, line);
			tree_string.append(" ");
			tree_string.append(line);
		}

		//if( tc == 79 )
			//cout << tree_string << endl;

		int begin = tree_string.find_first_of('(', 0) + 1;
		int last = tree_string.find_last_of( ')' ) - 1;
		Node *tree = make_tree( tree_string, begin, last );

		//if( tc == 79 )
			//print_tree( tree );

		int A;
		cin >> A;

		vector<Animal> animals;
		animals.resize(A);

		for(int i = 0; i < A; ++i) {
			string str; cin >> str;
			int num; cin >> num;
			for(int j = 0; j < num; ++j) {
				cin >> str;
				animals[i].features.insert( str );
			}

			sprintf(buf, "%.11lf", query( tree, animals[i] ) );
			cout << buf << '\n';
		}

		delete tree;
	}


	return 0;
}
