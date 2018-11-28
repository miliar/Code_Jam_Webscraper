#include <cstdio>
#include <vector>
#include <sstream>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <map>
#include <algorithm>
#include <set>
#include <cmath>
#include <queue>



using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FRR(i,a,b) for(int i=b-1;i>=0;i--)
#define VI vector<int>
#define VVI vector< VI >
#define VS vector<string>
#define pii pair<int, int>
#define INF 2000000000
#define sz size()
#define pb push_back
#define mp make_pair
#define ll long long int
#define eps 1e-9
#define print(v,n) {FOR(i,0,n)cout<<v[i]<<" ";cout<<endl;}
#define SORT(x) sort((x).begin(), (x).end())



int bc(int m){
	return !m? 0: 1 + bc(m & (m - 1));
}

ll gcd(ll a, ll b){
	if(a < b)return gcd(b,a);
	if(a%b == 0)return b;
	return gcd(b, a%b);
}


int main(){
	int cases; cin >> cases;

	FOR(T,1,cases+1){
		int n;
		cin >> n;
		VI x,y;
		FOR(i,0,n){
			int tmp; cin >> tmp; x.pb(tmp);
		}
		FOR(i,0,n){
			int tmp; cin >> tmp; y.pb(tmp);
		}
		SORT(y); SORT(x); reverse(y.begin(), y.end());
		ll ret = 0;
		FOR(i,0,y.sz)ret+= y[i]*x[i];
		cout << "Case #" << T << ": " << ret << endl;
	}
}


