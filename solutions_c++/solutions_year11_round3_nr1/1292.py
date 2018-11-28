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
#define Rep(i,n) for(int i = 0; i < (n); i++ )

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))

//debug
#define dump(x)  cout << #x << " = " << (x) << endl;
#define debug(x) cout << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;
#define	show(x)	 copy( (x).begin(), (x).end(), ostream_iterator<int>(cout, ",") );

using namespace std;

typedef vector< vector<int> > mat;
typedef pair<int, int> P;
typedef long long ll;

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);

class GCJ
{
public:
//	bool used[55][55];
	vector<string> solve( int R, int C, vector<string> & floor )
	{
		vector<string> ret;
		int dx[] = {0, 1, 0, 1};
		int dy[] = {0, 0, 1, 1};

//		Rep(i, 55) Rep(j, 55) used[i][j] = false;

		for( int y = 0; y < R; y++ ){
			for( int x = 0; x < C; x++ ){
//				if( used[y][x] == false )
				{
					int cnt = 0;
					Rep(k, 4){
						int xx = x + dx[k];
						int yy = y + dy[k];

						if( xx >= 0 && xx < C && yy >= 0 && yy < R ){
							if( floor[yy][xx] == '#' ){
								cnt++;
							}
						}
					}

					if( cnt == 4 ){
						// change blue tiles
						Rep(k, 4){
							int xx = x + dx[k];
							int yy = y + dy[k];
							if( k == 0 ){
								floor[yy][xx] = '/';
							}
							else if( k == 1 ){
								floor[yy][xx] = '\\';
							}
							else if( k == 2 ){
								floor[yy][xx] = '\\';
							}
							else{
								floor[yy][xx] = '/';
							}
						}
					}
				}
			}
		}

		for( int y = 0; y < R; y++ ){
			for( int x = 0; x < C; x++ ){
				if( floor[y][x] == '#' ){
					ret.push_back("Impossible");
					return ret;
				}
			}
		}

		ret = floor;
		return ret;
	}
};

int main()
{
	GCJ obj;
	vector< vector< string > > ans;
	int T = 0;

	cin >> T;

	for( int t = 0; t < T; t++ ){
		int C = 0;
		int R = 0;

		cin >> R >> C;
		vector< string > floor(R);

		Rep(i, R){
			cin >> floor[i];
		}

		ans.push_back( obj.solve(R, C, floor) );
	}

	// output
	for( int i = 0; i < T; i++ ){
		cout << "Case #" << i + 1 << ":" << endl;
		Rep(j, ans[i].size()){
			cout << ans[i][j] << endl;
		}
	}

	// wait
	cin >> T;

	return 0;
}


