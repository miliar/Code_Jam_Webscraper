#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <map>
#include <set> 
#include <iomanip>
#include <sstream>
#include <fstream>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
#define REP(i,a) for(int i=0;i<a;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define SIZE(c) (int)c.size()
#define ALL(c) (c).begin(),(c).end() 
typedef pair<int, int> PII;
const int INF = 1000000000;
const int MAXN = 1005;
int T, N, a[MAXN];
bool vis[MAXN], used[MAXN];
double dp[MAXN];
vector<int> cycle;
int fac(int x){return x == 0 ? 1 : x * fac(x-1);}

int dfs(vector<int> v, int idx){
	if(vis[idx]) return 0;
	vis[idx] = true;
	return 1 + dfs(v, v[idx]);
}

vector<int> getCycles(vector<int> v){
	vector<int> ret;
	memset(vis, false, sizeof vis);
	for(int i = 0; i < SIZE(v); i ++){
		if(!vis[i])
			ret.push_back(dfs(v, i));
	}
	return ret;
}

double getAvg(int n){
	if(n == 1) return 0;
	if(used[n]) return dp[n];
	used[n] = true;
	/*
	double tot = 0;
	for(int i = 1; i <= n; i ++)
		tot += f / i;
	//cout<<tot<<endl;
	double ret = 0;
	for(int i = 1; i < n; i ++){
		ret += (f / i) * (1 + getAvg(i));
	}
	cout<<ret<<endl;*/
	vector<int> v;
	int f = fac(n);
	for(int i = 0; i < n; i ++) v.push_back(i);
	int r = 0;
	double ret = 0;
	do{
		vector<int> c = getCycles(v);
		
		if(c[0] == n){
			r ++;
			continue;
		}
		else{
			double t = 1;
			REP(i, SIZE(c)){
				t += getAvg(c[i]);
			}
			t *= (1.0 / f);
			ret += t;
		}
	}while(next_permutation(ALL(v)));
	return dp[n] = ((ret + r / (double)f)/ (1 - (r / (double)f)));
}

int main() {
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	cin>>T;
	memset(used, false, sizeof used);
	REP(t, T){
		cin>>N;
		vector<int> v;
		REP(i, N){
			cin>>a[i];
			v.push_back(a[i] - 1);
		}
		cycle = getCycles(v);
		double ret = 0;
		REP(i, SIZE(cycle)){
			ret += (cycle[i] == 1 ? 0 : cycle[i]);
		}
		cout<<"Case #"<<(t + 1)<<": ";
		cout<<fixed<<setprecision(6)<<ret<<endl;
	}

	return 0;
}
