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
using namespace std;

#define FORALL(var,x) for (typeof(x.begin()) var=x.begin(); var!=x.end(); var++)
#define FOR(var,lo,hi) for (int var=(lo); var<(hi); var++)
#define SORT(x) sort(x.begin(), x.end())
#define ALL(x) x.begin(), x.end()
#define UNIQUE(x) x.erase(unique(x.begin(),x.end()),x.end()) 

#define mp make_pair
#define pb push_back

typedef long long ll;
typedef vector<int> vi;

char s[1024], ns[1024];

int main(void)	{
	int numTestCases, K;
	scanf("%d", &numTestCases);
	
	for (int nc = 1; nc <= numTestCases; nc++)	{
		scanf("%d", &K);
		scanf("%s", s);
		int len = strlen(s);
		int ans = len;

		vi perm;
		perm.resize(K);
		FOR(i, 0, K)	perm[i] = i;
		do {
			for (int j = 0; j < len; j += K)	{
				for (int i = j; i < j+K; i++)	{
					ns[i] = s[j+perm[i-j]];
				}
			}
			int last = 0, cnt = 0, i = 0;
			while (i < len)	{
				while (i < len && ns[i] == ns[last])	i++;
				last = i;
				cnt++;
			}

			ans = min(ans, cnt);
			
		}while (next_permutation(perm.begin(), perm.end()));
	

		cout << "Case #" << nc << ": " << ans << endl;	
	}
}
