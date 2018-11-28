
#define _CRT_SECURE_NO_DEPRECATE 

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

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)

#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ABS(A) ((A) < 0 ? (-(A)) : (A))
#define ALL(V) V.begin(), V.end()
#define SIZE(V) (int)V.size()
#define pb push_back
#define mp make_pair
#define EPS 1e-7
#define Pi 3.14159265358979

typedef long long Long;
typedef unsigned long long ULong;
typedef unsigned int Uint;
typedef unsigned char Uchar;
typedef vector <int> VI;
typedef pair <int, int> PI;

int tests;

char C[26][26];

bool O[26][26];

char buf[1 << 10];

vector<char> res;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &tests);
	int I = 0;
	while(tests--)
	{
		memset(C, 0, sizeof(C));
		int c;
		scanf("%d", &c);
		REP(i, c)
		{
			scanf("%s", buf);
			char c1 = buf[0];
			char c2 = buf[1];
			char c3 = buf[2];
			C[c1 - 'A'][c2 - 'A'] = c3;
			C[c2 - 'A'][c1 - 'A'] = c3;
		}
		memset(O, 0, sizeof(O));
		int o;
		scanf("%d", &o);
		REP(i, o)
		{
			scanf("%s", buf);
			O[buf[0] - 'A'][buf[1] - 'A'] = true;
			O[buf[1] - 'A'][buf[0] - 'A'] = true;
		}
		int n;
		scanf("%d", &n);
		scanf("%s", buf);
		if((int)strlen(buf) != n)
			throw -1;
		res.clear();
		REP(i, n)
		{
			char ch = buf[i];
			int len = (int)res.size();
			if(!len)
			{
				res.pb(ch);
				continue;
			}
			if(C[res.back() - 'A'][ch - 'A'])
			{
				ch = C[res.back() - 'A'][ch - 'A'];
				res.pop_back();
				res.pb(ch);
				continue;
			}
			REP(j, len)
				if(O[res[j] - 'A'][ch - 'A'])
				{
					res.clear();
					break;
				}
			if(!res.empty())
				res.pb(ch);
		}
		printf("Case #%d: [", ++I);
		REP(i, (int)res.size())
		{
			if(i)
				printf(", ");
			printf("%c", res[i]);
		}
		puts("]");

	}
	return 0;
}