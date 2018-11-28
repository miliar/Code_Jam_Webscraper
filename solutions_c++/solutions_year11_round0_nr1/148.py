#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define eps 1e-9
#define FOR(x, s, e) for(int x = (s); x < (e); ++x)
#define FORc(x, s, e, c) for(int x = (s); x < (e) && (c); ++x)
#define STEP(x, s, e, d) for(int x = (s); x < (e); x+=(d))
#define ROF(x, s, e) for(int x = (s); x >= (e); --x)
#define ROFc(x, s, e, c) for(int x = (s); x >= (e) && (c); --x)
#define vb vector<bool>
#define vi vector<int>
#define vii vector<pair<int, int> >
#define LL long long
#define pii pair<int, int>
#define vs vector<string>
#define pb push_back
#define mp make_pair
#define ALL(X) X.begin(), X.end()
#define countbit(X) __builtin_popcount(X)
#define gcd(x, y) __gcd(x, y)
#define x first
#define y second

using namespace std;

int main(int argc, char **argv){
	int T;
	cin >> T;
	FOR(Ca, 1, T+1){
		printf("Case #%d: ", Ca);
		int N;
		cin >> N;
		vii col(N);
		deque<int> A, B;
		FOR(i, 0, N){
			int y;
			string s;
			cin >> s >> y;
			col[i] = mp((int)(s[0] == 'B'), y);
			if (s[0] == 'O') A.pb(y);
			else B.pb(y);
		}
		int pa = 1, pb = 1, ptr = 0;
		int res = 0;
		while (ptr < N){
			bool pushed = 0;
			if (A.size()){
				if (pa < A.front()) pa++;
				else if (pa > A.front()) pa--;
				else if (!col[ptr].x)
					if (pa == col[ptr].y) ptr++, A.pop_front(), pushed = 1;
			}
			if (B.size()){
				if (pb < B.front()) pb++;
				else if (pb > B.front()) pb--;
				else if (col[ptr].x)
					if (pb == col[ptr].y & !pushed) ptr++, B.pop_front();
			}
			//printf("%d: %d %d\n", res, pa, pb);
			res++;
		}
		cout << res << endl;
	}
	return 0;
}
