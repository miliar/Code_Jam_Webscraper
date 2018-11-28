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

//double M[10];
int n;
int p[1024];

void sol()
{
	int tmp=0;
	FOR(a,1,n) if (p[a] != a) tmp++;
	cout << tmp << ".00000";
	/*M[2]=2.;
	FOR(n,3,10)
	{
		int p[12];
		int ans[12];
		int fa=0;
		CLR(ans);
		FOR(a,1,n) p[a]=a;
		while(1)
		{
			fa++;
			int t=0;
			FOR(a,1,n) if (p[a]==a) t++;
			ans[t]++;
			if (!next_permutation(p+1, p+n+1)) break;
		}
		double tmp = 1.;
		FOR(a,1,n) tmp += (M[n-a]*ans[a])/fa;
		M[n] = tmp / (1. - (double)ans[0]/(double)fa);
	}

	FOR(a,0,10) cout << M[a] << "\n";*/
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin >> T;
	FOR(t,1,T)
	{
		cin >> n;
		FOR(a,1,n) cin >> p[a];
		cout << "Case #" << t << ": ";
		sol();
		cout << "\n";
	}
	return 0;
}