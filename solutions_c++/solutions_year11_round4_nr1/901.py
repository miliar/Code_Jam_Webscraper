#include <iostream>
#include <vector>
#include <set>
#include <iomanip>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <map>
#include <assert.h>
#include <cmath>
#include <queue>
#include <stack>
using namespace std;

#define For(i,a,b) for(int i=a;i<b;i++)
#define rep(i,x) For(i,0,x)
#define foreach(i,c) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); ++i)

#define mp make_pair
#define pb push_back
#define sz(x) int((x).size())
#define TWO(x) (1<<(x))
#define F first
#define S second
#define setmax(a,b) a = max(a,b)
#define setmin(a,b) a = min(a,b)

typedef vector<int> Vi;
typedef vector<Vi> Vvi;
typedef pair<int,int> Pii;

typedef pair<int,int> Pii;
typedef vector<Pii> Vpii;
typedef vector<Vpii> Vvpii;
typedef long long ll;

struct Int{
	int begin, end;
	double speed;
	Int(int b, int e, double s){
		begin = b, end = e, speed = s;
	}
	Int(){}
	bool operator<(const Int& in) const{
		return begin < in.begin;
	}
};

bool comp2(Int a, Int b){
	return a.speed < b.speed;
}

int main(){
int np; cin>>np;
rep(tp,np){
	int X; double S, R, t; int n;
	cin>>X>>S>>R>>t>>n;
	Int V[n];
	rep(i,n) cin>>V[i].begin>>V[i].end>>V[i].speed;
	sort(&V[0], &V[n]);
	int last = 0;
	vector<Int> VV;
	rep(i, n){
		if(V[i].begin != last){
			VV.pb(Int(last, V[i].begin, 0));
		}
		VV.pb(V[i]);
		last = V[i].end;
	}
	if(last != X) VV.pb(Int(last, X, 0));
	double res = 0.0;
	sort(VV.begin(), VV.end(), comp2);
	foreach(it, VV){
		double len = it->end - it->begin;
		double speed = it->speed;

		double runtime = min(len/(R+speed), t);
		res += runtime;
		t -= runtime;
		res += (len - runtime*(R+speed))/(S+speed);
	}
	printf("Case #%d: %.06f\n", tp+1, res);
}
}
