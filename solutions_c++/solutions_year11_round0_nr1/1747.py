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
	int solve( const int N, vector< pair<int, int> > & input )
	{
		// input[i]: (robot, button)
		int ret = 0;
		int turn = 0;
		vector<int> robot_pos(2);			// [0]:Orange, [1]:Blue

		// Init
		robot_pos[0] = 1;
		robot_pos[1] = 1;

		for( int i = 0; i < input.size(); i++ ){
			// each query
			int tar_robot = input[i].first;
			int tar_button_pos = input[i].second;
			int other_robot = (tar_robot + 1) % 2;
			int other_next_pos = INF;

			// decide behavior of each robots
			int need_turn = abs(tar_button_pos - robot_pos[tar_robot]);
			robot_pos[tar_robot] = tar_button_pos;// Move target position

			// need press button turn
			need_turn++;

			// the other robot uses need_turn
			for( int j = i + 1; j < input.size(); j++ ){
				if( input[j].first == other_robot ){
					other_next_pos = input[j].second;
					break;
				}
			}
			if( other_next_pos != INF ){
				if( other_next_pos == robot_pos[other_robot] ){
					// そのまま
				}
				else if( other_next_pos > robot_pos[other_robot] ){
					// プラス方向に移動
					robot_pos[other_robot] += need_turn;
					if( robot_pos[other_robot] > other_next_pos ){
						// 行き過ぎた場合
						robot_pos[other_robot] = other_next_pos;
					}
				}
				else{
					// マイナス方向に移動
					robot_pos[other_robot] -= need_turn;
					if( robot_pos[other_robot] < other_next_pos ){
						// 行き過ぎた場合
						robot_pos[other_robot] = other_next_pos;
					}
				}
			}

			// Next
			turn += need_turn;
		}
		// finished
		ret = turn;
		return ret;
	}
};

int main()
{
	GCJ obj;
	vector<int> ans;
	int T = 0;

	cin >> T;

	for( int t = 0; t < T; t++ ){
		vector< pair<int, int> > input;
		int N = 0;

		cin >> N;

		for( int j = 0; j < N; j++ ){
			char robot = 'O';// 'O' or 'B'
			cin >> robot;
			int input_robot = (robot == 'O') ? 0 : 1;// 0:Orange, 1:Blue

			int button = 0;
			cin >> button;

			input.push_back( make_pair(input_robot, button) );
		}

		int answer = obj.solve( N, input );
		ans.push_back( answer );
	}

	// output
	for( int i = 0; i < T; i++ ){
		cout << "Case #" << i + 1 << ": " << ans[i] << endl;
	}

	// wait
	cin >> T;

	return 0;
}

