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

int num[3][3];

int main()
{
	int testN;
	cin>>testN;
	REP(testi,testN) {
		//
		REP(i,3) REP(j,3) num[i][j]=0;
		int n;
		int64 A,B,C,D,x0,y0,M;
		cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
		int64 RX=x0, RY=y0;
		REP(i,n) {
			int kindx=RX%3, kindy=RY%3;
	
			num[kindx][kindy]++;
			RX=(A*RX+B)%M;
			RY=(C*RY+D)%M;
		}
		
//REP(i,3) REP(j,3) cout<<num[i][j]<<" ";
//cout << endl;

		int64 res=0;
		For(i,0,8)
			For(j,0,8)
				For(k,0,8)
					if(i!=j && j!=k && i!=k)
					{
						if((i/3+j/3+k/3)%3 !=0 || (i%3+j%3+k%3)%3!=0) continue;
						res+=num[i/3][i%3]*num[j/3][j%3]*num[k/3][k%3];
					}
		res=res/6;	//cout << res << endl;
		
		For(i,0,8)
		{
			int tmp=num[i/3][i%3];
			if(tmp>=3)
				res+=tmp*(tmp-1)*(tmp-2)/6;
		}
		cout<<"Case #"<<testi+1<<": "<<res<<endl;
	}	
}
