#pragma comment(linker, "/STACK:16777216")
#include <queue>
#include <cassert>
#include <sstream>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <iostream>
#include <float.h>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
#define FOR(i, n) for(int i = 0; i < (int)(n); ++i)

template<class Arg, class Ret, Ret (*fn)(const Arg&), class Mem = map<Arg, Ret> > struct Memoizer {
	typedef map<Arg, Ret> Mem;
	Mem mem;
	Ret operator ()(const Arg& arg){		
		pair<Mem::iterator, bool> ret = mem.insert(pair<Arg, Ret>(arg, Ret()));
		if (ret.second){
			ret.first->second = fn(arg);
			if (!_finite(ret.first->second)){
				ret.first->second = fn(arg);
				ret.second = true;
			}
		}
		return ret.first->second;
	}
};

double _Fact(const int& n);
Memoizer<int, double, _Fact> Fact;
double _Fact(const int& n){
	if (n == 0)
		return 1;
	return Fact(n - 1) * n;
}

double _C(const PII& nk);
Memoizer<PII, double, _C> C;
double _C(const PII& nk){
	return Fact(nk.first) / (Fact(nk.second) * Fact(nk.first - nk.second));
}

double _B(const int& n);
Memoizer<int, double, _B> B;
double _B(const int& n){
	if (n == 0)
		return 1;
	return B(n - 1) * n + (n % 2 ? -1 : 1);
}

double _P(const PII& nk);
Memoizer<PII, double, _P> P;
double _P(const PII& nk){
	int n = nk.first;
	int k = nk.second;
	if (k == n){
		return 1.0 / Fact(n);
	}
	else if (k == n - 1){
		return 0;
	}
	else{
		return B(n - k) * C(PII(n, k)) / Fact(n);
	}
}

double _Get(const int& n);
Memoizer<int, double, _Get> Get;
double _Get(const int& n){
	if (n == 0)
		return 0;
	double res = 1;
	for (int i = 1; i <= n; i++)
		res += P(PII(n, i)) * Get(n - i);
	res /= (1 - P(PII(n, 0)));
	return res;
}

double Good(VI d){
	int s = 0;
	FOR(i, d.size())
		if (d[i] != i)
			s++;	
	return Get(s);
}

double Wrong(VI d){
	int n = d.size();
	VI cycleId(n, -1);
	double res = 0;
	FOR(i, n){
		if (cycleId[i] == -1){
			int cnt = 0;
			int p = i;
			for (;;){
				cycleId[p] = i;
				cnt++;
				p = d[p];
				if (cycleId[p] == i)
					break;
			}
			res += (cnt - 1) * 2;
		}
	}
	return res;
}

double VeryGood(VI d){
	int s = 0;
	FOR(i, d.size())
		if (d[i] != i)
			s++;	
	return s;
}

void Go(){	
	int n;
	scanf("%d", &n);
	VI d(n);
	FOR(i, n){
		scanf("%d", &d[i]);
		d[i]--;
	}
	//double res1 = Wrong(d);
	//double res = Good(d);
	double res = VeryGood(d);
	printf("%0.6lf", res);
}


int main(){	
	const string task = "D";
	const int attempt = -1;
	const bool dbg = false;


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