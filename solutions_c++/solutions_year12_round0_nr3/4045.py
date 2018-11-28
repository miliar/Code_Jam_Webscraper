#include <iostream>
#include <string>
#include <vector>
#include <cstring>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#include <numeric>
#include <cmath>
#include <sstream>
#include <stack>
#include <queue>
using namespace std;

typedef pair<int,int> pii;
typedef pair<int,string> pis;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef vector<string> vs;
typedef set<int> si;
typedef map<int,int> mii;
typedef map<int,string> mis;
typedef map<string,int> msi;
typedef long long ll;
typedef unsigned long long ull;
#define foreach(var, container) for(typeof((container).begin()) var = (container).begin(); var != (container).end(); ++var)
#define FOR(v, t) for(int v=0; v<int(t); ++v) 
#define RNG(v, f, t) for(int v=int(f); v<=int(t); ++v)
#define MIN(x,y) std::min(x,y)
#define MAX(x,y) std::max(x,y)

int find(int A, int B)
{
	int cnt=0;
	si uq;
	RNG(i, A, B)
	{
		int ld=log10(i)+1e-9, lp=ld, dec=1, jd=10;
		FOR(j, ld) dec*=10;
		FOR(j, ld)
		{
			int c = i/dec + (i%dec)*jd;
			if (c>i && A<=c && c<=B && !uq.count(c)) uq.insert(c);
			jd*=10;
			dec/=10;
		}
		cnt+=uq.size();
		uq.clear();
	}
	return cnt;
}
int main()
{
	int T;cin>>T;
	FOR(t,T)
	{
		int A,B;cin>>A>>B;
		cout<<"Case #"<<t+1<<": "<<find(A,B)<<endl;
	}
	return 0;
}
