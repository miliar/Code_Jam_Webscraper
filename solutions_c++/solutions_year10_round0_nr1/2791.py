#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;


typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()


int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int T;
	cin>>T;
	For(i, 1, T) {
		int s;
		long q, count;
		cin>>s>>q;
		count = pow(2,s) - 1;
		q-=count;
		if(0==(q%(count+1)))
			cout<<"Case #"<<i<<": ON"<<endl;
		else
			cout<<"Case #"<<i<<": OFF"<<endl;
	}
	return 0;
}
