#pragma comment(linker,"/STACK:32000000")
#include <stdio.h>
#include <iostream>
#include <sstream>
#include <queue>
#include <algorithm>
#include <vector>
#include <math.h>
#include <set>
#include <map>
#include <string>

using namespace std;

#define infile ".in"
#define outfile ".out"
#define FOR(i, n) for (int i = 0; i <(n); i++)
#define DFOR(i, n) for (int i = (n) - 1; i >= 0; i--)
#define PB push_back
#define MP make_pair
#define ALL(x) x.begin(), x.end()
#define LL long long
#define SQR(x) ((x) * (x))
#define ABS(x) ((x) < 0 ? -(x) : (x))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define CLR(a, b) memset((a), (b), sizeof(a))
#define SS stringstream
#define PII pair<int, int>
#define VPII vector < PII >

void init(){
	freopen(infile, "r", stdin);
	freopen(outfile, "w", stdout);
}

int n;
int ans;
vector<int> v[2];
vector<int> p[2];
int x[2];
int ind[2];


void solvecase(){
	ans = 0;
	int cur = 0;
	x[0] = x[1] = 0;
	ind[0] = ind[1] = 0;
	while(cur < n){
		bool f1 = false, f2 = false;
		ans++;
		if(ind[0]<v[0].size() && v[0][ind[0]]!=x[0]){
			f1 = true;
			if(v[0][ind[0]] < x[0]) 
				x[0]--;
			else
				x[0]++;
		}
		if(ind[1]<v[1].size() && v[1][ind[1]]!=x[1]){
			f2 = true;
			if(v[1][ind[1]] < x[1]) 
				x[1]--;
			else
				x[1]++;
		}
		if(!f1 && ind[0]<v[0].size() && v[0][ind[0]]==x[0] && p[0][ind[0]]==cur){
			cur++;
			ind[0]++;
			continue;
		}
		if(!f2 && ind[1]<v[1].size() && v[1][ind[1]]==x[1] && p[1][ind[1]]==cur){
			cur++;
			ind[1]++;
			continue;
		}		
	}
	cout << ans << endl;
}

void solve(){
	int t;
	cin >> t;
	for(int i=0; i<t; i++){
		cin >> n;
		v[0].clear(); v[1].clear();
		p[0].clear(); p[1].clear();
		for(int j=0; j<n; j++){
			string s;
			cin >> s;
			int x;
			cin >> x;
			x--;
			if(s=="O"){
				v[0].push_back(x);
				p[0].push_back(j);
			} else {
				v[1].push_back(x);
				p[1].push_back(j);
			}			
		}		
		cout << "Case #" << i+1 << ": ";
		solvecase();
	}
}

int main(){
	init();
	solve();
	return 0;
}