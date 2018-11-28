#include <algorithm> 
#include <bitset> 
#include <cassert>
#include <cmath> 
#include <complex>
#include <cstdio> 
#include <cstdlib> 
#include <cstring>
#include <ctime> 
#include <deque> 
#include <functional> 
#include <iomanip> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <utility> 
#include <vector> 
using namespace std; 

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define max2(x,y) ((x) = max((x),(y)))
#define min2(x,y) ((x) = min((x),(y)))
typedef long long LL;

map<string, int> str2int;
int getint(const string &name)
{
	map<string,int>::iterator it = str2int.find(name);
	if (it == str2int.end()) {
		int sz = SZ(str2int);
		str2int[name] = sz;
		return sz;
	}
	return it->second;
}

int N;
int S, Q;

int cache[1024][128];
int queryEngine[1024];

int getmin(int query, int engine)
{
	if (query == Q)
		return 0;
	int &res = cache[query][engine];
	if (res != -1)
		return res;

	res = 123456789;
	if (queryEngine[query] == engine) {
		for (int i = 0; i < S; ++i) {
			if (i == engine)
				continue;
			min2(res, 1 + getmin(query+1, i));
		}
	} else {
		res = getmin(query+1, engine);
	}

	return res;
}

int main()
{
	char input[1024];
	gets(input);
	sscanf(input, "%d", &N);
	for (int nn = 0; nn < N; ++nn) {
		str2int.clear();

		gets(input);
		sscanf(input, "%d", &S);
		for (int i = 0; i < S; ++i) {
			gets(input);
			getint(input);
		}

		gets(input);
		sscanf(input, "%d", &Q);
		for (int i = 0; i < Q; ++i) {
			gets(input);
			queryEngine[i] = getint(input);
		}

		memset(cache, -1, sizeof cache);

		int mn = 123456789;
		for (int i = 0; i < S; ++i)
			min2(mn, getmin(0, i));

		printf("Case #%d: %d\n", nn+1, mn);
	}
	return 0;
}
