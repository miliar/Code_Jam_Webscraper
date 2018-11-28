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

string isWin( char who, vector<string> & field, const int N )
{
	stringstream ss("");
	string tmp = "";
	ss << who;
	ss >> tmp;

	string strwon = tmp + " won";
	string ret = "";

	Rep(i, N){
		Rep(j, N){
			if( !(field[i][j] == who ||  field[i][j] == 'T') ){
				break;
			}

			if( j == N - 1 ){
				ret = strwon;
			}
		}
		Rep(j, N){
			if( !(field[j][i] == who ||  field[j][i] == 'T') ){
				break;
			}

			if( j == N - 1 ){
				ret = strwon;
			}
		}
	}
	Rep(i, N){
		if( !(field[i][i] == who ||  field[i][i] == 'T') ){
			break;
		}

		if( i == N - 1 ){
			ret = strwon;
		}
	}
	Rep(i, N){
		if( !(field[N - i - 1][i] == who ||  field[N - i - 1][i] == 'T') ){
			break;
		}

		if( i == N - 1 ){
			ret = strwon;
		}
	}
	Rep(i, N){
		if( !(field[i][N - i - 1] == who ||  field[i][N - i - 1] == 'T') ){
			break;
		}

		if( i == N - 1 ){
			ret = strwon;
		}
	}
	Rep(i, N){
		if( !(field[N - i - 1][N - i - 1] == who ||  field[N - i - 1][N - i - 1] == 'T') ){
			break;
		}

		if( i == N - 1 ){
			ret = strwon;
		}
	}

	return ret;
}

string solve( vector<string> & field, const int N )
{
	string ret = "";
	string draw = "Draw";
	string notyet = "Game has not completed";

	ret = isWin('X', field, N);
	if( ret != "" ){
		return ret;
	}

	ret = isWin('O', field, N);
	if( ret != "" ){
		return ret;
	}

	Rep(i, N){
		Rep(j, N){
			if( field[i][j] == '.' ){
				return notyet;
			}
		}
	}

	return draw;
}

int main()
{
	int T = 0;
	const int N = 4;
	vector< string > ans;

	cin >> T;
	string tmp = "";

	Rep(t, T){
		vector< string > field(N);
		getline(cin,tmp);
		Rep(i, N){
			getline(cin, field[i]);
		}
		ans.push_back( solve(field, N) );
	}
	Rep(t, T){
		cout << "Case #" << t + 1 << ": ";
		cout << ans[t] << endl;
	}

	// stop
	cin >> T;

	return 0;
}



