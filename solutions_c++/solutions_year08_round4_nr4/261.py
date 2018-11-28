// By mirosuaf v.2.1 modified for CodeJam
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(f,w) ({ bool _ok=true; f _ok=_ok && (w); _ok; })
#define EXISTS(f,w) (!ALL(f,!(w)))
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI; 

string change(string s, vector<int> v) {
    int II=s.size()/v.size();
    
    string ans="";
    REP(i,II) {
	REP(j,v.size()) {
	    ans+=s[i*v.size()+v[j]];
	    }
	}    
    return ans;
    }


int main() {
int ile;
scanf("%d",&ile);
int k;
string s,ss;
char ch[1000];
FOR(iile,1,ile) {
int wynik=INF;
scanf("%d",&k);
scanf("%s",ch);
s=ch;

vector<int> v;
REP(i,k) v.push_back(i);

do {
int wrt=0;
ss=change(s,v);
FOR(i,1,ss.size()-1) if (ss[i]!=ss[i-1]) wrt++;

if (wrt+1<wynik) wynik=wrt+1;

} while (next_permutation(v.begin(),v.end()));



printf("Case #%d: %d\n",iile,wynik);
}
return 0;
}

