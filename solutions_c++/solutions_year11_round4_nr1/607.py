#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <algorithm>
#include <memory.h>

using namespace std;

#define WR printf
#define RE scanf
#define PB push_back
#define SE second
#define FI first

#define FOR(i,k,n) for(int i=(k); i<=(n); i++)
#define DFOR(i,k,n) for(int i=(k); i>=(n); i--)
#define SZ(a) (int)((a).size())
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define CLR(a) memset(a, 0, sizeof(a))

#define LL long long
#define VI  vector<int>
#define PAR pair<int ,int>
#define o_O 1000000000 
void __never(int a){printf("\nOPS %d", a);}
#define ass(s) {if (!(s)) {__never(__LINE__);cout.flush();cerr.flush();abort();}}

int X, S, R, n;
double t;
int B[1024], E[1024], W[1024];
int WW[1001000];

void sol()
{
	CLR(WW);
	FOR(a,1,n) FOR(b,B[a]+1,E[a]) WW[b] = W[a];
	sort(WW+1, WW+X+1);
	//reverse(WW+1, WW+X+1);

	double ans=0.;
	FOR(a,1,X)
		if (ans < t && ans+1./(WW[a]+R) > t)
		{
			ans = t + (1.-(t-ans)*(WW[a]+R))/(WW[a]+S);
		}
		else if (ans < t)
		{
			ans += 1./(WW[a]+R);
		}
		else ans += 1./(WW[a]+S);
	WR("%.10lf", ans);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin >> T;
	FOR(z,1,T)
	{
		cin >> X >> S >> R >> t >> n;
		FOR(a,1,n) cin >> B[a] >> E[a] >> W[a];
		cout << "Case #" << z << ": ";
		sol();
		cout << "\n";
	}
	return 0;
}