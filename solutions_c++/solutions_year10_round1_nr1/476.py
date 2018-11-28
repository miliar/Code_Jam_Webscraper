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

int N,K,tcase;
vector<string> v;
string hmm[100];

int f(int x,int y, int dr,int dc,char X)
{
	int ret = 0;
	while(x < N && x >= 0 && y < N && y >= 0 && hmm[x][y] == X)
	{
		ret++;
		x += dr;
		y += dc;
	}
	return ret;
}

int main()
{
	getInt(tcase);
	FOR(T,1,tcase)
	{
		cout << "Case #" << T << ": " ;
		v.clear();
		getInt(N);
		getInt(K);
		string temp;
		REP(i,N)cin >> temp,v.PB(temp);
		REP(i,N)hmm[i] = "";
		REP(k,N)
		{
			int bar = N-k-1;
			int s = N-1;
			int i = N-1;
			while(1)
			{
				if(s < 0)break;
				if(v[bar][s] == '.')
				{
					s--;
					continue;
				}
				hmm[i--] += v[bar][s--];
			}
		}
		REP(i,N)
		{
			while(hmm[i].length() != N)hmm[i] += '.';
		}
		bool wina = false,winb = false;
		REP(i,N)REP(j,N)
		{
			if(hmm[i][j] == 'R' && !wina)
			{
				int m = 0;
				m = MAX(m,f(i,j,1,0,'R'));
				m = MAX(m,f(i,j,0,1,'R'));
				m = MAX(m,f(i,j,1,-1,'R'));
				m = MAX(m,f(i,j,1,1,'R'));
				if(m >= K)
				{
					wina = true;
					continue;
				}
			}
			else if(hmm[i][j] == 'B' && !winb)
			{
				int m = 0;
				m = MAX(m,f(i,j,1,0,'B'));
				m = MAX(m,f(i,j,0,1,'B'));
				m = MAX(m,f(i,j,1,-1,'B'));
				m = MAX(m,f(i,j,1,1,'B'));
				if(m >= K)
				{
					winb = true;
					continue;
				}
			}
		}
		if(wina && winb)cout << "Both" << endl;
			else if(wina) cout << "Red" << endl;
				else if(winb) cout << "Blue" << endl;
					else cout << "Neither" << endl;
	}
	return 0;
}
