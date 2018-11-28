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

int MATCH[211];
bool visited[211];
vector<int> edges[211];


int dfs(int node)
{
       if( visited[node] ) return 0;
       visited[node] = true;
       for( int i = 0 ; i < edges[node].size(); i ++ )
       {
	      int neigh = edges[node][i];
	      if( MATCH[neigh] == -1 || dfs(MATCH[neigh]) )
	      {
		     MATCH[neigh] = node;
		     return 1;
	      }
       }
       return 0;
}



bool menor(VI v1, VI v2)
{
       for( int i = 0 ; i < v1.size(); i ++ ) if( v1[i] >= v2[i] ) return false;
       return true;
}


int main()
{
	int i,j ,k;
	      
	int casos; cin >> casos;
	for( int h = 0 ; h < casos; h ++ )
	{
	       int N, K;
	       cin >> N >> K;
	       vector<int> vec[101];
	       for( i = 0 ; i < N; i ++ )
	       {
		      for( j = 0 ; j < K; j ++ )
		      {
			     cin >> k; vec[i].push_back(k);
		      }
	       }
	       sort(vec, vec+N);
	       for( i = 0 ; i < 211; i ++ ) edges[i].clear();
	       for( i = 0 ; i < N; i ++ )
		      for( j = 0; j < N ; j ++ )
			    if( i != j )
			    {
				   if( menor(vec[i] , vec[j] ) )
				   {
					  edges[i].push_back(j+N);
				   }
			    }
			  
	      int res = N;
	      memset(MATCH, -1, sizeof(MATCH));
	      for( i = 0 ; i < N ; i ++ )
	      {
		     memset(visited, false, sizeof(visited));
		     if( dfs(i) ) res--;
	      }
	      cout << "Case #" << (h+1) << ": " << res << endl;
	}return 0;
}
