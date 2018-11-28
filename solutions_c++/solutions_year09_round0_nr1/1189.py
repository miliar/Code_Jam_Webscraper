/**
 * Qualification Round 2009
 * g++ 3.4.5
 */
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef vector<II> VII;

template<typename T> inline int sz(const T& x) { return (int)x.size(); }


struct Node {
	Node* child[26];
	Node() { memset(child, 0, sizeof child); }
	~Node() { for(int i = 0; i < 26; ++i) delete child[i]; }
};


void insert(Node* node, string& word, int k = 0) {
	int c = word[k] - 'a';

	if( !node->child[c] )
		node->child[c] = new Node();

	if(++k < sz(word))
		insert(node->child[c], word, k);
}


int query( Node* node, VVI& pat, int k = 0 ) {
	if( k == sz(pat) )
		return 1;

	VI& alpha = pat[k];
	int am = 0;
	for(VI::iterator it = alpha.begin(); it != alpha.end(); ++it) {
		if( node->child[*it] )
			am += query( node->child[*it], pat, k+1 );
	}
	return am;
}

int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	Node* trie = new Node();

	int N, L, D;
	cin >> L >> D >> N;

	for(int i = 0; i < D; ++i) {
		string word;
		cin >> word;
		insert(trie, word);
	}

	for(int t = 1; t <= N; ++t) {
		string s;
		cin >> s;

		VVI pat(L, VI());
		int i = 0;
		bool bracket = false;
		for(int p = 0; p < sz(s); ++p) {

			if( s[p] >= 'a' && s[p] <= 'z' )
				pat[i].push_back( s[p] - 'a' );
			else if( s[p] == '(' )
				bracket = true;
			else if( s[p] == ')' )
				bracket = false;
			else
				cerr << "error" << endl;

			if(!bracket) ++i;
		}
		assert( i == L );

		int ans = query( trie, pat );
		cout << "Case #" << t << ": " << ans << '\n';
	}

	delete trie;
	return 0;
}

