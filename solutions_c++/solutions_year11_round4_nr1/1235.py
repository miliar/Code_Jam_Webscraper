#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>
using namespace std;
const int MAXN = 50000;
const double eps = 1e-12;
struct Node{
	int s, e;
	double wi;
}va[MAXN];
double  s, r, t;
int x,n;
bool cmp(const Node &a, const Node &b){
	return a.s < b.s;
}
bool cmb(const Node &a, const Node &b){
	return a.wi < b.wi;
}
bool ZERO(double t){
	return fabs(t) < eps;
}
bool GT(double a, double b){
	return (a > b );
}
bool GEQ(double a, double b){
	return (a > b|| ZERO(a-b) );
}	
double solve(){
	cin >> x >> s >> r >> t >> n;
	int i;
	for(i = 0; i < n; i ++){
		cin >> va[i].s >> va[i].e >> va[i].wi;
	}
	sort(va, va+n, cmp);
	int j = n;
	if(va[0].s != 0){
		va[j].s = 0;
		va[j].wi = 0;
		va[j].e = va[0].s; j ++;
	}
	if(va[n-1].e != x){
		va[j].e = x;
		va[j].s = va[n-1].e;
		va[j].wi = 0;
		j ++;
	}
	for(i = 1; i < n; i ++){
		if(va[i].s != va[i-1].e){
			va[j].s = va[i-1].e;
			va[j].e = va[i].s;
			va[j].wi = 0;
			j ++;
		}
	}
	n = j;
	sort(va, va+n, cmb);
	double tim = 0;
	double tt;
	double dis;
	for(i = 0; i < n; i ++){
		if(GT(t,0)){
			dis = va[i].e  - va[i].s;
			tt = dis / (va[i].wi + r);
			if(GEQ(t, tt)){
				tim += tt;
				t -= tt;
			}else{
				tim += t;
				dis -= t * (va[i].wi + r);
				tim += dis / (va[i].wi + s);
				t = -1;
			}
		}else{
			dis = va[i].e  - va[i].s;
			tim += dis /(va[i].wi + s);
		}
	}
	return tim;
}
int main(){
	int cas;
	freopen("A-large.in","r", stdin);
	freopen("A-large.out","w", stdout);
	cin >> cas;
	int i;
	for(i = 1; i <= cas; i ++){
		double outt = solve();
		printf ("Case #%d: %.10lf\n", i,outt);
	}
	return 0;
}