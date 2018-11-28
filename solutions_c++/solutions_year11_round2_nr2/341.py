#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_##i=(b);i<_##i;++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define MP          make_pair
#define S           size()
typedef long long   LL;

vector<double> v;
int c;

bool oki(double x, double d){
	double ulti = v[0]-x+d;
	FOR(i, 1, c){
		if(v[i] > ulti){
			double aux = v[i]-x;
			if(aux < ulti) ulti += d;
			else ulti = aux+d;
		}
		else{
			double aux = v[i]+x;
			if(ulti > aux) return false;
			else ulti += d;
		}
	}
	return true;
}

void solve(){
	int V;
	double P, d;
	cin>>c>>d;
	v = vector<double>();
	F(i, c){
		cin>>P>>V;
		F(j, V) v.PB(P);
	}
	c = v.S;
	sort(ALL(v));
	double a = 0.0, b = 6000000000000.0;
	while(b-a > 1e-3){
		double mid = double(LL(a)+LL(b))/2.0;
		if(oki(mid, d)) b = mid;
		else a = mid + 0.5;
	}
	printf("%.7lf\n", a);
}

int main(){
	//freopen("a.in", "r", stdin);
	//freopen("B-small-attempt0.in","r",stdin); freopen("B-small-attempt0.out","w",stdout);
	freopen("B-large.in","r",stdin); freopen("B-large.out","w",stdout);
	int t;
	scanf("%d", &t);
	for(int cas=1; cas<=t ;cas++){
		printf("Case #%d: ", cas);
		solve();
	}
}

