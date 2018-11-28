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
#define REVERSE(x) reverse((x).begin(), (x).end())

int bc(ll m){
	return !m? 0 : 1 + bc(m & (m - 1)); 
}

ll gcd(ll a, ll b){
	if(b > a)return gcd(b,a);
	if(a% b == 0)return b;
	return gcd(a%b, b);
}

int dx[4][2] = {{0,-1}, {-1,0}, {0,1}, {1,0}};

int main(){
	int cases; cin >> cases;
	FOR(T,1,cases+1){
		cout << "Case #" << T << ": " ;
	       	ll n,m,a; cin >> n >> m >> a;
		bool found = false;
		FOR(x1,-n,1)FOR(y1,0,m+1)FOR(y2,0,m+1){
			FOR(x2, x1, x1+n+1){
				if(x1*y2 - x2*y1 == a || x1*y2 - x2*y1 == -a){
					cout << -x1 << " " << 0 << " " <<  0 << " " <<  y1 << " " <<  x2 - x1 << " " <<  y2 << endl;
					found = true;
					goto here;	
				}
			}
		}
here:		;

		if(!found)cout << "IMPOSSIBLE" << endl;	
	}
}


