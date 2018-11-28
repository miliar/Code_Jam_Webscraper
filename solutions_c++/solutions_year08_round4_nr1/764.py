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
#define INF 20000000
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

VI g[10010];

int dx[4][2] = {{0,-1}, {-1,0}, {0,1}, {1,0}};


int gate[10010], change[10010], value[10010];
int fc[10010][2];


int f(int r, int v){
	if(value[r] != -1)return value[r] == v? 0: INF;
	if(fc[r][v] !=-1)return fc[r][v];
	int ret = INF;
	if(v){
		if(gate[r]){
			ret <?= f(2*r, 1) + f(2*r + 1, 1);
			if(change[r]){
				ret <?= f(2*r, 0) + f(2*r + 1, 1) + 1;
				ret <?= f(2*r + 1, 0) + f(2*r, 1) + 1;
				ret <?= f(2*r , 1) + f(2*r + 1, 1) + 1;
			}
		}
		else{
			ret <?= f(2*r, 0) + f(2*r + 1, 1);
			ret <?= f(2*r + 1, 0) + f(2*r, 1) ;
			ret <?= f(2*r , 1) + f(2*r + 1, 1);
			if(change[r]){
			     ret <?= f(2*r, 1) + f(2*r + 1, 1) + 1;  	
			}	       
		}	
	}
	else{
		if(!gate[r]){
			ret <?= f(2*r, 0) + f(2*r + 1, 0);
			if(change[r]){
				ret <?= f(2*r, 0) + f(2*r + 1, 1) + 1;
				ret <?= f(2*r + 1, 0) + f(2*r, 1) + 1;
				ret <?= f(2*r , 0) + f(2*r + 1, 0) + 1;
			}
		}
		else{
			ret <?= f(2*r, 0) + f(2*r + 1, 1);
			ret <?= f(2*r + 1, 0) + f(2*r, 1) ;
			ret <?= f(2*r , 0) + f(2*r + 1, 0);
			if(change[r]){
			     ret <?= f(2*r, 0) + f(2*r + 1, 0) + 1;  	
			}	       
		}
	}
	return fc[r][v] = ret;	
}


int main(){
	int cases; cin >> cases;
	FOR(T,1,cases+1){
		cout << "Case #" << T << ": ";
	       	int n, v; cin >> n >> v;
		memset(value, -1, sizeof(value));
		memset(fc, -1, sizeof(fc));
		FOR(i,0,(n-1)/2){
			int g, c;
			cin >> gate[i+1] >> change[i+1];
		}
		FOR(i,(n-1)/2, n){
			cin >> value[i+1];
		}
		int res = f(1,v);
		if(res >= INF){
			cout << "IMPOSSIBLE" << endl;
		}
		else cout << res << endl;
			
	}
}


