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

int tcase,P,ret;
int M[(1<<11)];
int tree[(1<<11)*4];
int arr[(1<<11)*4];

void build(int s,int e, int index)
{
	if(s == e)
	{
		tree[index] = M[s];
		//cout << s << " " << e << " " << tree[index] << endl;
		return;
	}
	build(s,(s+e)/2,2*index+1);
	build((s+e)/2+1,e,2*index+2);
	tree[index] = MIN(tree[2*index+1],tree[2*index+2]);
	//cout << s << " " << e << " " << tree[index] << endl;
}

int query(int s,int e,int a,int b,int index)
{
	if(a > e || b < s)return 10000;
	if(a >= s && b <= e)return tree[index];
	arr[2*index+1] += arr[index];
	arr[2*index+2] += arr[index];
	tree[2*index+1] -= arr[index];
	tree[2*index+2] -= arr[index];
	arr[index] = 0;
	int pertamax = query(s, e, a, (a+b)/2, 2*index+1);
	int keduax = query(s, e, (a+b)/2+1, b, 2*index+2);
	return MIN(pertamax,keduax);
}

void update(int s,int e,int a,int b,int index)
{
	if(a > e || b < s)return;
	if(a >= s && b <= e)
	{
		tree[index]--;
		arr[index]++;
		return;
	}
	update(s,e,a,(a+b)/2,2*index+1);
	update(s,e,(a+b)/2+1,b,2*index+2);
	tree[index] = MIN(tree[2*index+1],tree[2*index+2]);
}

void doit(int s,int e)
{
	if(s >= e)return;
	int q = query(s,e,0,(1<<P)-1,0);
	//cout << s << " " << e << " " << q << endl;
	if(q > 0)
	{
		update(s,e,0,(1<<P)-1,0);
	}
	else
	{
		ret++;
	}
	doit(s,(s+e)/2);
	doit((s+e)/2+1,e);
}

int main()
{
	getInt(tcase);
	FOR(t,1,tcase)
	{
		RESET(arr,0);
		RESET(tree,0);
		ret = 0;
		cout << "Case #" << t << ": ";
		getInt(P);
		//cout << P << endl;
		REP(i,(1<<P))
		{
			getInt(M[i]);
		}
		int temp;
		REP(i,P)
		{
			REP(j,(1<<(P-i-1)))cin >> temp;
		}
		build(0,(1<<P)-1,0);
		REP(i,P)
		{
			int L = (1<<(i+1));
			for(int j = 0; j+L-1 < (1<<P); j+= L)
			{
				int q = query(j,j+L-1,0,(1<<P)-1,0);
				if(q <= 0)
				{
					ret++;
				}
				else
				{
					update(j,j+L-1,0,(1<<P)-1,0);
				}
			}
		}
		cout << ret << endl;
	}
	return 0;
}
