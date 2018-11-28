#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cassert>
#include <cmath>

using namespace std;

#define Eo(x) { cerr << #x << " = " << (x) << endl; }

typedef long long int64;
typedef double real;

static const int inf = 0x3f3f3f3f;
static const real eps = 1e-6;

const int maxn = 64;

struct pp{
	int x,y,r;
} a[maxn];

char was[maxn];

real sq(real k){
	return k*k;
}

inline real mabs(real k){
	return abs(k);
}

typedef pair<real,real> prr;
vector<prr> solve(real x1, real x2, real y1, real y2, real r1, real r2, real r){
	vector<prr> res;
	real xa = 2*(x2-x1);
	real ya = 2*(y2-y1);
	real c = sq(r-r1)-sq(r-r2)+sq(x2)-sq(x1)+sq(y2)-sq(y1);
	if (mabs(ya) < eps){
		assert(mabs(xa) > eps);
		c /= xa;
		real xx = c;
		real dy = sq(r-r1)-sq(xx-x1);
		real yyy1 = sqrt(dy);
		real yy1 = y1 + yyy1;
		real yy2 = y1 - yyy1;
		res.push_back(prr(xx,yy1));
		res.push_back(prr(xx,yy2));
	} else if (mabs(xa) < eps){
		assert(mabs(ya) > eps);
		c /= ya;
		real yy = c;
		real dx = sq(r-r1)-sq(yy-y1);
		real xxx1 = sqrt(dx);
		real xx1 = x1 + xxx1;
		real xx2 = x1 - xxx1;
		res.push_back(prr(xx1,yy));
		res.push_back(prr(xx2,yy));
	} else {
		ya /= xa;
		c /= xa;

		real aa = sq(ya)+1;
		real bb = c*ya-x1*ya+y1;
		real cc = c*c-2*x1*c+x1*x1+y1*y1-sq(r1-r);
		real dd = bb*bb-aa*cc;
		if (dd < 0) return res;
		if (dd < eps){
			real y = bb / aa;
			real x = c-ya*y;
			res.push_back(prr(x,y));
		} else {
			real yy1 = (bb - sqrt(dd))/aa;
			real yy2 = (bb + sqrt(dd))/aa;
			real xx1 = c - ya*yy1;
			real xx2 = c - ya*yy2;
			res.push_back(prr(xx1,yy1));
			res.push_back(prr(xx2,yy2));
		}
	}
	return res;
}

int n;

bool can(real r){
	if (n == 1){
		return r >= a[0].r;
	}
	if (n == 2){
		return r >= a[0].r && r >= a[1].r;
	}
	for (int i = 0; i < 3; i++){
		if (r < a[i].r) return false;
	}
	for (int i = 0; i < 3; i++){
		for (int j = i+1; j < 3; j++){
			real dd = sqrt(sq(a[i].x-a[j].x)+sq(a[i].y-a[j].y))+a[i].r + a[j].r;
			dd *= 0.5;
			if (r < dd) continue;
			return true;
		}
	}
	return false;
}

int main(){
	int T; cin >> T;
	for (int _ = 0; _ < T; _++){
		cin >> n;
		for (int i = 0; i < n; i++){
			scanf("%d%d%d",&a[i].x,&a[i].y,&a[i].r);
		}
		real l = 0;
		real r = inf;
		while (r-l > eps){
			real m = (r+l)*0.5;
			if (can(m)){
				r = m;
			} else{
				l = m;
			}
		}
		printf("Case #%d: %.6lf\n",_+1,l);
	}
	return 0;
}
