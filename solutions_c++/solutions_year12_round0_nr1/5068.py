#include <array>
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
#include <utility>
#include <conio.h>
using namespace std;

typedef long long int64;
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

const double pi = 2*acos(0.0);

int main() 
{
	freopen("A-small-attempt1.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int t;
	string translatorbase("ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz");
	string translator("our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq");
	string g;
	string resp;
	int found;

	scanf("%d", &t); 
	getline(cin, g);

	For(test, 1, t) 
	{
		getline(cin, g);

		resp="";
		Rep(i, g.size())
		{
			found = translatorbase.find(g[i]);
			resp += translator[found];
		}

		printf("Case #%d: ", test);
		cout << resp << endl;
	}

	fclose (stdin);
	fclose (stdout);

	exit(0);
}
