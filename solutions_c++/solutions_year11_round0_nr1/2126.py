#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
using namespace std;
 
typedef vector < int > vi;
typedef vector < string > vs;
typedef vector < bool > vb;
#define FOR(i,q,w) for (int i=q;i<w; i++)
#define PB push_back
#define MP make_pair
const int MOD = 1000000007;
const int INF = 2000000000;
typedef long long ll;

int n,m,t;
pair<int,int> A[1000];

int main()
{
		cin >> t;

		FOR (tt,0,t)
		{
				cin >> n;
				FOR (i,0,n)
				{
						int u;
						char c;
						cin >> c >> u;
						u--;
						A[i] = MP(u,(c=='O'));
				}
				
				int x = 0, y = 0, last = 0, res = 0, i =- 0;

				while (i<n)
				{
						int j = 1, r = 0;
						
						if (A[i].second)
						{
								int t = abs(x-A[i].first);
								r += t+1;
								r -= last;
								if (r < 1) r = 1;
								x = A[i].first;
						}
						else
						{
								int t = abs(y-A[i].first);
								r += t+1;
								r -= last;
								if (r < 1) r = 1;
								y = A[i].first;
						}
						

						while (i+j < n && A[i+j].second == A[i].second)
						{
								if (A[i].second)
								{
										r += abs(x-A[i+j].first)+1;
										x = A[i+j].first;

								}
								else
								{
										r += abs(y-A[i+j].first)+1;
										y = A[i+j].first;
								}
								j++;
						}
						
						res += r;
						last = r;
						i += j;

				}
				cout << "Case #" << tt+1 << ": " << res << endl;
		}

		return 0;
} 
 