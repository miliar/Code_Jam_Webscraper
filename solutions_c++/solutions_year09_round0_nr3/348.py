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
#define ALL(X) X.begin(), X.end()

typedef pair<int,int> Point;

int ans = 0;

const string prob("welcome to code jam");

struct Process {
	Process(string str) : str_(str) {
		init();
	}
	char operator()(char ch) {
		//char ret = tolower(ch);
		if( s_.find( ch ) == s_.end() )
			return '@';
		return ch;
	}
private:
	void init() {
		FOR(i,0,str_.size())
			s_.insert( str_[i] );
	}
	string str_;
	set<char> s_;
};

class Solver
{
public:
	Solver(const string& str) : str_(str) {}
	//~Solver() { MSG(memo_.size()); }
	unsigned long long int counter(int cur, int n = 0) {
		unsigned long long int ret = 0;
		if( prob.size() <= n ) {
			assert(false);
			ret = 0;
		} else if( n == prob.size()-1 || str_.size() <= cur ) {
			int temp = cur;
			while( string::npos != str_.find( prob[n], temp ) ) {
				ret++;
				temp = str_.find( prob[n], temp )+1;
			}
		} else if( n < prob.size()-1 ) {
			if( memo_.find( make_pair(cur,n) ) != memo_.end() ) {
				map< pair<int,int>, int >::iterator ite = memo_.find( make_pair(cur,n) );
				ret = ite->second;
			} else {
				int temp = cur;
				while(1) {
					int pos = str_.find( prob[n], temp );
					if( string::npos != pos ) {
						ret += counter(pos+1, n+1);
						if( ret >= 10000 )
							ret%=10000;
					} else {
						memo_.insert( make_pair( make_pair(cur,n), ret ) );
						break;
					}
					temp = pos+1;
				}
			}
		}
		return ret;
	}
private:
	const string str_;
	map< pair<int,int>, int > memo_;
};

int main()
{
	ifstream input("input.txt");
	ofstream fout("output.txt");
	
	if( !input.is_open() ) {
		cout << "The file is not open!\n";
		return 0;
	}
	
	std::string str;
	getline(input, str);

	const int probSize = castToFrom<int,string>( str );

	FOR(l,0,probSize) {
		getline(input, str);

		transform( ALL(str), str.begin(), Process(prob) );
		str.erase( remove( ALL(str), '@' ), str.end() );

		Solver solver(str);
		string ans = castToFrom<string,int>(solver.counter(0));
		FOR(i,ans.size(),4)
			ans = "0" + ans;

		cout << "Case #" << l+1 << ": " << ans << endl;
		fout << "Case #" << l+1 << ": " << ans << endl; 
	}

	return 0;
}