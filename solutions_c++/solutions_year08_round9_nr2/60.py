#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker,"/STACK:64000000")

#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <cctype>
#include <cassert>

using namespace std; 

#define sz(v) ((int) (v).size())
#define all(v) (v).begin(), (v).end()
#define mp make_pair
#define pb push_back

typedef double D;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> ii;

template<typename T> T abs(T x) { return x>0 ? x : -x; }
template<typename T> T sqr(T x) { return x*x;          }

ll w,h,x,y,dx1,dy1,dx2,dy2;

bool norm(ll x, ll y) {
	return x>=0 && y>=0 && x<w && y<h;
}

const ll max_s=3*1000*1000;

void getRange(ll x, ll len, ll dx, ll &l, ll &r) {
	if (dx==0) {
		if (0<=x && x<len) {
			r=1<<22;
			l=-r;
		}
		else {
			l=1<<22;
			r=-l;
		}
		return;
	}
	if (dx<0) {
		dx=-dx;
		x=len-1-x;
	}
	if (x>=len) {
		l=1<<22;
		r=-l;
		return;
	}
	r=(len-x-1)/dx;
	if (x>=0) {
		l=0; 
		return;
	}
	l=(-x)/dx;
	if (x+l*dx<0) l++;
}

ll gcd(ll a, ll b) {
	if (a==0) return b;
	return gcd(b%a,a);
}

ll solve2() {
	ll g=gcd(abs(dx1),abs(dx2));
	ll res=0;
	for (ll xx=0; xx<w; xx++) {
		if (xx%g) continue;
		double t=double(xx-x)/double(dx1);
		double yy=double(y)+t*double(dy1);
		if (yy>1e-2 && yy<h-1-1e-2)
			res++;
	}
	return res;
}

bool used[100][100];

ll solve() {
	memset(used,false,sizeof(used));
	queue<ii> q;
	used[x][y]=true;
	q.push(mp(x,y));
	while (!q.empty()) {
		ii p=q.front();
		q.pop();
		int x=p.first, y=p.second;
		if (norm(x+dx1,y+dy1) && !used[x+dx1][y+dy1]) {
			used[x+dx1][y+dy1]=true;
			q.push(mp(x+dx1,y+dy1));
		}
		if (norm(x+dx2,y+dy2) && !used[x+dx2][y+dy2]) {
			used[x+dx2][y+dy2]=true;
			q.push(mp(x+dx2,y+dy2));
		}
	}
	int res=0;
	for (int i=0; i<w; i++)
		for (int j=0; j<h; j++)
			if (used[i][j])
				res++;
	return res;
}

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	int tn;
	cin>>tn;
	for (int tst=0; tst<tn; tst++) {
		cerr<<tst<<endl;
		printf("Case #%d: ",tst+1);
		cin>>w>>h;
		cin>>dx1>>dy1>>dx2>>dy2;
		cin>>x>>y;
		cout<<solve()<<endl;
	}

	return 0;
}
