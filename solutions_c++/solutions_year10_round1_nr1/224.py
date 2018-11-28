#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <climits>
#include <ctime>
#include <cassert>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <functional>
#include <iterator>
#include <utility>
#include <algorithm>
#include <numeric>
#include <complex>

using namespace std;

#define ALL(A) A.begin(), A.end()
#define EACH(it,A) for(typeof(A.begin()) t=A.begin();t!=A.end();t++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,a,b) for(i=(a);i<(b);i++)
#define SET(A,p) memset(A,p,sizeof(A))
#define CPY(A,B) memcpy(A,B,sizeof(A))

typedef vector<int> VI;
typedef vector<double> VD;
typedef long long ll;
typedef pair<int,int> ip;
typedef pair<ll,ll> llp;
#define probT ip
typedef vector<probT> VP;

#define sz size()
#define cl clear()
#define fi first
#define se second
#define pb push_back
#define ins insert

char A[64][64];

int main()
{
	int T;
	cin >> T;
	FOR(te,0,T)
	{
		int N,K;
		cin >> N >> K;
		FOR(i,0,N) cin >> A[i];
		FOR(i,0,N) for(int j=N-1,t=N-1;j>=0;j--)
			if(A[i][j] != '.') swap(A[i][j],A[i][t--]);
		int re=0, bl=0;
		FOR(i,0,N) if(!re) FOR(j,0,N)
		{
			int f;
			if(j<=N-K) { f=1; FOR(k,0,K) if(A[i][j+k]!='R') { f=0; break;} }
			if(f) { re=1; break;}
			if(i<=N-K) { f=1; FOR(k,0,K) if(A[i+k][j]!='R') { f=0; break;} }
			if(f) { re=1; break;}
			if(i<=N-K && j<=N-K) { f=1; FOR(k,0,K) if(A[i+k][j+k]!='R') { f=0; break;} }
			if(f) { re=1; break;}
			if(i>=K-1 && j<=N-K) { f=1; FOR(k,0,K) if(A[i-k][j+k]!='R') { f=0; break;} }
			if(f) { re=1; break;}
		}
		FOR(i,0,N) if(!bl) FOR(j,0,N)
		{
			int f;
			if(j<=N-K) { f=1; FOR(k,0,K) if(A[i][j+k]!='B') { f=0; break;} }
			if(f) { bl=1; break;}
			if(i<=N-K) { f=1; FOR(k,0,K) if(A[i+k][j]!='B') { f=0; break;} }
			if(f) { bl=1; break;}
			if(i<=N-K && j<=N-K) { f=1; FOR(k,0,K) if(A[i+k][j+k]!='B') { f=0; break;} }
			if(f) { bl=1; break;}
			if(i>=K-1 && j<=N-K) { f=1; FOR(k,0,K) if(A[i-k][j+k]!='B') { f=0; break;} }
			if(f) { bl=1; break;}
		}
		cout << "Case #" << te+1 << ": " << (re?(bl?"Both":"Red"):(bl?"Blue":"Neither")) << endl;
	}
	return 0;
}
