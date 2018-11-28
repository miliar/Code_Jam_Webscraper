#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <complex>
#include <numeric>
#include <vector>
#include <string>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define sz(a) int((a).size())
#define FOR(i, a, b) for(int i=(a), _b=(b); i<_b; ++i)
#define REP(i, n) FOR(i, 0, n)
#define FORD(i, a, b) for(int i=(a), _b=(b); i>=_b; --i)
#define CL(a, v) memset(a, v, sizeof a)
#define INF 1000000000
#define INF_LL 1000000000000000000LL
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

const int h = 111;

int n;
char o[h];
int p[h];

void move (int &p, int dest)
{
	if(p==dest) return;
	if(dest<p) --p;
	else ++p;
}

int main()
{
	freopen("a-large.in", "r", stdin); //-small-attempt
	freopen("a-large.out", "w", stdout); //-large
	int T, it=1;
for(scanf("%d", &T); it<=T; ++it)
{
	scanf("%d", &n);
	REP(i, n)
	{
		char c=0;
		do{ scanf("%c", &c); } while(!isalpha(c));
		o[i] = c;
		scanf("%d", p+i);
	}
	int po = 1, pb = 1;
	int s = 0;
	REP(i, n)
	{
		int j=i;
		while(j<n && o[i]==o[j]) ++j;
		if(o[i]=='B')
		{
			while(pb != p[i])
			{
				move(pb, p[i]);
				if(j<n) move(po, p[j]);
				++s;
			}
			if(j<n) move(po, p[j]);
			++s;
		}
		else
		{
			while(po != p[i])
			{
				move(po, p[i]);
				if(j<n) move(pb, p[j]);
				++s;
			}
			if(j<n) move(pb, p[j]);
			++s;
		}
	}
	printf("Case #%d: %d\n", it, s);
}
	return 0;
}
