#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>

#define REP(i, n) for( i = 0; i < n; i++ )

using namespace std;

int main()
{
	freopen("a-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);

	int N;
	cin >> N;
	for( int cas = 1; cas <= N; cas++ )
	{
		int n;
		cin >> n;

		int curr_pos_b, curr_pos_o;
		int buffer_b, buffer_o;

		curr_pos_b = curr_pos_o = 1;
		buffer_b = buffer_o = 0;
		long long int ans = 0;
		char c;
		int next_pos;
		for( int i = 0; i < n; i++ )
		{
			cin >> c;
			cin >> next_pos;
			if( c == 'O' )
			{
				int moves_req = (abs(next_pos-curr_pos_o)-buffer_b >= 0 ? abs(next_pos-curr_pos_o)-buffer_b : 0) + 1;
				ans += moves_req;
				buffer_b = 0;
				buffer_o += moves_req;
				curr_pos_o = next_pos;
			}
			else
			{
				int moves_req = (abs(next_pos-curr_pos_b)-buffer_o >= 0 ? abs(next_pos-curr_pos_b)-buffer_o : 0) + 1;
				//cout << "moves_req = " << moves_req << endl;
				ans += moves_req;
				buffer_o = 0;
				buffer_b += moves_req;
				curr_pos_b = next_pos;
			}
		}
		cout << "Case #" << cas << ": " << ans << endl;
	}
}
