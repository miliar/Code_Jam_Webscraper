////////////////////////////////////////////////////////////////////
// This source code is for Visual C++ 2010 Express
////////////////////////////////////////////////////////////////////
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iterator>
#include <stack>
#include <functional>
#include <iomanip>
#include <string>
#include <cstring>
#include <deque>
#include <math.h>
#include "UnionFind.h"

#define	numberof(a)	(sizeof(a) / sizeof(a[0]))
#define	INF		(1000000)
#define Rep(i,n) for(int i = 0; i < (n); i++ )

using namespace std;

typedef vector< vector<int> > mat;
typedef pair<int, int> P;
typedef long long ll;
struct Point{
	ll x;
	ll y;
	Point() {};
	Point( ll xx, ll yy ) : x(xx), y(yy) {};
};

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);

string solve( string str, vector<char> & lang_map )
{
	string ret = "";

	Rep(i, str.length()){
		char tar = str[i];
		if( tar != ' ' ) {
			bool isUpper = isupper(tar);
			if( isUpper ){
				tar = tolower(tar);
				tar = lang_map[tar - 'a'];
				tar = toupper(tar);
			}
			else{
				tar = lang_map[tar - 'a'];
			}
		}
		ret += tar;
	}

	return ret;
}

vector<char> create_dictionary( void )
{
	vector<char> ret('z' - 'a' + 1, '-');
	vector<string> str1;
	vector<string> str2;
	set<char> chars;

	str1.push_back("a zoo");
	str1.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
	str1.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	str1.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");
 
	str2.push_back("y qee");
	str2.push_back("our language is impossible to understand");
	str2.push_back("there are twenty six factorial possibilities");
	str2.push_back("so it is okay if you want to just give up");

	Rep(i, str1.size()){
		Rep(j, str1[i].length()){
			if( str1[i][j] != ' ' ){
				ret[str1[i][j] - 'a'] = str2[i][j];
				chars.insert( str2[i][j] );
			}
		}
	}

	// check
	Rep(i, ret.size()){
		if( ret[i] == '-' ){
			for( char c = 'a'; c <= 'z'; c++ ){
				if( chars.find(c) == chars.end() ){
					ret[i] = c;
					break;
				}
			}
		}
	}

	Rep(i, ret.size()){
//		cout << static_cast<char>(i + 'a') << " -> " << ret[i] << endl;
	}

	return ret;
}

int main()
{
	int T = 0;
	string str = "";
	vector< string > ans;
	vector<char> lang_map;

	cin >> T;

	lang_map = create_dictionary();

	getline(cin, str);
	for( int t = 0; t < T; t++ ){
		getline( cin, str );
		ans.push_back( solve(str, lang_map) );
	}

	Rep(i, ans.size()){
		cout << "Case #" << i + 1 << ": " << ans[i] << endl;
	}

	// stop
	cin >> T;

	return 0;
}



