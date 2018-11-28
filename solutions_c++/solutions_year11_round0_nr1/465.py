
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

const int SZ = 1 << 7;

int tests;

int n;

char ch[SZ];
int pos[SZ];

int cur;

int new_cur;

void move(int &x, char C)
{
	if(pos[cur] == x && ch[cur] == C)
	{
		++new_cur;
		return;
	}
	int to = x;
	FOR(i, cur, n)
		if(ch[i] == C)
		{
			to = pos[i];
			break;
		}
	if(to > x)
		++x;
	else if(to < x)
		--x;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &tests);
	int I = 0;
	while(tests--)
	{
		scanf("%d", &n);
		REP(i, n)
			scanf("%s%d", ch + i, &pos[i]);
		int po = 1, pb = 1;
		cur = 0;
		int res = 0;
		while(cur < n)
		{
			new_cur = cur;
			move(po, 'O');
			move(pb, 'B');
			cur = new_cur;
			++res;
		}
		printf("Case #%d: %d\n", ++I, res);
	}
	return 0;
}