////////////////////////////////////////////////////////////////////
// Written by Hisaki Niikura
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
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>

#define	numberof(a)	(sizeof(a) / sizeof(a[0]))
#define	INF		(1000000)

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))

//debug
#define dump(x)  cout << #x << " = " << (x) << endl;
#define debug(x) cout << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;
#define	show(x)	 copy( (x).begin(), (x).end(), ostream_iterator<int>(cout, ",") );	// container<int>を全て表示

using namespace std;

typedef vector< vector<int> > mat;
typedef pair<int, int> P;	// (price, index)
typedef long long ll;

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);

class GCJ
{
public:
	vector<string> combine;
	vector<string> opposed;

	char getCombineChar( char c1, char c2 )
	{
		for( int i = 0; i < combine.size(); i++ ){
			if(	(c1 == combine[i][0] && c2 == combine[i][1]) 
			||	(c2 == combine[i][0] && c1 == combine[i][1]) ){
				return combine[i][2];
			}
		}
		return ' ';
	}
	string solve( int C, int D, int N, vector<string> combine, vector<string> opposed, string invoke )
	{
		string ret = "";

		this->combine = combine;
		this->opposed = opposed;

		for( int i = 0; i < invoke.length() - 1; ){
			// i + 1文字目までチェック済ということ
			// check combine
			char change_char = getCombineChar(invoke[i], invoke[i + 1]);
			if( change_char != ' ' ){
				// change
				invoke = invoke.substr(0, i) + change_char + invoke.substr(i + 2, invoke.length() - (i + 2) + 1);
				i = i - 1;
				if( i < 0 ) i = 0;
				continue;
			}

			// check opposed
			bool is_opposed = false;
			for( int j = 0; j < opposed.size(); j++ ){
				set<int> oppose_check;
				for( int l = 0; l <= i + 1; l++ ){
					for( int k = 0; k < 2; k++ ){
						char opposed_word = opposed[j][k];
						if( invoke[l] == opposed_word ){
							oppose_check.insert( k );
							break;
						}
					}
				}

				if( oppose_check.size() == 2 ){
					is_opposed = true;
					break;
				}
			}

			if( is_opposed == true ){
				invoke = invoke.substr(i + 2, invoke.length() - (i + 2) + 1);
				i = 0;
			}
			else{
				i++;
			}

			if( invoke.length() == 0 ) break;
		}

		ret += '[';
		for( int i = 0; i < invoke.length(); i++ ){
			ret += invoke[i];
			if( i != invoke.length() - 1 ) ret += ", ";
		}
		ret += ']';

		return ret;
	}
};

int main()
{
	GCJ obj;
	vector<string> ans;
	int T = 0;

	cin >> T;

	for( int t = 0; t < T; t++ ){
		int C = 0;
		int D = 0;
		int N = 0;
		vector<string> combine;
		vector<string> opposed;
		string invoke = "";
		string tmp = "";

		cin >> C;

		for( int j = 0; j < C; j++ ){
			cin >> tmp;
			combine.push_back( tmp );
		}

		cin >> D;

		for( int j = 0; j < D; j++ ){
			cin >> tmp;
			opposed.push_back( tmp );
		}

		cin >> N;
		cin >> invoke;

		ans.push_back( obj.solve(C, D, N, combine, opposed, invoke) );
	}

	// output
	for( int i = 0; i < T; i++ ){
		cout << "Case #" << i + 1 << ": " << ans[i] << endl;
	}

	// wait
	cin >> T;

	return 0;
}

