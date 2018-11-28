#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
using namespace std;

#define ALL(ar)       (ar).begin(),(ar).end()
#define SZ(a)         int((a).size())
#define MP(a,b)       make_pair(a,b)
#define INF           0x7f7f7f7f
typedef long long     LL;
typedef vector<int>   VI;
typedef pair<int,int> II;

int T, N;

int main()
{
	freopen("in.in", "rt", stdin);
	freopen("out.out", "wt+", stdout);

	cin >> T;
	for (int tc = 0; tc < T; tc++)
	{
		string s, s2;
		cin >> s; s2 = s;
		int z = 0;
		if (!next_permutation (ALL(s))) {
			if (s[0] != '0') s.insert (s.begin()+1, '0');
			else {
				for (int i = 0; i < SZ(s); i++)
					if (s[i] != '0') {
						swap (s[0], s[i]);
						break;
					}
				s.insert (s.begin()+1, '0');
			}
		}
		printf ("Case #%d: ", tc+1);
		cout << s << endl;
	}	
	
	return 0;
}