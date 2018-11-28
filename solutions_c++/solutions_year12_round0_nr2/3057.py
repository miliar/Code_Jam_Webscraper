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

int solve( int N, int S, int p, vector<int> & each_points )
{
	int ret = 0;
	int surprise = S;
	vector<int> max_points(N);

	Rep(i, N){
		max_points[i] = (each_points[i] % 3 == 0) 
						? (each_points[i] / 3) : (each_points[i] / 3) + 1;
	}

	Rep(i, N){
		if(max_points[i] >= p){
 			ret++;
		}
		else if(p - max_points[i] == 1){
			// check use surprising
			if( each_points[i] >= 2 && (each_points[i] % 3 != 1) && surprise > 0 ){
				// use surprising
				ret++;
				surprise--;
			}
		}
	}

	return ret;
}

int main()
{
	int T = 0;
	int N = 0;
	int S = 0;
	int p = 0;
	vector< int > ans;

	cin >> T;

	for( int t = 0; t < T; t++ ){
		cin >> N >> S >> p;

		vector<int> each_points(N);
		Rep(i, N){
			cin >> each_points[i];
		}
		ans.push_back( solve(N, S, p, each_points) );
	}

	Rep(i, ans.size()){
		cout << "Case #" << i + 1 << ": " << ans[i] << endl;
	}

	// stop
	cin >> T;

	return 0;
}



