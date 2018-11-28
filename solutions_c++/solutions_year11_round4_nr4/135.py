#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <ctime>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define fore(i, a, b) for(int i = a; i < (int)(b); ++i)
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(a) a.begin,a.end()
#define ll long long

vector<int> g[1234];

int n, m;

int q[1234];

int d[1234][1234];

void bfs(int v){
	bool used[434];
	memset(used, 0, sizeof used);
	int h = 0, t = 0;
	q[0] = v;
	d[v][v] = 0;
	while(t <= h){
		int w = q[t++];
		forn(i, g[w].size()){
			int u = g[w][i];
			if (!used[u]){
				d[v][u] = d[v][w] + 1;
				used[u] = 1;
				q[++h] = u;
			}
		}
	}
}

int dyn[555][555];

int get(int u, int v) {
	if(dyn[u][v] != -1)
		return dyn[u][v];

	if(d[u][v] == 1000)
		return -1000;

	if(d[u][v] == 1) {
		dyn[u][v] = (int)g[u].size() - 1;
		if(u == 0)
		return dyn[u][v];
	}

	int res = 0;

	forn(k, n){
		if(d[u][k] + d[k][v] == d[u][v] && k != u && k != v) {
			int cur = get(u, k) + get(k, v);
			cur += (int)g[k].size() - 1;
			if(cur > res)
				res = cur;
		}
	}
	return dyn[u][v] = res;
}

int best;
bool us[1234];



void go(int v){
	if(v == 1){
		int c = 0;
		bool cnt[38];
		memset(cnt, 0, sizeof cnt);
		forn(i, n){
			if (us[i]){				
				forn(j, g[i].size()){
					if ((g[i][j] == 1 || !us[g[i][j]]) && !cnt[g[i][j]])
						++c, cnt[g[i][j]] = 1;
				}
			}
		}
		best = max(best, c);
		return;
	}
	forn(i, g[v].size()){
		if(!us[g[v][i]] && d[v][g[v][i]] + d[g[v][i]][1] == d[v][1]){
			us[g[v][i]] = 1;
			go(g[v][i]);
			us[g[v][i]] = 0;
		}
	}
}

int main(){
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int t;
	cin >> t;
	forn(tt, t){
		cerr << tt << endl;
		cin >> n >> m;
		string s;
		getline(cin, s);
		forn(i, n)
			g[i].clear();
		forn(i, 1){
			getline(cin, s);
			s += "   ";
			char* ss = (char*)s.c_str();
			int x, y;
			while(sscanf(ss, "%d,%d", &x, &y) == 2){
				if(x != 1)
					g[x].pb(y);
				if(y != 1)
					g[y].pb(x);
				while(*ss != ' ')
					ss++;
				while(*ss == ' ')
					ss++;
			}
		}
		forn(i, n){
			forn(j, n)
				d[i][j] = 1000;
			bfs(i);
		}
		int FIR = d[0][1];
		best = 0;
		us[0] = 1;
		go(0);
		/*
		memset(dyn, -1, sizeof dyn);
		int SEC = get(0, 1);
		*/
		printf("Case #%d: %d %d\n", tt + 1, FIR - 1, /*SEC + 1 - FIR + 1*/ best);
	}
	
	return 0;
}