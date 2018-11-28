#pragma comment(linker, "/STACK:16777216")
#include <queue>
#include <cassert>
#include <sstream>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <iostream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
#define FOR(i, n) for(int i = 0; i < (int)(n); ++i)


void Go(){
	int n;
	cin >> n;
	vector<string> d(n);
	FOR(i, n)
		cin >> d[i];	
	VI cnt(n);
	VI win(n);
	FOR(i, n){		
		FOR(j, n){
			if (d[i][j] == '1'){
				win[i]++;
				cnt[i]++;
			}			
			else if (d[i][j] == '0')
				cnt[i]++;
		}
	}
	vector<double> WP(n);
	FOR(i, n){
		WP[i] = (double)(win[i]) / cnt[i];
	}
	vector<double> OWP(n);
	FOR(i, n){
		double dd = 0;
		int c = 0;
		FOR(j, n){			
			if (d[i][j] == '1'){
				dd += (double)(win[j]) / (cnt[j] - 1);
				c++;
			}
			else if (d[i][j] == '0'){
				dd += (double)(win[j] - 1) / (cnt[j] - 1);
				c++;
			}
		}
		if (c == 0)
			throw 42;
		OWP[i] = dd / c;
	}
	vector<double> OOWP(n);
	FOR(i, n){
		double dd = 0;
		int c = 0;
		FOR(j, n){
			if (d[i][j] != '.'){
				dd += OWP[j];
				c++;
			}
		}
		if (c == 0)
			throw 42;
		OOWP[i] = dd / c;
	}
	vector<double> RPI(n);
	FOR(i, n){
		RPI[i] = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
	}
	FOR(i, n){
		printf("%0.10lf\n", RPI[i]);
	}
}

int main(){
	const string task = "A";
	const int attempt = -1;
	const bool dbg = false;


	if (dbg){
		freopen("inp.txt", "r", stdin);
	}
	else{
		stringstream ss;
		ss << "gcj/2011/1b/";
		if (attempt < 0)
			ss << task << "-large";
		else
			ss << task << "-small-attempt" << attempt;
		freopen((ss.str() + ".in").c_str(), "r", stdin);
		freopen((ss.str() + ".out").c_str(), "w", stdout);
	}


	int t;
	scanf("%d", &t);
	FOR(i, t){
		printf("Case #%d: \n", i + 1);
		Go();		
	}
	return 0;
}