#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <numeric>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>

#include <boost/tokenizer.hpp>

using namespace std;
using namespace boost;

const double EPS = 1e-10;

template<class T> inline std::string toString(T arg) {std::stringstream ss(""); ss << arg; return ss.str(); }
template<class To, class From> To castToFrom(From arg) {To ret; std::stringstream ss(""); ss << arg; ss >> ret; return ret; }

#define PB push_back
#define INF INT_MAX
#define MSG(X) cout << #X << " = " << X << endl

#define FOR(i,a,b) for(unsigned int i=a; i<(b); i++)
//#define FOROB(X,it) for(typeof(X) ite = X.begin(); it!=X.end(); ++it)
#define FORALL(X) X.begin(), X.end()

struct UnknownString
{
	UnknownString(const string& str) : str_(str) {
		int c = 0;
		while( c < str.size() ) {
			if(str[c] == '(') {
				set<char> s;
				c++;
				while( str[c] != ')' ) {
					s.insert( str[c] );
					c++;
				}
				checker_.push_back(s);
				c++;
			} else {
				set<char> s;
				s.insert(str[c]);
				checker_.push_back(s);
				c++;
			}
		}
	}

	void print() {
		FOR(i,0,checker_.size()){
			typedef set<char>::iterator Iter;
			for(Iter ite = checker_[i].begin(); ite!=checker_[i].end(); ++ite)
				cout << *ite << ',';
			cout << endl;
		}
	}
	bool operator==(const string str) const {
		assert( checker_.size() == str.size() );
		FOR(i,0,str.size()) {
			if( checker_[i].end() == checker_[i].find( str[i] ) )
				return false;
		}
		return true;
	}
private:
	string str_;
	vector< set<char> > checker_;
};

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

	vector<int> num;

	tokenizer< char_separator<char> > tokens(str, sep);
	for(Iter ite = tokens.begin(); ite!=tokens.end(); ++ite) {
		num.push_back( castToFrom<int,string>(*ite));
	}

	vector<string> words;
	int c = 0;
	while( c < num[1] ) {
		getline(input, str);
		words.push_back(str);
		c++;
	}

	c = 0;
	while( c < num[2] ) {
		getline(input, str);
		UnknownString temp(str);
		//temp.print();
		int ret = 0;
		FOR(i,0,words.size()) {
			if( temp == words[i] )
				++ret;
		}
		cout << "Case #" << c+1 << ": " << ret << endl;
		fout << "Case #" << c+1 << ": " << ret << endl;
		c++;
	}
	
	return 0;
}