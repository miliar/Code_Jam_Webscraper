#include <iostream>
#include <vector>
#include <map>

using namespace std;

typedef unsigned int uint;

class Node{
public:
	string name;
	map<string, Node> children;

	Node(){}
	Node( string n ):name(n){}
};

vector<string> split( const string& s, const string& delimiter ){
  vector<string> result;
  string::size_type from = 0;
  string::size_type to = 0;

  while ( to != string::npos ){
    to = s.find( delimiter, from );
    if ( from < s.size() && from != to ){
      result.push_back( s.substr( from, to - from ) );
    }
    from = to + delimiter.size();
  }
  return result;
}

int add_to_node( Node* current, vector<string>& path ){
	int r = 0;
	for (int i=0; i<path.size(); i++){
		if (current->children.find(path[i]) == current->children.end()){
			r++;
			Node child(path[i]);
			current->children[path[i]] = child;
		}
		current = &( current->children[path[i]] );
	}
	return r;
}

int main(){
	int t;
	cin >> t;
	for (int i=1; i<=t; i++){
		int n, m;
		cin >> n >> m;
		Node root("");
		for (int j=0; j<n; j++){
			string s;
			cin >> s;
			vector<string> path = split( s, "/" );
			//cout << root.children.size();
			add_to_node( &root, path );
		}
		int total = 0;
		for (int j=0; j<m; j++){
			string s;
			cin >> s;
			vector<string> path = split( s, "/" );
			total += add_to_node( &root, path );
		}
		cout << "Case #" << i << ": " << total <<endl;
	}
}
