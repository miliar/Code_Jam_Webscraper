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
#define dforn(a, n) for(int (a) = (n); (a) >= 0; --(a))

#define forsn(a, s, n) for(int (a) = (s); (a) < (n); ++(a))
#define dforsn(a, s, n) for(int (a) = (s); (a) >= (n); --(a))

#define forall(a, b) for(typeof((b).begin()) (a) = (b).begin(); (a) != (b).end(); ++(a))
#define dforall(a, b) for(typeof((b).begin()) (a) = (b).rbegin(); (a) != (b).rend(); ++(a))
#define esta(a, b) (((a) & (1LL<<(b))) != 0)

typedef long long tint;
const int INF = INT_MAX-1000;

char buffer[64];
int dig[10];

int main()
{
#ifdef TAVO92
	freopen("B-large.in" , "r" , stdin);
	freopen("B-large.out", "w" , stdout);
#endif
	
	int T, size;
	
	scanf("%i", &T); cin.getline(buffer, 64);
	
	forn(t, T)
	{
		cin.getline(buffer, 64);
		size = 0;
		while(buffer[size] != '\0') ++size;
		
		memset(dig, 0, sizeof(dig));
		forn(i, size) ++dig[buffer[i]-'0'];
		
		string str, init;
		str = init = buffer;
		
		string ret;
		
		if(next_permutation(str.begin(), str.end()))
		{
			ret = str;
		}
		else
		{
			ret = init;
			sort(ret.begin(), ret.end());
			
			int n0=0;
			
			ret.insert(1, "0");
			
			forn(i, ret.size()) if(ret[i] != '0')
			{
				n0 = i;
				break;
			}
			
			swap(ret[0], ret[n0]);
		}
		
		printf("Case #%i: %s\n", t+1, ret.c_str());
	}
	
	return 0;
}
