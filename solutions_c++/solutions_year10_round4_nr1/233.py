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
#define INF 100000000
int res = INF ;
int aux[200][200];

int tratar(int si, int first)
{
	int r = 0;
//	REP(i, si){ REP(j, si) printf("%i  ", aux[i][j]); printf("\n");}
	REP(i, si) REP(j, si)
	{
		// probamos las verticales....
		set<int> S;
		int non = 0;

		if( aux[i][j] == -1 ) non++;
		else S.insert(aux[i][j]);
		
		
		int opi = si - j - 1;
		int opj = si - i - 1;
		
		if( aux[opi][opj] == -1 ) non++;
		else S.insert(aux[opi][opj]);
		
		swap(opi, opj);
		if( aux[opi][opj] == -1 ) non++;
		else S.insert(aux[opi][opj]);
			
		opi = j, opj = i;
		
		if( aux[opi][opj] == -1 ) non++;
		else S.insert(aux[opi][opj]);
		
//		printf("%i\n", S.size());
		if( S.size() > 1 ) return INF;
		if( aux[i][j] == -1 ) r++;
	}
	
//	printf("%i %i\n", si, first);
	return (si * si) - (first * first);
}



int main()
{
	int i,j ,k;
	
	int casos; cin >> casos;
	for( int h = 0 ; h < casos; h ++ )
	{
		int N;
		cin >> N;
		res = INF;
		int mat[N][N];
		for( int r = 0 ; r < N ; r ++ )
		{
			int rr = r;
			for( int c = 0; rr >= 0  ; c ++ )
			{
				
				cin >> mat[rr][c];
				rr--;
			}
		}
		for( int c = 1; c < N; c ++ )
		{
			int cc = c;
			for( int r = N-1; cc < N ; r -- , cc++)
				cin >> mat[r][cc];
		}
//		REP(i, N) { REP(j, N) printf("%i   ", mat[i][j]); printf("\n");}
		int first = N;
		for( int si = N  ; si <= 3 * N  ; si ++ )
		{
			for( int r = 0; r <= si-N; r ++ )
			{
				
				REP(j, si) REP(k, si) aux[j][k] = -1;
				for( int rr = r; rr < r+N; rr ++ )
				{
					for( int cc = 0; cc < N ; cc ++ )
					{
						if( res < INF -10 ) break;
						aux[rr][cc] = mat[rr-r][cc];
				
					}
				}
				res = min ( res, tratar(si, first) );			
				REP(j, si) REP(k, si) aux[j][k] = -1;
				for( int rr = r; rr < r+N; rr ++ )
					for( int cc = si-N; cc < si ; cc ++ )
					{
				
						aux[rr][cc] = mat[rr-r][cc-(si-N)];
						
					}
						if( res < INF -10 ) break;
				res = min ( res, tratar(si, first) );
			}
			for( int c = 0; c <= si-N; c ++ )
			{
				
				REP(j, si) REP(k, si) aux[j][k] = -1;
				for( int cc = c; cc < c + N ; cc ++ )
					for( int r = 0; r < N; r ++ )
					{

						aux[r][cc] = mat[r][cc-c];
					
					}
					if( res < INF -10 ) break;
				res = min ( res, tratar(si, first) );
				REP(j, si) REP(k, si) aux[j][k] = -1;
				for( int cc = c; cc < c + N ; cc ++ )
					for( int r = si-N; r < si; r ++ )
					{
	
						aux[r][cc] = mat[r-(si-N)][cc-c];
			
						
					}
				if( res < INF -10 ) break;
				res = min ( res, tratar(si, first) );
			}
		
			
			if( res < INF -10 ) break;
		}


		cout << "Case #" << (h+1) << ": " << res << endl;
	}return 0;
}











