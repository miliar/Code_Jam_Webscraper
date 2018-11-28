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
const int COTA = 10000000;

int dp[COTA+10][10];
char buffer[32];

int calc(int n, int base)
{
	if(n == 1) return 1;
	if(n>COTA) return 0;
	
	int& ret = dp[n][base];
	
	if(ret != -1) return ret;
	
	ret = 0;
	int sum = 0;
	
	while(n>=base)
	{
		sum += (n%base)*(n%base);
		n /= base;
	}
	
	sum += n*n;
	
	ret = calc(sum, base);
	return ret;
}

int main()
{
#ifdef TAVO92
	freopen("A-small.in" , "r" , stdin);
	freopen("A-small.out", "w" , stdout);
#endif
	
	memset(dp, -1, sizeof(dp));
	
	int t;
	scanf("%i", &t);
	cin.getline(buffer, 32);
	
	forn(p, t)
	{
		cin.getline(buffer, 32);
		stringstream strm; strm << buffer;
		
		vector<int> candi;
		
		while(!strm.eof())
		{
			int tmp;
			strm >> tmp;
			candi.push_back(tmp);
		}
		
		forsn(i, 2, INF)
		{
			bool q = true;
			forn(j, candi.size())
				q &= calc(i, candi[j]);
			
			if(q)
				{printf("Case #%i: %i\n", p+1, i); break;}
		}
	}
	
	return 0;
}
