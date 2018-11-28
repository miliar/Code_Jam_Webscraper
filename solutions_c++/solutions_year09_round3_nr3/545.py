#include <algorithm>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
 
using namespace std;
 
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int, int> ii;
#define FOR(i,a,b) for(typeof(a) i=(a); i < (b); i++)
#define sz(a) int((a).size()) 
#define all(c) (c).begin(), (c).end() 
#define tr(c, i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c, x) ((c).find(x) != (c).end()) 
#define cpresent(c, x) (find(all(c), x) != (c).end())
template<class T> T sqr(T x){return x*x;}
int toint(string s){istringstream sin(s); int x; sin>>x; return x;}
string tostring(int x){ostringstream sout; sout<<x; return sout.str();}

vi cell, visited;
int p, q, gold;
int fact[] = {1, 1, 2, 6, 24, 120};

enum {INF = 987654321};

void dfs(int v)
{
	if(v >= 0 && v < p && cell[v] && !visited[v]) {
		visited[v] = 1;
		gold++;
		dfs(v + 1);
		dfs(v - 1);
	}
}

int ans(vi &perm)
{
	int cost = 0;

	cell.clear();
	cell.resize(p, 1);
	
	FOR(i, 0, q) {
		visited.clear();
		visited.resize(p, 0);
		gold = 0;
		cell[perm[i]] = 0;
		dfs(perm[i] - 1);
		dfs(perm[i] + 1);
		cost += gold;
	}

	return cost;
}
		

void process(int tc)
{
	int cost = INF;

	scanf("%d %d", &p, &q);

	vi rel(q);
	
	FOR(i, 0, q) {
		scanf("%d", &rel[i]);
		rel[i]--;
	}

	FOR(i, 0, fact[q]) {
		cost = min(cost, ans(rel));
		next_permutation(all(rel));
	}

	printf("Case #%d: %d\n", tc, cost);
}

int main()
{
	int tc;

	scanf("%d", &tc);

	FOR(i, 0, tc) 
		process(i + 1);
	
	return 0;
}
