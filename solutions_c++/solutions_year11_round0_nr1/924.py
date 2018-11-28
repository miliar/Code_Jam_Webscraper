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

template<class T> T Abs(T x) { return x < 0 ? -x : x; }
template<class T> T Sign(T x) { return x < 0 ? -1 : x > 0 ? 1 : 0; }

struct S{
	int p[2];
	int i;
	S() {}
	S(int a, int b, int i) : i(i) {
		p[0] = a;
		p[1] = b;
	}
};
typedef pair<int, S> N;

bool operator < (const S& a, const S& b){
	return memcmp(&a, &b, sizeof(a)) < 0;
}

void Go(){
	int n;
	cin >> n;
	string s;
	int p;
	vector<PII> d;
	vector<VI> pp(2, VI(n, -1));
	FOR(i, n){
		cin >> s >> p;
		d.push_back(PII(s[0] == 'O' ? 0 : 1, p - 1));		
	}
	FOR(j, 2){
		int c = -1;
		for (int i = n - 1; i >= 0; i--){
			if (d[i].first == j)
				c = i;
			pp[j][i] = c;
		}
	}		
	int res = -1;
	N u = N(0, S(0, 0, 0));
	for (;;){		
		if (u.second.i >= n){
			res = u.first;
			break;
		}

		PII& a = d[u.second.i];
		N v = u;
		if (v.second.p[a.first] == a.second){			
			v.second.i++;			
		}
		else{
			v.second.p[a.first] += Sign(a.second - u.second.p[a.first]);
		}
		if (pp[a.first ^ 1][u.second.i] != -1){
			v.second.p[a.first ^ 1] += Sign(d[pp[a.first ^ 1][u.second.i]].second - u.second.p[a.first ^ 1]);
		}
		v.first++;
		u = v;
	}
	printf("%d", res);
}

int main(){
	const string task = "A";
	const int attempt = -1;
	bool dbg = false;


	if (dbg){
		freopen("inp.txt", "r", stdin);
	}
	else{
		stringstream ss;
		ss << "gcj/2011/qual/";
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
		printf("Case #%d: ", i + 1);
		Go();
		printf("\n");
	}
	return 0;
}