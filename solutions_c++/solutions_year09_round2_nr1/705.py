#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <numeric>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <utility>
#include <stack>

#include <boost/tokenizer.hpp>
#include <boost/typeof/typeof.hpp>

using namespace std;
using namespace boost;

const double EPS = 1e-9;

template<class T> inline std::string toString(T arg) {std::stringstream ss(""); ss << arg; return ss.str(); }
template<class To, class From> To castToFrom(From arg) {To ret; std::stringstream ss(""); ss << arg; ss >> ret; return ret; }

#define PB push_back
#define INF INT_MAX
#define FOR(i,a,b) for(int i=a; i<(b); i++)
#define REP(i,b) for(int i=0; i<(b); i++)
#define typeof BOOST_TYPEOF
#define FOROB(X,ite) for( typeof(X.begin()) ite = X.begin(); ite!=X.end(); ++ite)
#define ALL(X) X.begin(), X.end()

template<class T>
void MSG_HELP(const std::vector<T>&  arg) {
	const int SIZE = arg.size();
	std::cout << '[' << SIZE << "]{";
	if( SIZE-1 >= 0 )
		FOR(i,0,SIZE-1)
			std::cout << arg[i] << ',';
	cout << arg.back();
	std::cout << '}';
}

template<class T>
void MSG_HELP(const std::deque<T>&  arg) {
	const int SIZE = arg.size();
	std::cout << '[' << SIZE << "] {";
	if( SIZE-1 >= 0 )
		FOR(i,0,SIZE-1)
			std::cout << arg[i] << ',';
		cout << arg.back();
	std::cout << "}";
}

template<class T>
void MSG_HELP(const T& arg) {
	std::cout << arg;
}

#define MSG(X) std::cout << #X << " = ", MSG_HELP(X), std::cout << std::endl

struct Node;

struct Node {
	string name;
	double p;
	vector<Node*> children;
	string Name() {
		string ret = "(" + castToFrom<string,double>( p ) + " " + name;
		REP(i,children.size())
			ret += children[i]->Name();
		ret += ")";
		return ret;
	}
	double calcProb(set<string>& s) {
		set<string>::iterator ite = s.find( name );
		double ret = 0;
		if( s.end() != ite ) {
			ret = p * children[0]->calcProb(s);
		} else if( children.size()>1 ) {
			ret = p * children[1]->calcProb(s);
		} else {
			ret = p;
		}
		return ret;
	}
};

bool isStart(const char ch) {
	return ch == '(';
}

bool isEnd(const char ch) {
	return ch == ')';
}

bool isDigit(const char ch) {
	if( ('0' <= ch && ch <='9') || ch == '.' )
		return true;
	else
		return false;
}

bool isName(const char ch) {
	if( ('a' <= ch && ch <='z') )
		return true;
	else
		return false;
}

int main()
{
	ifstream input("input.txt");
	ofstream fout("output.txt");
	
	if( !input.is_open() ) {
		cout << "The file is not open!\n";
		return 0;
	}

	char_separator<char> sep(" ");
	typedef tokenizer< char_separator<char> >::iterator Iter;
	
	std::string str;
	getline(input, str);

	const int probSize = castToFrom<int,string>( str );


	FOR(l,0,probSize) {
		getline(input, str);
		int size = castToFrom<int,string>( str );
		vector< set<string> > prob;
		string tree;
		REP(i,size) {
			getline(input, str);
			tree += str;
		}
		getline(input, str);
		size = castToFrom<int,string>( str );
		REP(i,size) {
			getline(input, str);
			set<string> s;
			vector<string> v;
			tokenizer< char_separator<char> > tokens(str, sep);
			FOROB(tokens,ite) {
				v.push_back(*ite);
			}
			FOR(j,2,v.size()) {
				s.insert(v[j]);
			}
			prob.push_back(s);
		}

		vector<Node*> nodeList;

		Node start;
		stack<Node*> s;
		s.push(&start);
		int c = 0;
		while( c < tree.size() ) {
			const char ch = tree[c];
			if( isDigit(ch) ) {
				Node* ptr = s.top();
				string temp;
				while( isDigit(tree[c]) ) {
					temp += tree[c];
					c++;
				}
				ptr->p = castToFrom<double>( temp );
				//c++;
			} else if( isStart(ch) ) {
				Node* ptr = new Node;
				s.top()->children.push_back(ptr);
				nodeList.push_back(ptr);
				s.push(ptr);
				c++;
			} else if( isEnd(ch) ) {
				s.pop();
				c++;
			} else if( isName(ch) ) { //Name
				Node* ptr = s.top();
				string temp;
				while( isName(tree[c]) ) {
					temp += tree[c];
					c++;
				}
				ptr->name = temp;
				//c++;
			} else {
				c++;
			}
		}

		fout.setf( ios::showpoint | ios::fixed );
		fout.precision(7);

		fout << "Case #" << l+1 << ":\n";
		REP(i,prob.size())
			fout << start.children[0]->calcProb(prob[i]) << endl;

	}

	

	
	return 0;
}