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

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;

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
		
		map<char,int> num;
		VI left;
		REP(i,str.size()) {
			num.insert( make_pair(str[i],-1) );
		}

		int base = num.size();

		if( num.size() == 1 ) {
			long long int ret = 0;
			REP(i,str.size())
				ret += pow(2.0,(double)i);
			fout << "Case #" << l+1 << ": " << ret << endl;
		} else {
			num[ str[0] ] = 1;
			int count = 0;
			FOR(i,1,str.size()) {
				if( num.find( str[i] )->second == -1 ) {
					num[ str[i] ] = count;
					count++;
					if( count == 1 )
						count++;
				}
			}

			unsigned long long int ret = 0;
			reverse(ALL(str));

			REP(i,str.size()) {
				//unsigned long long int a = num.find( str[i] )->second;
				assert( num.find( str[i] ) != num.end() );
				assert( num[ str[i] ] != -1 );
				ret += (long long)pow((double)base,i)*( num[ str[i] ] );
			}

			fout << "Case #" << l+1 << ": " << ret << endl;
		}


		//fout << "Case #" << l+1 << ": " << ret << endl;
	}


	
	return 0;
}