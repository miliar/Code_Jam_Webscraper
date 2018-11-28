#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <cstring>
#include <ctime>
#include <cstdio>
#include <memory>
using namespace std;
#define pb push_back
#define INF 1000000000
#define L(s) (int)((s).end()-(s).begin())
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define C(a) memset((a),0,sizeof(a))
#define ll long long
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define VI vector<int>
#define ppb pop_back
#define mp make_pair
#define pii pair<int,int>
#define pdd pair<double,double>
//#define x first
//#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pi 3.1415926535897932384626433832795028841971
//#define tt (ll+rr)/2
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define rnd() ((rand() << 16) ^ rand())

void go(string & cur, set<pair<char, char> > & s, map<pair<char, char>, char> & m)
{
	if (L(cur) > 1)
	{
		if (m.find(mp(cur[L(cur) - 1], cur[L(cur) - 2])) != m.end())
		{
			char c = m[mp(cur[L(cur) - 1], cur[L(cur) - 2])];
			cur.ppb(), cur.ppb();
			cur += c;
			go(cur, s, m);
			return;
		}
	}
	
	if (L(cur))
	{
		rept(i, L(cur) - 1)
			if (s.find(mp(cur[L(cur) - 1], cur[i])) != s.end())
			{
				cur = "";
				return;
			}
	}

}

int main()
{
	#ifndef ONLINE_JUDGE 
	freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout); 
	#endif
	
	int TC;
	cin >> TC;
	rep(tc, TC)
	{
		int c, d, n;
		cin >> n;
		vector<string> vs(n);
		rept(i, n)
			cin >> vs[i];
		cin >> d;
		vector<string> ops(d);
		rept(i, d)
			cin >> ops[i];
		cin >> n;
		string s;
		cin >> s;

		set<pair<char, char> > op;

		rept(i, L(ops))
			op.insert(mp(ops[i][0], ops[i][1])),
			op.insert(mp(ops[i][1], ops[i][0]));

		map<pair<char, char>, char> m;
		rept(i, L(vs))
		{
			string t = vs[i].substr(0, 2);
			m[mp(t[0], t[1])] = vs[i][2];
			m[mp(t[1], t[0])] = vs[i][2];
		}

		string cur;

		rept(i, n)
		{
			cur += s[i];
			go(cur, op, m);
		}


		printf("Case #%d: ", tc);
		printf("[");
		rept(i, L(cur))
		{
			if (i) printf(", ");
			printf("%c", cur[i]);
		}
		printf("]\n");


	}
	
	return 0;
}
