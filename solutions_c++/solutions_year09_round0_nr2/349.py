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

typedef pair<int,int> Point;

class Map 
{
public:
	Map(int x, int y) : x_(x), y_(y) { 
		map_.resize(x_);
		FOR(i,0,x_)
			map_[i].resize(y_);
	}
	Point flowsTo(int x, int y) {
		return flowSolver(x,y);
	}
	bool setMap( vector< vector<int> >& map ) {
		assert(map_.size() == map.size() );
		map_ = map;
		return true;
	}
	vector< vector< char > > getMap() {
		vector< char > v(y_);
		vector< vector< char > > ret(x_,v);
		map< Point, char > sink;
		char ch = 'a';
		FOR(y,0,y_) {
			FOR(x,0,x_) {
				Point temp = flowsTo(x,y);
				if( sink.end() == sink.find( temp ) ) {
					sink.insert( make_pair( temp, ch ) );
					ret[x][y] = ch;
					ch++;
				} else {
					ret[x][y] = sink[temp];
				}
			}
		}
		return ret;
	}
	int operator()(int x, int y) {
		if( x < 0 || x_ <= x || y < 0 || y_ <= y )
			return INT_MAX;
		else
			return map_[x][y];
	}
	int operator()(Point& point) {
		return operator()(point.first, point.second);
	}
private:
	Point flowSolver(int x, int y) {
		vector< pair<int, Point> > v;
		v.push_back( make_pair( this->operator()(x, y-1), Point(x,y-1)) );
		v.push_back( make_pair( this->operator()(x-1, y), Point(x-1,y)) );
		v.push_back( make_pair( this->operator()(x+1, y), Point(x+1,y)) );
		v.push_back( make_pair( this->operator()(x, y+1), Point(x,y+1)) );

		int score = map_[x][y];
		int index = 0;
		bool flag = false;
		FOR(i,0,v.size()) {
			if( v[i].first < score ) {
				index = i;
				score = v[i].first;
				flag = true;
			}
		}
		if( flag )
			return flowSolver( v[index].second.first, v[index].second.second );
		else
			return Point(x,y);
	}
	vector< vector<int> > map_;
	const int x_;
	const int y_;
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

	const int probSize = castToFrom<int,string>( str );

	FOR(l,0,probSize) {
		getline(input, str);
		tokenizer< char_separator<char> > tokens(str, sep);

		Iter ite = tokens.begin();
		const int y = castToFrom<int,string>( *(ite++) );
		const int x = castToFrom<int,string>( *(ite++) );

		cout << y << ',' << x << endl;
		
		vector< vector<int> > map;
		FOR(i,0,y) {
			getline(input, str);
			tokenizer< char_separator<char> > tok(str, sep);
			vector<int> temp;
			for(Iter ite = tok.begin(); ite!=tok.end(); ++ite)
				temp.push_back( castToFrom<int,string>( *ite ) );
			map.push_back(temp);
		}
		vector< vector<int> > mapT;
		mapT.resize(x);
		FOR(i,0,x)
			mapT[i].resize(y);

		FOR(i,0,x)
			FOR(j,0,y)
				mapT[i][j] = map[j][i];

		Map waterMap(x,y);
		waterMap.setMap(mapT);
		vector< vector< char > > ans = waterMap.getMap();

		FOR(j,0,y) {
			FOR(i,0,x)
				cout << ans[i][j] << ' ';
			cout << endl;
		}
		cout << endl;
		cout << "================" << endl;

		fout << "Case #" << l+1 << ":\n";
		FOR(j,0,y) {
			FOR(i,0,x)
				fout << ans[i][j] << ' ';
			fout << endl;
		}

	}

	return 0;
}