#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdlib>

using namespace std;

#define sz(v) ((int)(v).size())
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<string> vs;

template<class T>T abs(T x) { return (x>0) ? x : -x; }
template<class T>T sqr(T x) { return x*x;            }

void writeCaseNumber(int num) { printf("Case #%d: ",num); }

const int inf=1000*1000;
const int max_n=30000+218;

int n,v;
int g[max_n],c[max_n];
int ans[max_n][2];

int solve(int v, int val) {
	int &res=ans[v][val];
	if (res!=-1) return res;
	if (v>=(n-1)/2) {
		if (val==c[v]) res=0; else res=inf;
		return res;
	}
	res=inf;
	for (int gate=0; gate<2; gate++) {
		if (gate!=g[v] && !c[v]) continue;
		int add=gate!=g[v];
		for (int v1=0; v1<2; v1++)
			for (int v2=0; v2<2; v2++) {
				int v3=(gate==1) ? (v1&v2) : (v1|v2);
				if (val!=v3) continue;
				res=min(res,solve(v*2+1,v1)+solve(v*2+2,v2)+add);
			}
	}
	return res;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int tn;
	cin>>tn;

	for (int tst=0; tst<tn; tst++) {
		writeCaseNumber(tst+1);
		memset(ans,-1,sizeof(ans));
		cin>>n>>v;
		for (int i=0; i<(n-1)/2; i++) 
			cin>>g[i]>>c[i];
		for (int i=0; i<(n+1)/2; i++)
			cin>>c[i+(n-1)/2];
		int res=solve(0,v);
		if (res<inf)
			printf("%d\n",res);
		else
			printf("IMPOSSIBLE\n");
	}

	return 0;
}
