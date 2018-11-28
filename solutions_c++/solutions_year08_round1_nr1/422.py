/*
	Author : Vinay Emani
	Contact : VinayEmani AT gmail DOT com
*/
#include <iostream>
#include <cstring>
#include <string>
#include <sstream>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <utility>
using namespace std;
#define lint long long
#define SZ(s) ((int)(s.size()))
#define PB push_back
#define MP make_pair
#define FORN(i,a,b) for(i=(int)(a);i<(int)(b);i++)
#define FOR(i,n) FORN(i,0,n)
#define FOREACH(it,S) for(typeof(S.begin()) it = S.begin();it != S.end();it++)
#define SET(x,a) memset(x,a,sizeof x)
#define BEG(a) a.begin()
#define END(a) a.end()
#define ALL(a) BEG(a),END(a)

lint x[1024],y[1024];
int n;
int main(){
	int cas,t=0;
	cin >> cas;
	while(cas--){
		t++;
		cin >> n;int i;
		FOR(i,n)cin >> x[i];
		FOR(i,n)cin >> y[i];
		sort(x,x+n);sort(y,y+n);
		lint ans=0;
		FOR(i,n)ans+=x[i]*y[n-1-i];
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
