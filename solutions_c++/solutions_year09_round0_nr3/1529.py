#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <queue>
#include <climits>
#include <string>
#include <cstring>
using namespace std;

#define forn(a, n) for(int (a) = 0; (a) < (n); ++(a))
#define forsn(a, s, n) for(int (a) = (s); (a) < (n); ++(a))
#define forall(a, b) for(typeof((b).begin()) (a) = (b).begin(); (a) != (b).end(); ++(a))
#define esta(a, b) (((a) & (1LL<<(b))) != 0)

typedef long long tint;
const int INF = INT_MAX-1000;

int n, dp[600][30];
char buffer[600];
string word = "welcome to code jam-";

int main()
{
#ifdef TAVO92
	freopen("C-large.in" , "r" , stdin);
	freopen("C-large.out", "w" , stdout);
#endif
	
	cin >> n;
	cin.getline(buffer, 540);
	
	int ret, size;
	string str;
	
	forn(t, n)
	{
		cin.getline(buffer, 540);
		memset(dp, 0, sizeof(dp));
		
		size = 0;
		forn(i, INF)
		{
			++size;
			if(buffer[i] == '\0') break;
		}
		
		dp[0][0] = 1;
		
		forn(i, size) forn(j, word.size())
		{
			if(buffer[i] == word[j])
				{dp[i+1][j+1] += dp[i][j]; dp[i+1][j+1] %= 10000;}
			
			dp[i+1][j] += dp[i][j];
			dp[i+1][j] %= 10000;
		}
		
		ret = dp[size][word.size()-1];
		
		stringstream strm; strm << ret; strm >> str;
		
		while(str.size() < 4)
			str = "0"+str;
			
		printf("Case #%i: %s\n", t+1, str.c_str());
	}
	
	return 0;
}
