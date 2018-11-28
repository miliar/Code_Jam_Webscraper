#define _CRT_SECURE_NO_DEPRECATE

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
//added
#include <conio.h>
#include <list>
#include <stack>
#include <bitset>

using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;


#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()



template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }


int main() {
	std::freopen("input.txt", "rt", stdin);
	std::freopen("output.txt", "wt", stdout);

	int t;
	scanf("%d", &t);
	For(test, 1, t) {
		int len;
		cin>>len;
		vi top, bottom;
		Rep(i,len)
		{
			int tt; cin>>tt;
			top.push_back(tt);
		}
		sort(All(top));
		Rep(i,len)
		{
			int tt; cin>>tt;
			bottom.push_back(tt);
		}
		sort(bottom.rbegin(),bottom.rend());
		vector<int>::iterator itt = top.begin(),itb = bottom.begin();
		long int sum = 0;
		for(;itt!=top.end();++itt,++itb)
		{
			sum+= ((*itt) * (*itb));
		}
		printf("Case #%d: %d\n",test,sum);
	}

	//_getch();
	exit(0);
}

/*
struct comp_insens_struct {
	bool operator () (const string &a, const string &b)
	{
		int r;

		r = strcasecmp (a.c_str (), b.c_str ());

		if (r < 0)
			return true;
		else
			return false;
	}
};
*/