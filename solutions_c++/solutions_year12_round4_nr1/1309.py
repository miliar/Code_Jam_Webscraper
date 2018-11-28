#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

typedef long long Long;
typedef unsigned long long uLong;
typedef unsigned int uint;

const double PI = acos(-1.0);
const double EPS = 1e-12;

#define FOR(i,a,b) for (int i=(int)(a); i<(int)(b); ++i)
#define two(X) (1<<(X))
#define twoL(X) (((Long)(1))<<(X))
#define bit(S,X) (((S)&two(X))!=0)
#define bitL(S,X) (((S)&twoL(X))!=0)

template<class T> string toStr(T n){ostringstream ss;ss<<n;ss.flush(); return ss.str();}
template<class T> string vtos(vector<T> a) { stringstream ss; for (int i=0; i<(int)a.size(); i++) { if (i > 0) ss << ", "; ss << a[i]; } return ss.str(); }

int toInt(string s){int n=0; istringstream ss(s); ss>>n; return n;}
Long toLong(string s){Long n=0; istringstream ss(s); ss>>n; return n;}

int N, D;
int dist[10005], len[10005];

/*
map< pair<int, int>, bool> mem;
bool get(pair<int, int> a)
{
	if (mem.find(a) != mem.end())
		return mem[a];

	return true;
}*/

bool can_reach(int cur, int next, int radius)
{
	return dist[cur] + radius >= dist[next];
}

int getRad(int cur_loc, int vine_holding)
{
	int op1 = dist[vine_holding] - cur_loc;
	int op2 = len[vine_holding];

	if (op2 >= op1) return op1;
	else return dist[vine_holding] - op2;
}

bool dfs(int cur_loc, int vine_holding)
{
	int radius = getRad(cur_loc, vine_holding);
	//cerr << "Currently at loc" << cur_loc << ", holding vine#" << vine_holding << ", with a radius of " << radius << endl;
	if (cur_loc + 2*radius >= D) return true; //can reach from here

	for (int i=vine_holding+1; i<N; i++)
		if (can_reach(vine_holding, i, radius) && dfs(max(dist[vine_holding], dist[i]-len[i]) , i))
			return true;

	return false;
}

void solve()
{
	cin >> N;
	FOR(i,0,N)
		cin >> dist[i] >> len[i];

	cin >> D;

	if (dfs(0, 0))
		cout << "YES" << endl;
	else cout << "NO" << endl;
	
}

int main()
{
	freopen("data.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin >> T;
	for (int x=1; x<=T; x++) 
	{
		printf("Case #%d: ", x);
		solve();
	}

	return 0;
}

