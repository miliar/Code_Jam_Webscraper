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
	vector<double> solve( int N, vector< vector<char> > & mat )
	{
		vector<double> ret(N);
		vector<double> WP(N);
		vector<double> OWP(N);
		vector<double> OOWP(N);

		Rep(i, N){
			int cnt = 0;
			int win = 0;
			Rep(j, N){
				if( mat[i][j] == '1' ){
					win++;
				}
				if( mat[i][j] != '.' ) cnt++;
			}
			WP[i] = (double)win / cnt;
		}

		Rep(i, N){
			// [i]'s OWP
			vector<int> opp;
			Rep(j, N){
				if( mat[i][j] != '.' ) opp.push_back( j );
			}

			vector<double> wp_tmp;
			Rep(f, opp.size()){
				// jÇÃWP(iÇèúÇ¢ÇΩÇ‡ÇÃ)Çí≤Ç◊ÇÈ
				int index = opp[f];
				int cnt = 0;
				int win = 0;

				Rep(k, N){
					if( k == i ) continue;
					if( mat[index][k] == '1' ) win++;
					if( mat[index][k] != '.' ) cnt++;
				}
				wp_tmp.push_back( (double)win / cnt );
			}

			double sum = 0.0;
			Rep(j, wp_tmp.size()){
				sum += wp_tmp[j];
			}
			OWP[i] = sum / wp_tmp.size();
		}

		Rep(i, N){
			// [i]'s OOWP
			vector<int> opp;
			Rep(j, N){
				if( mat[i][j] != '.' ) opp.push_back( j );
			}

			double sum = 0.0;
			Rep(j, opp.size()){
				// jÇÃWP(iÇèúÇ¢ÇΩÇ‡ÇÃ)Çí≤Ç◊ÇÈ
				int index = opp[j];
				sum += OWP[index];
			}
			OOWP[i] = sum / opp.size();
		}

		Rep(i, N){
			ret[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
		}

		return ret;
	}
};

int main()
{
	GCJ obj;
	vector< vector<double> > ans;
	int T = 0;

	cin >> T;

	for( int t = 0; t < T; t++ ){
		int N = 0;

		cin >> N;

		vector< vector<char> > mat(N, vector<char>(N, '.'));

		Rep(i, N) Rep(j, N) cin >> mat[i][j];

		ans.push_back( obj.solve(N, mat) );
	}

	// output
	for( int i = 0; i < T; i++ ){
		cout << "Case #" << i + 1 << ":" << endl;
		Rep(j, ans[i].size()) printf("%f\n", ans[i][j]);
	}

	// wait
	cin >> T;

	return 0;
}


