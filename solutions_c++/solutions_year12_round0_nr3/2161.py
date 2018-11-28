//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
//#pragma comment(linker,"/STACK:33554432") /*32Mb*/
#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<numeric>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<memory>
#include<string>
#include<vector>
#include<cctype>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

typedef unsigned long long      ui64;
typedef long long               i64;
typedef	vector<int>             VI;
typedef	vector<bool>            VB;
typedef	vector<VI>              VVI;
typedef	vector<string>          VS;
typedef	pair<int,int>           PII;
typedef map<string,int>         MSI;
typedef set<int>                SI;
typedef set<string>             SS;
typedef map<int,int>            MII;
typedef	pair<double,double>     PDD;

#define PB                      push_back
#define MP                      make_pair
#define X                       first
#define Y                       second
#define FOR(i, a, b)            for(int i = (a); i < (b); ++i)
#define RFOR(i, a, b)           for(int i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b)             memset(a, b, sizeof(a))
#define SZ(a)                   int((a).size())
#define ALL(a)                  (a).begin(), (a).end()
#define RALL(a)                 (a).rbegin(), (a).rend()
#define INF                     (2000000000)

int leng(int a) {
	if(!a) return 1;
	int k = 0;
	while(a) {
		k++;
		a /= 10;
	}
	return k;
}

int solve(int A, int B) {
	int ans = 0;
	FOR(i,A,B+1) {
		int t = i;
		int L = leng(t);
		int p10 = (int)pow(10.0,L-1);
		t = 10*(t%p10) + (t/p10);
		while(t!=i) {
			if(t>i && t<=B) ans++;
			t = 10*(t%p10) + (t/p10);
		}
	}
	return ans;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int t;
	cin >> t;
	FOR(test,0,t) {
		int A,B;
		cin >> A >> B;
		printf("Case #%d: %d\n",test+1,solve(A,B));
	}
    return 0;
}