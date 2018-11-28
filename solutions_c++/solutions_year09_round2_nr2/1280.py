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
#include <deque>

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
		//int prob = castToFrom<int,string>( str );
		vector<char> prob( str.begin(), str.end() );
		vector<char> current = prob;
		sort( ALL(prob) );

		set< vector< char > > s;

		do {
			if( '0' != prob[0] ) {
				//cout << "perm" << endl;
				//MSG(prob);
				s.insert(prob);
			}
		} while( next_permutation( ALL(prob) ) );
		
		
		//cout << "set" << endl;
		//FOROB(s,ite)
		//	MSG(*ite);

		set< vector< char > >::iterator ite = s.find( current );
		++ite;
		if( ite!= s.end() ) {
			string ret( ite->begin(), ite->end() );
			fout << "Case #" << l+1 << ": " << ret << endl;
		} else {
			deque<char> temp(s.begin()->begin(),s.begin()->end());
			char ch = temp.front();
			temp.pop_front();
			temp.push_front('0');
			temp.push_front(ch);
			string ret( temp.begin(), temp.end() );
			fout << "Case #" << l+1 << ": " << ret << endl;
		}

	}

	

	
	return 0;
}