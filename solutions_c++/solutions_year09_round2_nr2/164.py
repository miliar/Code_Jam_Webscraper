
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


int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d\n", &T);
	char buf[1 << 10];
	REP(I, T)
	{
		gets(buf);
		if(next_permutation(buf, buf + strlen(buf)))
			printf("Case #%d: %s\n", I + 1, buf);
		else
		{
			int len = strlen(buf);
			string str = "";
			REP(i, len)
				if(buf[i] != '0')
					str += buf[i];
			int cnt = strlen(buf) - str.length() + 1;
			sort(ALL(str));
			printf("Case #%d: ", I + 1);
			printf("%c", str[0]);
			REP(i, cnt)
				printf("0");
			printf("%s\n", str.c_str() + 1);
		}
	}
	return 0;
}