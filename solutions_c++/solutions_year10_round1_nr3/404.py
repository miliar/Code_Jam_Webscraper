#include <iostream>
#include <cstdio>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <cmath>
#include <cstdlib>

//Hendri's Template
#define REP(i, n) for(int i = 0, _n = (n); i < _n; i++)
#define FOR(i, a, b) for(int i = (a), _b = (b); i <= _b; i++)
#define FORD(i, a, b) for(int i = (a), _b = (b); i >= _b; i--)
#define RESET(A,v) memset(A, v, sizeof(A))

#define MP make_pair
#define PB push_back
#define F first
#define S second

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

template<class T> inline T MIN(T a, T b){return a < b?a:b;}
template<class T> inline T MAX(T a, T b){return a > b?a:b;}

inline void getInt(int& x)
{
	char c;
	int mul = 1;
	while(c = getchar())
	{
		if(c == '-')mul = -1;
		if(c >= '0' && c <= '9')
		{
			x = c-'0';
			break;
		}
	}
	while(c = getchar())
	{
		if(c >= '0' && c <= '9')
		{
			x = (x<<1)+(x<<3)+(c-'0');
		}
		else break;
	}
	x *= mul;
}
//End of Hendri's Template

int A1,A2,B1,B2,tcase;

bool win(int a,int b)
{
	if(a < b){int temp = a;a = b;b = temp;}
	if(b == 0 || a == b)return false;
	if(a/b > 1)return true;
	return !win(b,a%b);
	//return __builtin_popcount(ret)%2 == 0 ? true:false;
}

int main()
{
	getInt(tcase);
	FOR(T,1,tcase)
	{
		cout << "Case #" << T << ": " ;
		getInt(A1);
		getInt(A2);
		getInt(B1);
		getInt(B2);
		int ret = 0;
		FOR(i,A1,A2)FOR(j,B1,B2)
		{
			if(win(MAX(i,j),MIN(i,j)))
			{
				ret++;
			}
		}
		cout << ret << endl;
	}
	return 0;
}
