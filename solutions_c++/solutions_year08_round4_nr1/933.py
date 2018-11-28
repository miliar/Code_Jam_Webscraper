#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <ctime>

using namespace std;

typedef long long int64;

#define Fill(a,c) memset(&a, c, sizeof(a))
#define All(v) (v).begin(), (v).end()
#define REP(i,n) for (int i = 0; i < (n); i++)
#define REPD(i,n) for (int i = (n) - 1; i >= 0; i--)
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define FOREACH(it, X) for(__typeof(X.begin()) it = X.begin(); it != X.end(); ++it)

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }
	
#define pi acos(-1.)
#define eps 1e-7
//#define inf 1LL<<32
#define inf 1e17
#define maxn 11000

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;

int gate[maxn];
bool value[maxn];
bool change[maxn];
int M;
int K;

int search(int r, bool v)
{
	
	if(value[r]==v) return 0;
	if(r>=K-1) return -1;
	if(change[r])
		if(((value[2*r+1] && value[2*r+2])==v || (value[2*r+1] || value[2*r+2])==v)) return 1;	

		int r1,r2;
		r1=search(r*2+1,v);
		r2=search(r*2+2,v);
		if(r1<0&&r2<0) return -1;
		
		if(!change[r])
		{
			if((r1<0 || r2<0) && v==gate[r]) return -1;
			if(v==gate[r]) return r1+r2;
		}

		int res;
			if(r1>=0 && r2<0) res=r1;
			else if(r1<0 && r2>=0) res=r2;
			else	res=min(r1,r2);
		return res + (v==gate[r]);		
}
int main()
{
	int testn;
	cin>>testn;
	REP(testi,testn) {
		//
		int v0;
		cin>>M>>v0;
		K=(M+1)/2;
		REP(i,K-1) cin>>gate[i]>>change[i];
		For(i,K-1,M-1) cin>>value[i];
		Ford(i,K-2,0) 
			if(gate[i]==1)
				value[i]=value[2*i+1] && value[2*i+2];
			else
				value[i]=value[2*i+1] || value[2*i+2];
#ifdef DEBUG
		REP(i,M) cout<<value[i]<<" ";
		cout<<endl;
#endif

		int res = search(0,v0);
		cout<<"Case #"<<testi+1<<": ";
		if(res>=0)
			cout<<res<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}
}
