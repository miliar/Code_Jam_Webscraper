// Daniel Grunwald

#include <iostream>
#include <string>
#include <map>

using namespace std;

#ifdef TEST
#define dout(X) cerr << X << endl
#else
#define dout(X) 
#endif

const int MAXINT = 0x7fffffff;



int dp[101];
int S, Q;

int dp_minimum() {
	int minimum = MAXINT;
	for (int j = 1; j <= S; j++) {
		minimum = min(minimum, dp[j]);
	}
	return minimum;
}

int main()
{
	int N;
	cin >> N;
	for (int test = 1; test <= N; test++) {
		map<string, int> se_map;
		cin >> S;
		string s;
		getline(cin, s); // get rest of line
		for (int i = 1; i <= S; i++) {
			getline(cin, s);
			dout(s << " = " << i);
			se_map[s] = i;
		}
		cin >> Q;
		getline(cin, s); // get rest of line

		memset(dp, 0, sizeof(dp)); // reset dp array
		for (int i = 0; i < Q; i++) {
			getline(cin, s);
			int query = se_map[s];
			dout(i << " : " << s << " (" << query << ")");
			if (query > 0) {
				int switchCost = dp_minimum() + 1;
				for (int j = 1; j <= S; j++) {
					dp[j] = min(dp[j], switchCost); 
				}
				dp[query] = MAXINT; // don't let the universe implode
#ifdef TEST
				for (int j = 1; j <= S; j++) {
					cerr << dp[j] << " ";
				}
				cerr << endl;
#endif
			}
		}
		cout << "Case #" << test << ": " << dp_minimum() << endl;
	}
	return 0;
}