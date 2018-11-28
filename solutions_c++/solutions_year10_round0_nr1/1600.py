//Author: suh_ash2008
#include <iostream>
#include <cstdio>
#include <cctype>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cassert>
#include <string.h>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define GL ({LL t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define SET(x,a) memset(x,a,sizeof(x));
#define all(a) a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define tr(i,a) for( typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define pb push_back
#define sz(a) (int)(a.size())
#define INF (int)1e9
#define EPS (double)1e-12
#define is istringstream
#define os ostringstream
#define lb lower_bound
#define ub upper_bound
#define bs binary_search

typedef long long LL;
typedef unsigned long long ULL;
typedef pair< int,int > ii;
typedef vector< ii > vii;
typedef vector < vii > vvii;
typedef vector< int > vi;
typedef vector< vi > vvi;
typedef vector< string > vs;

#define MAXN 1000+5
int seen[MAXN], next_inx[MAXN];
int weight[MAXN], cost[MAXN];

int main(){
	ifstream fin("A.in");
	ofstream fout("A.out");
	int _, kase = 0;
	fin >> _;
	while(_--){
		kase++;
		int N, K;
		fin >> N >> K;
		bool ok = 1;
		REP(i, N){
		    if(K % 2)    K /= 2;
			else {ok = 0; break;}
		}
		fout << "Case #" << kase << ": ";
		if(ok)    fout << "ON\n";
		else fout << "OFF\n";
	}
	fin.close();
	fout.close();
	return 0;
}
