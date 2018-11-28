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

template<class T> inline void getInt(T& x)
{
	char c;
	int mul = 1;
	while((c = getchar()) != EOF)
	{
		if(c == '-')mul = -1;
		if(c >= '0' && c <= '9')
		{
			x = c-'0';
			break;
		}
	}
	if(c == EOF){x = EOF;return;}
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

int tcase,N,L,H;
int fre[10010];

int GCD(int a,int b)
{
	return b == 0 ? a : GCD(b,a%b);
}

int main()
{
	getInt(tcase);
	FOR(t,1,tcase)
	{
		cout << "Case #" << t << ": ";
		cin >> N >> L >> H;
		REP(i,N)cin >> fre[i];
		bool xx = false;
		FOR(i,L,H)
		{
			bool ok = true;
			REP(j,N)
			{
				if(i%fre[j] != 0 && fre[j]%i != 0)ok = false;
			}
			if(ok)
			{
				cout << i << endl;
				xx = true;
				break;
			}
		}
		if(!xx)
		cout << "NO" << endl;
		continue;
		int gcd = 1;
		ll t = 1;
		vector<int> s;
		map<int,bool> m;
		m.clear();
		s.clear();
		REP(i,N)
		{
			cin >> fre[i];
			FOR(j,2,10000)
			{
				if(fre[i] == 1)break;
				if(fre[i]%j == 0)
				{
					if(!m[j])
					{
						m[j] = true;
						s.PB(j);
					}
					while(fre[i]%j == 0)fre[i] /= j;
				}
			}
		}
		REP(i,s.size())
		{
			t *= s[i];
			if(t > H)break;
		}
		if(t > H)cout << "NO" << endl;
			else if(t >= L)
			{
				cout << t << endl;
			}
			else
			{
				ll v[s.size()];
				REP(i,s.size())
				{
					v[i] = t*s[i];
				}
				while(1)
				{
					ll m = v[0];
					int idx = 0;
					REP(i,s.size())
					{
						if(v[i] < m)
						{
							m = v[i];
							idx = i;
						}
					}
					if(m >= L)
					{
						cout << m << endl;
						break;
					}
					else if(m > H)
					{
						cout << "NO" << endl;
						break;
					}
					v[idx] *= s[idx];
				}
			}
	}
	return 0;
}
