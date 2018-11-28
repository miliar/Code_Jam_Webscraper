#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
#include <memory.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef double dd;
typedef long double ld;
typedef vector <int > VI;
typedef vector < VI > VVI;
typedef vector < ll > VLL;
typedef vector < dd > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define VAR(V,init) __typeof(init) V=(init)
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define FOREACH(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define ALL(X) (X).begin(),(X).end()
#define CLE(a,b) memset(a,b,sizeof(a))
#define MINN(a,b) ((a)>(b)?(b):(a))
#define MAXX(a,b) ((a)<(b)?(b):(a))
#define PB push_back
#define PF push_front
#define CB pop_back
#define CF pop_front
#define MP make_pair
#define FI first
#define SE second
#define SZ(X) ((int)(X.size()))
#define INF 1000000000
#define INFLL 1000000000000000000ll
int COND = 100;
#define DB(x) ({if(COND){COND--; cerr << __LINE__ << " : " << #x << ": " << x << endl; };})
#define deb(A) //A
//////////////////

#define MAX_L 15
#define MAX_N 5000

const int p = 70032301, q = 1000000007;

int l, d, n;
set<int> dic[MAX_L];
char word[MAX_L + 1], pat[(MAX_L + 2) * MAX_N + 10];
VS pos;
VI len;

int hash(const string & s) {
	int has = 0, l = s.length() - 1;
	FORD(i, l, 0)
		has = ((ll)has * (ll)p + s[i]) % q;
	return has;
}

VS parse(const string & s) {
	VS res;
	res.clear();
	int l = s.length(), is = 0;
	string tok;
	while(is < l) {
		tok = "";
		if(s[is] == '(') {
			++is;
			while(s[is] >= 'a' && s[is] <= 'z')
				tok += s[is++];
			++is;
			res.PB(tok);
		}
		else
			res.PB(tok + s[is++]);
	}
	return res;
}

void rek(int n, int & res, int w, int pn) {
	if(n > 0 && dic[n - 1].find(w) == dic[n - 1].end())
		return;
	if(n == l) {
		++res;
		return;
	}
	FOR(i, 0, len[n] - 1)
		rek(n + 1, res, (((ll)w) + ((ll)pn) * ((ll)pos[n][i]))% q, (((ll)pn) * ((ll)p)) % q);
}

int main()
{
	scanf("%d%d%d\n", &l, &d, &n);
	REP(i, d) {
		scanf("%s\n", word);
		string w(word);
		int s = w.length();
		REP(i, s)
			dic[i].insert(hash(w.substr(0, i + 1)));
	}
	REP(i,n) {
		scanf("%s\n", pat);
		pos = parse(string(pat));
		len.clear();
		FOREACH(ip, pos)
			len.PB(ip->length());
		int res = 0;
		rek(0, res, 0, 1);
		printf("Case #%d: %d\n", i + 1, res);
	}
	return 0;
}
