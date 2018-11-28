#define _CRT_SECURE_NO_DEPRECATE
#include<cstdio>
#include<vector>
#include<queue>
#include<string>
#include<set>
#include<sstream>
#include<iostream>
using namespace std;

#define FOR(i,s,n) for(int i = (s); i < (n); ++i)
#define REP(i,n) FOR(i,0,n)
#define sz(x) int((x).size())
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define all(x) (x).begin(),(x).end()

typedef vector<int> VI;
typedef pair<int, int> PII;
#define SS stringstream
template<typename T> string tos(T q,int w=0){SS A;A.flags(ios::fixed);A.precision(w);A<<q;string s;A>>s;return s;}
template<typename T> T sto(string s){SS A(s);T t;A>>t;return t;}
template<typename T> vector<T > s2v(string s){SS A(s);vector<T > ans;while(A&&!A.eof()){T t;A>>t;ans.pb(t);}return ans;}


struct Node {
	double p;
	string name;
	int next[2];
};

#define DIM 10000
Node b[DIM];
int ptr = 0;

int newnode(double p) {
	++ptr;
	b[ptr].p = p;
	b[ptr].next[0] = b[ptr].next[1] = 0;
	b[ptr].name = "";
	return ptr;
}

int look;

string s;

void skip() {
	while(s[look] == ' ' || s[look] == '\n') ++look;
}


int maketree() {
	skip();
	++look; // (
	string u;
	skip();
	while(s[look] != ' ' && s[look] != '\n' && s[look] != ')') {
		u += s[look];
		++look;
	}
	int v = newnode(sto<double>(u));
	skip();
	if(s[look] == ')') {
		++look;
		return v;
	}
	else {
		skip();
		u = "";
		while(s[look] != ' ' && s[look] != '\n') {
			u += s[look];
			++look;
		}
		b[v].name = u;
		b[v].next[0] = maketree();
		b[v].next[1] = maketree();
		skip();
		++look;
		return v;
	}

}

double f(int v, const set<string> &r) {
	if(b[v].name == "") return b[v].p;
	if(r.count(b[v].name) > 0) {
		return b[v].p * f(b[v].next[0] , r);
	}
	else {
		return b[v].p * f(b[v].next[1] , r);
	}
}

int main() {
	//freopen("1.txt","r",stdin);
	freopen("a-large.in","r",stdin);
	freopen("a-large.out","w",stdout);

	char buf[1024];
	int tc;
	gets(buf);
	tc = sto<int>(buf);
	
	FOR(ttt,1,tc+1) {
		printf("Case #%d:\n",ttt);
		gets(buf);
		int l = sto<int>(buf);
		s = "";
		REP(i,l) {
			gets(buf);
			s += (string(buf)+" ");
		}
		
		ptr = 0;
		look = 0;
		int root = maketree();

		gets(buf);
		int n = sto<int>(buf);
		REP(i,n) {
			gets(buf);
			vector<string> a = s2v<string>(buf);
			string name = a[0];
			int k = sto<int>(a[1]);
			set<string> r;
			REP(j,k) {
				r.insert(a[j+2]);
			}
			double ans = f(root, r);
			printf("%.7lf\n", ans);
		}
	}
	return 0;
}