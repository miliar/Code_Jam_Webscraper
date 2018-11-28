#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i, n) for(int i=0;i<int(n);i++)
#define FOR(i, a, b) for(int i=(a);i<int(b);i++)
#define RFOR(i, b, a) for(int i=(b);i>int(a);i--)
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define ALL(x)   (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define ISS istringstream
#define OSS ostringstream
#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
#define MP(X,Y) make_pair(X,Y)

#define ll long long
const double pi=acos(-1.0);
const double eps=1e-11;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}

int N; 
int dp[111][111][111];
pair<char,int> arr[111];
#define INF 1001000


int nextO[111], nextB[111];
void move(int &pos, int nextPos)
{
	if( pos < nextPos ) pos++;
	else if( pos > nextPos ) pos--;
}
void press(){}

int main()
{
	int i,j ,k;
	int casos;
	cin >> casos;
	for( int h = 0 ; h < casos ; h ++ )
	{
		cin >> N;
		for( i = 0 ; i < N ; i  ++ ) cin >> arr[i].first >> arr[i].second;
		nextB[N] = nextO[N] = 1;
		for( i = N-1 ; i >= 0 ; i -- )
		{
			nextO[i] = nextO[i+1];
			nextB[i] = nextB[i+1];
			if( arr[i].first == 'O' ) nextO[i] = arr[i].second;
			else nextB[i] = arr[i].second;
		}
		deque<int> O, B;
		int lastO = 1, lastB = 1;
		int res = 0;
		for( i = 0 ; i < N ; i ++ )
		{
			if( arr[i].first == 'O' )
			{
				while( arr[i].second != lastO )
				{
					res++;
					move(lastO, nextO[i]);
					move(lastB, nextB[i]);
				}
				res++;
				press();
				move(lastB, nextB[i]);
			}else
			{
				while( arr[i].second != lastB )
				{
					res++;
					move(lastO, nextO[i]);
					move(lastB, nextB[i]);
				}
				res++;
				press();
				move(lastO, nextO[i]);
			}
		}
		cout << "Case #" << h+1 << ": " << res << endl;
	}return 0;
}