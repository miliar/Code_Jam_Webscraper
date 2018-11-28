#include<iostream>
#include<stdio.h>
#include<assert.h>
#include<string.h>
#include<time.h>
#include<stdlib.h>
#include<math.h>
#include<string>
#include<sstream>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<vector>
#include<algorithm>
#pragma comment(linker, "/STACK:16777216")
#define pb push_back
#define ppb pop_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define LL long long
#define bit __builtin_popcountll
using namespace std;
template<class T> inline T sqr(T x) { return x * x; }
typedef pair<int, int> pii;
const double eps = 1e-9;
const double pi = acos(-1.0);
const int maxn = (int)2e6 + 10;
int A,B,I;
int what[maxn];
int calc(int x)
{
	int res = 0;
	stringstream ss;
	ss<<x;
	string s;
	ss>>s;
	for(int i = 1; i < sz(s); i++)
	{
		string t = s.substr(i);
		string r = s;
		r.erase(i);
		r = t + r;
		stringstream tt(r);
		int y;
		tt>>y;
		if (A <= y && y <= B && x < y)
		{
			if (what[y] != I) res++;
			what[y] = I;
		}
	}
	return res;
}
int main()
{
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	int T;
	cin>>T;
	for(int t = 0; t < T; t++)
	{
		memset(what,0,sizeof(what));
		cin>>A>>B;
		int res = 0;
		for(int i = A; i <= B; i++)
		{
			I = i;
			res += calc(i);
		}
		printf("Case #%d: %d\n",t + 1,res);
	}
	return 0;
}
