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



int main()
{
	int i,j , k;
	int casos; cin >> casos;
	for( int h = 0 ; h < casos ; h ++ )
	{
		char comb[333][333];
		memset(comb, 0, sizeof(comb));
		int C, D, N;
		cin >> C;
		for( i = 0 ; i < C ; i ++ )
		{
			string s; cin >> s;
			comb[s[0]][s[1]] = comb[s[1]][s[0]] = s[2];
		}
		cin >> D;
		bool hate[333][333];
		memset(hate, false, sizeof(hate));
		for( i = 0 ; i < D ; i ++ )
		{
			string s; cin >> s;
			hate[s[0]][s[1]] = hate[s[1]][s[0]] = true;
		}
		cin >> N;
		char c;
		deque<char> Q;
		int has[333];
		memset(has, 0, sizeof(has));
		for( i = 0 ; i < N ; i ++ )
		{
			cin >> c;
// 			cout << c << endl;
			// tratamos de combinar con la anterior...
			if( Q.size() && comb[c][Q[0]] )
			{
				has[Q[0]]--;
				Q[0] = comb[c][Q[0]];
// 				cout << "HOLANDA  " << Q[0] << endl;
			}else
			{
				bool ok = true;
				for( char a = 'A' ; a <= 'Z' ; a ++ )
					if( hate[a][c] && has[a])
						ok = false;
					
				if( !ok )
				{
					memset(has, 0, sizeof(has));
					Q.clear();
				}else Q.push_front(c), has[c]++;
			}
		}
		reverse(Q.begin(), Q.end());
		cout << "Case #" << h+1 << ": ";
		cout << "[";
		for( i = 0 ; i < Q.size() ; i ++ ) 
		{
			if( i ) cout << ", ";
			cout << Q[i] ;
		}cout << "]" << endl;
	}
	return 0;
}