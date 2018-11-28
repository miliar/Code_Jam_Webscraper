#include <string>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <stack>
#include <queue>
#include <algorithm>
#include <deque>
#include <utility>
#include <sstream>
#include <vector>
#include <map>
#include <ctime>
#include <set>
using namespace std;
#define sz size()
#define vi vector<int>
#define vs vector<string>
#define dsz size()-1
#define pb push_back
#define maxn(a,b) (a) = ((a) < (b) ? (b) : (a))
#define FUP(ii,ss,ff) for ((ii) = (ss);(ii) <= (ff);(ii)++)
#define FDOWN(ii,ss,ff) for ((ii) = (ss);(ii) >= (ff);(ii)--)
#define FALL(ii, vv) for ((ii) = 0;signed (ii) <= signed ((vv).dsz);(ii)++)
#define ITERATE(__it,__container) for(__it=__container.begin(); __it!=__container.end(); __it++)
#define EPS 1e-12
#define INF 2147483647
#define sgn(x) ((x)>0 ? 1 : (x)==0 ? 0 : -1)
#define sq(x) ((x)*(x))
#define sorta(a) sort(a.begin(), a.end())
#define cleara(a, b) memset(a, b, sizeof(a))
#define ALL(a) a.begin(), a.end()
#define absd(a) ((a)<0?-(a):(a))
#define absm absd
#define mp make_pair
typedef unsigned int uint;
typedef long long ll;

vector<string> split(const string& s, const string& delim ){
	std::vector<string> res;
	std::string t;
	int i;
	FALL(i,s){
		if (delim.find(s[i])!=std::string::npos){
			if (!t.empty()){
				res.push_back(t); 
				t=""; }}
		else t+=s[i];}
	if (!t.empty()) res.push_back(t);
	return res;}

struct tr {
	map<string, tr> chl;
};

int ret;
char ts[1000];

int main() {
	int t, i, T, n, m, j;
	scanf("%d", &t);
	FUP(T,1,t) {
		ret = 0;
		scanf("%d%d", &n, &m);
		tr root;
		FUP(i,0,n+m-1) {
			if (i == n) {
				ret = 0;
			}
			scanf("%s", ts);
			vs r = split(ts, "/");
			tr* c = &root;
			FALL(j,r) {
				if (!c->chl.count(r[j])) {
					ret++;
					c->chl[r[j]] = tr();
				}
				c = &c->chl[r[j]];
			}
		}
		printf("Case #%d: %d\n", T, ret);
	}
	return 0;
}