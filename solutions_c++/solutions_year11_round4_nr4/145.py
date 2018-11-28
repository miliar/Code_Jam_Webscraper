#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<numeric>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<memory>
#include<string>
#include<vector>
#include<cctype>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

typedef unsigned long long		ui64;
typedef long long				i64;
typedef	vector<int>				vi;
typedef	vector<string>			vs;
typedef	pair<int,int>			pii;
typedef	pair<double,double>		point;

#define pb						push_back
#define mp						make_pair
#define X						first
#define Y						second
#define all(a)					(a).begin(), (a).end()
#define INF						(2000000000)

vector< vi > g;
vi reach;
int ans2,ans1;
void dfs(int x, set<int> used, int can){
	if(can==0){
		ans2 = max(ans2, ((int)used.size())-ans1 );	
		return;
	}
	can--;
	for(int i=0;i<(int)g[x].size();i++)
		used.insert(g[x][i]);
	for(int i=0;i<(int)g[x].size();i++){
		if(reach[ g[x][i] ] == can)
			dfs(g[x][i],used,can);
	}
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tests;
	scanf("%d",&tests);

	for(int test=0;test<tests;test++){
		printf("Case #%d: ", test+1);

		int n,m; cin >> n >> m;
		g.clear();
		reach.clear();
		g.resize(n);
		//for(int i=0;i<g.size();i++) g[i].
		for(int i=0;i<m;i++){
			string s; cin >> s;
			int a,b;
			a = b = 0;
			bool bx = true;
			for(int i=0;i<s.size();i++){
				if(s[i]==',')
					bx = false;
				else{
					if(bx)
						a = a*10 + (s[i]-'0');
					else
						b = b*10 + (s[i]-'0');
				}
			}
			g[a].pb(b);
			g[b].pb(a);
		}
		
		queue<int> Q;
		Q.push(1);
		reach.resize(n,100);
		reach[1] = 0;

		while(!Q.empty()){
			queue<int> P;
			while(!Q.empty()){
				int top = Q.front(); Q.pop();
				for(int i=0;i<(int)g[top].size();i++){
					if(reach[ g[top][i] ] > reach[top]+1){
						reach[ g[top][i] ] = reach[top] + 1;
						P.push( g[top][i] );
					}
				}
			}
			Q = P;
		}

		ans1 = reach[0];
		ans2 = -1;
		set<int> temp; temp.insert(0);
		dfs(0,temp,ans1);

		printf("%d %d\n", ans1-1, ans2);
	}

	return 0;
}