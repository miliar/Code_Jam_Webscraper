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

void solve(){
	int n;
	scanf("%d", &n);
	vector<string> vs(n);
	vector<pair<double,double> > wp(n), owp(n), oowp(n);
	F(i, n){
		cin>>vs[i];
		double a = 0, b = 0;
		F(j, n){
			if(vs[i][j] != '.') b += 1.0;
			if(vs[i][j] == '1') a += 1.0;
		}
		wp[i].first = double(a);
		wp[i].second = double(b);
	}
	F(i, n){
		double a = 0;
		F(j, n){
			double aux = 0.0;
			if(vs[i][j] == '1') aux = (wp[j].first)/(wp[j].second-1.0);
			if(vs[i][j] == '0') aux = (wp[j].first-1.0)/(wp[j].second-1.0);
			a += aux;
		}
		owp[i].first = a;
		owp[i].second = wp[i].second;
		//cout<<a<<" "<<wp[i].second<<endl;
	}
	F(i, n){
		double a = 0;
		F(j, n){
			if(vs[i][j] != '.'){
				a += (owp[j].first/owp[j].second);
			}
		}
		oowp[i].first = a;
		oowp[i].second = wp[i].second;
	}
	F(i, n){
		double r = 0.25*(wp[i].first/wp[i].second);
		r += 0.50*(owp[i].first/owp[i].second);
		r += 0.25*(oowp[i].first/oowp[i].second);
		printf("%.7lf\n", r);
	}
}

int main(){
	//freopen("a.in", "r", stdin);
	//freopen("A-small-attempt0.in","r",stdin); freopen("A-small-attempt0.out","w",stdout);
	freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);
	int t;
	scanf("%d", &t);
	for(int cas=1; cas<=t ;cas++){
		printf("Case #%d:\n", cas);
		solve();
	}
}

