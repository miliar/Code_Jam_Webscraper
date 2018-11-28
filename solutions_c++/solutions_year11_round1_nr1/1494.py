#include <iostream>
#include <iomanip>
#include <ctime>
#include <numeric>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <sstream>
#include <map>
#include <set>
#include <cstdio>
#include <queue>
#include <list>
#include <stack>
#define ll long long
#define vi vector<int>
#define mp make_pair
#define oo (1<<30)
#define ones(x) __builtin_popcount(x)
#define All(v) (v).begin(),(v).end()
#define rAll(v) (v).rbegin(),(v).rend()
#define x first
#define y second
#define pb push_back
#define eps (1e-9)
#define MAX 2400
using namespace std;
/*int n,m;
int p[MAX];
void Init(int n) {for(int i = 0; i <=n ; i++) p[i] = i;}
int Find(int a){ return p[a] == a? a : p[a] = Find(p[a]); }
void link(int a,int b){ p[a] = b; }
void Union(int a, int b) {link(Find(a),Find(b));}
*/
//int g[MAX][MAX];
//vector<vector<int> > g;
//vector<pair<int,pair<int,int> > > edg;
//bool air[MAX];
//int dist[MAX];
/*struct state{
	int u,v;
	state(){}
	state(int u,int v):u(u),v(v){}
};*/

int main(){
	int runs;
	
	cin>>runs;
	for(int r = 1; r <= runs; r++){
		int N,pd,pg;
		cin>>N>>pd>>pg;
		printf("Case #%d: ",r);		
		if (pg == 0 && pd > 0){
			printf("Broken\n");
			continue;
		
		}
		if (pg == 100 && pd != 100){
			printf("Broken\n");
			continue;
		}
		if (pd == 100){
			printf("Possible\n");
			continue;
		}
		
		if (pd < 100 && pg < 100){
			int G = __gcd(pd,100);
			pd /= G;
			int c = 100/G;
			if( c <= N && c > pd ) printf("Possible\n");
			else printf("Broken\n");
		}
	}
	
	return 0;
}
