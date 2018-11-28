#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <fstream>
#include <iostream>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <vector>
#include <utility>
#include <cmath>
using namespace std;

#ifdef _WIN32
#  define I64 "%I64d"
#else
#  define I64 "%lld"
#endif

#define pb push_back
#define mp make_pair
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()

#define forn(i,n) for (int i=0; i<int(n); ++i)
#define fornd(i,n) for (int i=int(n)-1; i>=0; --i)
#define forab(i,a,b) for (int i=int(a); i<=int(b); ++i)

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;


const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;

string its (const int &val){
	stringstream ss;
	ss << val;
	return ss.str();
}

int sti (const string &s){
	stringstream ss;
	ss << s;
	int val;
	ss >> val;
	return val;
}

int main(){
#ifndef ONLINE_JUDGE
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
#endif
	int n;
	scanf("%d", &n);
	forn(testcase,n){
		set <pair <int,int> > ans;
		int a,b;
		scanf("%d%d", &a, &b);
		forab(i,a,b){
			string val = its(i);
			int m = sz(val);
			forn(j,m){
				if (val[j] == '0') continue;
				string wtf = "";
				forn(k,m)
					wtf += val[(j+k)%m];
				int num = sti(wtf);
				if (num>i && num<=b)
					ans.insert(mp(i,num));
			}
		}
		int out = sz(ans);
		printf("Case #%d: %d\n", testcase+1, out);
	}
    return 0;
}