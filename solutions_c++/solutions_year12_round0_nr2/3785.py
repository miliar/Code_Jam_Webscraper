#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <algorithm>	// require sort next_permutation count __gcd reverse etc.
#include <cstdlib>	// require abs exit
#include <cstdio>	// require scanf printf
#include <functional>
#include <numeric>	// require accumulate
#include <cmath>
#include <climits>
#include <limits>
#include <cfloat>
#include <iomanip>	// require setw
#include <sstream>	// require stringstream 
#include <cstring>	// require memset
#include <cctype>	// require tolower, toupper
#include <fstream>	// require freopen
#include <ctime>
#define rep(i,n) for(int i=0;i<(n);i++)
#define ALL(A) A.begin(), A.end()

using namespace std;

typedef long long ll;
typedef pair<int, int> P;
typedef pair<P, int> T;

bool is_more_p_or_equal_p (int p, T t )
{
	return (t.first.first >= p || t.first.second >= p || t.second >= p );
}

int main()
{
//	cut here before submit 
//	freopen ("testcase.Dancing_With_the_Googlers", "r", stdin );
	freopen ("B-small-attempt0.in", "r", stdin );
	vector<T> score[31];
	rep (i, 31 ) score[i].clear();

	for (int s = 0; s <= 30; s++ ){
		for (int i = 0; i <= 10; i++ ){
			for (int j = i; j <= 10; j++ ){
				int k = s - i - j;
				if (j - i <= 2 && k - i <= 2 && k >= 0 && k <= 10 && k >= j ){
					score[s].push_back (T (P (i, j ), k ) );
				} // end if
			} // end for
		} // end for
	} // end for
/*
	for (int i = 0; i <= 30; i++ ){
		cout << "score: " << i << ' ';
		rep (j, score[i].size() ){
			cout << '(' << score[i][j].first.first << ',' << score[i][j].first.second << ',';
			cout << score[i][j].second << ')' << ' ';
		} // end rep
 		cout << endl;
	} // end for
*/

	int t;
	cin >> t;
	for (int Case = 1; Case <= t; Case++ ){
		int N, S, p;
		cin >> N >> S >> p;
		vector<int> t (N, 0 );		
		int cnt = 0;
		rep (i, N ){
			cin >> t[i];
			if (t[i] >= 2 && t[i] <= 28 ){
				cnt++;
			} // end if
		} // end rep
		sort (ALL (t ) );
		int res = 0;
		vector<vector<T> > tt (cnt );
		cnt = 0;
		rep (i, N ){
			if (t[i] >= 2 && t[i] <= 28 ){
				tt[cnt++] = score[t[i]];
			}else{
				if (is_more_p_or_equal_p (p, score[t[i]][0] ) ){
					res++;
				} // end if
			} // end rep
		} // end rep
		int ans = 0;
 		for (int i = 0; i < 1<<cnt; i++ ){
			if (__builtin_popcount (i ) == S ){
				int curr = 0;
				for (int j = 0; j < cnt; j++ ){
					if (i&(1<<j ) ){
						if (is_more_p_or_equal_p (p, tt[j][0] ) )
							curr++;
					}else{
						if (is_more_p_or_equal_p (p, tt[j][1] ) )
							curr++;
					} // end if
				} // end for
				ans = max (ans, curr );
			} // end if
		} // end for
		res += ans;
		cout << "Case #" << Case << ": " << res << endl;

	} // end loop
		
	return 0;
}
