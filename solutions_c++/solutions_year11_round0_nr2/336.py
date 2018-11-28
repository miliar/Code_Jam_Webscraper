#pragma comment(linker, "/STACK:16777216")

#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <memory.h>

using namespace std;

#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define FORD(i,a,b) for (int i = (int)(a)-1; i >= (int)(b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPD(i,a) FORD(i,a,0)
#define SQR(a) (a)*(a)
#define MP make_pair
#define PB push_back
#define FILL(a) memset(a,0,sizeof(a));
#define SIZE(a) (int)((a).size())
#define ALL(a) (a).begin(),(a).end()
#define LL long long
const double PI = 2*acos(0.0);
const double EPS = 1e-12;
const int INF = 1000000000;

int tc, n, c, d;
char k;
string s;
string ans;
string cc[1000];
string dd[1000];
char ispair[26][26];
bool isbad[26][26];

bool foundbad(){
	REP(i,ans.size()-1)
		if (isbad[ans[i]-'A'][ans[ans.size()-1]-'A']) return true;
	return false;
};

int main(){
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	cin >> tc;
	REP(ic,tc){
		cin >> c;
		REP(i,c) cin >> cc[i];
		cin >> d;
		REP(i,d) cin >> dd[i];
		cin >> n >> s;
		memset (ispair, ' ', sizeof (ispair));
		memset (isbad, false, sizeof (isbad));
		REP(i,c) ispair[cc[i][0]-'A'][cc[i][1]-'A'] = ispair[cc[i][1]-'A'][cc[i][0]-'A'] = cc[i][2];
		REP(i,d) isbad[dd[i][0]-'A'][dd[i][1]-'A'] = isbad[dd[i][1]-'A'][dd[i][0]-'A'] = true;
		ans = "";
		REP(i,s.size()){
			ans += s[i];
			if (ans.size()>1){
				if (ispair[ans[ans.size()-1]-'A'][ans[ans.size()-2]-'A']!=' '){
					k = ispair[ans[ans.size()-1]-'A'][ans[ans.size()-2]-'A'];
					ans = ans.substr(0,ans.size()-2);
					ans += k;
				}else if (foundbad ()) ans = "";
			};
		};
		printf ("Case #%d: [", ic+1);
		REP(i,(int)ans.size()-1) printf ("%c, ", ans[i]);
		if (ans.size()) printf ("%c", ans[ans.size()-1]);
		printf ("]\n");
	};
	return 0;
};