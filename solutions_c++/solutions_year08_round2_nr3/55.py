#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cassert>
#include <climits>
#include <iostream>
#include <iomanip>
#include <vector>
#include <deque>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <list>
#include <algorithm>

using namespace std;

#define FORI(N) for (int i = 0; i < (N); i++)
#define FOREI(N) for (int i = 1; i <= (N); i++)
#define FORJ(N) for (int j = 0; j < (N); j++)
#define FOREJ(N) for (int j = 1; j <= (N); j++)
#define FORK(N) for (int k = 0; k < (N); k++)
#define FOREK(N) for (int k = 1; k <= (N); k++)
#define ALL(A) A.begin(), A.end()
#define EACH(A,T) for (typeof(A.begin()) T = A.begin(); T != A.end(); T++)
#define REP(N) while (N--)

#define sz size()
#define pb(N) push_back(N)
#define CLEAR(M,O) memset (M, C, sizeof(M))

int main()
{
	int T;
	cin >> T;
	for (int cc = 1; cc <= T; cc++)
	{
		int K;
		cin >> K;
		int q;
		cin >> q;
		cout << "Case #" << cc << ":";
		FORI(q)
		{
			int N;
			cin >> N;
   			int c = 1;
   			int n = N, m = K, k = 1;
   			while (1)
   			{
				assert (n <= m);
                int p = k%m;
				if (p == 0) p = m;
				if (n == p) break;
				p++;
				if (p > m) p = 1;
				if (n >= p)
				{
					c++;
					int aa = n-p+1, bb = m-1, cc = k+1;
					n = aa;
					m = bb;
					k = cc;
				}
				else
				{
                    c++;
					int aa = m-p+1 + n, bb = m-1, cc = k+1;
					n = aa;
					m = bb;
					k = cc;
				}
			}
			cout << " " << c;
		}
		cout << endl;
	}
	return 0;
}
