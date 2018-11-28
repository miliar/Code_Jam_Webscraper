#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define V(a) vector<a>
#define fori(i, n) for(int i=0;i<n;i++)
#define rep(i, a, b) for(int i=a;i<=b;i++)
#define forv(i, a) for(int i=0;i<a.size(); i++)
#define fill(a) memset(a, 0, sizeof(a));
#define fill1(a) memset(a, -1, sizeof(a));
#define LL long long
#define PB push_back
#define SZ(x) (x.size())


vector<string> split( const string& s, const string& delim =" " ) { vector<string> res; string t; for ( int i = 0 ; i != s.size() ; i++ ) { if ( delim.find( s[i] ) != string::npos ) { if ( !t.empty() ) { res.push_back( t ); t = ""; } } else { t += s[i]; }  } if ( !t.empty() ) {  res.push_back(t); } return res; }
vector<int> splitInt( const string& s, const string& delim =" " ) { vector<string> tok = split( s, delim ); vector<int> res; for ( int i = 0 ; i != tok.size(); i++ ) res.push_back( atoi( tok[i].c_str() ) ); return res; }
template<class T> T tok(string s) {	T a; stringstream ss(s); ss>>a; return a; };
template<class T> string str(T a) {	ostringstream ss; ss<<a; return ss.str();};

int stest, n, k;
char s[1003];
char s1[1003];
int f[100];
const int inf = 10000;
int cal(){
	char cur = 0;
	int d=0;
	fori(e,n)if(cur!=s1[e]){
		d++;
		cur=s1[e];
	}
	return d;
}

void go(char*s, char* s1){
	fori(i,k)s1[i]=s[f[i]];
}

void test(){
	fori(v,n/k){
		int e=v*k;
		go(s+e, s1+e);
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &stest);
	rep(ee,1, stest){
		scanf("%d", &k);
		scanf("%s", s);
		n=strlen(s);
		fori(i, k) f[i]=i;
		int res =inf;
		do{
			test();
			res<?=cal();
		}while(next_permutation(f, f+k));
		printf("Case #%d: %d\n", ee, res);
	}
	
	return 0;
}
