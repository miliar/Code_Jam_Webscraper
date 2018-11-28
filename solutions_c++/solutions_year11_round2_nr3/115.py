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

vector<int> edges[2222];
vector<pair<int,int>  > edges2;
vector<int> nodes[2222];
int N, M;
vector<vector<int> > rooms;
void doit(vector<int> vec)
{
//	cout << " HOlanda " << endl;
//	for( int p = 0 ; p < vec.size() ; p ++ ) cout << vec[p] << " "  ; cout << endl;

	int seen[2222];
	memset(seen, -1, sizeof(seen));
	int i,j ,k;
	for( i = 0 ; i < vec.size() ; i ++ ) seen[vec[i]] = i;
	// tratamos de dividir...
	for( i = 0 ; i < edges2.size() ; i ++ )
	{
		int a, b;
		a = edges2[i].first, b = edges2[i].second;
		if( seen[a] < 0 or seen[b] < 0 ) continue;
		if( seen[a] + 1 == seen[b] ) continue;
		if( seen[a] == 0  && seen[b]+1 == vec.size() ) continue;
		vector<int> vec1, vec2;
		for( i = 0 ; vec[i] <= a ; i ++ ) vec1.PB(vec[i]);
		i--;
		for( ; i < vec.size() && vec[i] <= b ; i ++ ) vec2.PB(vec[i]);
//		cout << i << "  " << vec.size() << endl;
		i--;
		for( ; i < vec.size() ; i ++ ) vec1.PB(vec[i]);
//		cout << a << "  " << b << endl;
//		for( j = 0 ; j < vec1.size() ; j ++ ) cout << vec1[j] << " " ; cout << endl;
//		for( j = 0 ; j < vec2.size() ; j ++ ) cout << vec2[j] << " " ; cout << endl;
//		return ;
		doit(vec1), doit(vec2);
		return;
	}
	// aca encontro una comp conexa...
	for( i = 0 ; i < vec.size() ; i ++ ) nodes[vec[i]].PB(rooms.size());
	rooms.PB(vec);
//	for( int p = 0 ; p < vec.size() ; p ++ ) cout << vec[p] << " "  ; cout << endl;
}

bool dp[1<<8][10];
int color[10];
int col[10];
int best;
void doit2(int mask, int cant)
{
	if( cant > best )
	{
		best = cant;
		for( int i = 0 ; i < N ; i ++ ) color[i] = col[i];
	}
	if( dp[mask][cant] ) return;
	dp[mask][cant] = true;
	int i,j ,k;
	for( int m = 1 ; m < (1<<N) ; m ++ )
	{
		if( m & mask ) continue;
		// tiene todas las rooms?
		set<int> R;
		for( j = 0 ; j < N ; j ++ )
		{
			if(!((1<<j)&m))continue;
			for( k = 0 ; k < nodes[j].size() ; k ++ ) R.insert(nodes[j][k]);
		}
		if( R.size() == rooms.size() )
		{
			for( j = 0 ; j < N ; j ++ )
			{
				if(!((1<<j)&m))continue;
				col[j] = cant;
			}
			doit2(mask|m, cant+1);
			for( j = 0 ; j < N ; j ++ )
			{
				if(!((1<<j)&m))continue;
				col[j] = 0;
			}
		}
	}
}



int main()
{
	int i,j ,k;
	int casos; cin >> casos;
	for( int h = 0 ; h < casos ;h ++ )
	{
		cin >> N >> M;
		vector<int> vec;
		rooms.clear();
		for( i = 0 ; i < N ; i ++ ) nodes[i].clear();
		for( i = 0 ; i < N ;i ++ ) edges[i].clear();
		edges2.clear();

		for(i = 0 ; i < M ; i ++ )
		{
			cin >> k;
			k--;
			vec.PB(k);
		}
		for( i = 0 ; i < M ; i ++ )
		{
			cin >> k; k--;
			if( vec[i] < k )
			edges2.PB(MP(vec[i], k));
			else edges2.PB(MP(k,vec[i]));
			edges[k].PB(vec[i]);
			edges[vec[i]].PB(k);
		}
		vec.clear();
		for( i = 0 ; i < N ; i ++ )
		{
			vec.PB(i);
		}
//				cout << " HOLANDA  " << endl;
		doit(vec);
//				cout << " HOLANDA  " << endl;
		best = 1;
		memset(color, 0, sizeof(color));
		memset(dp, false, sizeof(dp));
		doit2(0,0);
		cout << "Case #" << h+1 << ": " << best << endl;;
		for( i = 0 ; i < N ; i ++ )
		{
			if( i ) cout << " ";
			cout << color[i]+1 ;
		}cout << endl;
	}return 0;
}

