#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <map>
using namespace std;
const int M = 210;
const int inf = 1000000000;
const double eps = 1e-10;

struct Noded{
	double dis;
	int man;
};
struct Node{
	Noded tp[M];
}da, db;
int n, m;
bool find(double &star, Noded t, double mid){
	star += m;
	double ll = m*(t.man-1);
	double diss;
	if(t.dis-mid >= star){
		if(ll - mid  <= 0){
			star = t.dis - mid + ll;
			return true;
		}else{
			diss = ll - mid;
			if(diss <= mid){
				star = diss+ t.dis; return true;
			}else return false;
		}
	}else if(t.dis >= star){
		double lef = t.dis - star;
		if(ll - lef <= 0){
			star = t.dis - lef + ll; return true;
		}else{
			diss = ll - lef;
			if(diss <= mid){
				star = diss + t.dis; return true;
			}else return false;
		}
	}
	else{
		diss = star - t.dis;
		diss += ll;
		if(diss <= mid){
			star = t.dis + diss; return true;
		}else return false;
	}
}
bool judge(double mid){
	
	int i;
	double fro = -inf;
	for(i = 0; i < n; i ++){
		bool flag = find(fro, da.tp[i], mid);
		if(!flag ) {
			return false;
		}
	}
	return true;
}
bool cmp(const Noded &a, const Noded &b){
	return a.dis < b.dis;
}
double solve(){
	scanf ("%d%d", &n, &m);
	int i, x;
	for(i = 0; i < n ; i ++){
		scanf ("%lf%d",  &da.tp[i].dis, &da.tp[i].man);
	}
	sort(da.tp, da.tp+n, cmp);
	double lef = 0, rig = inf, mid;
	while(lef +eps < rig){
		mid = (lef + rig)*0.5;
		if(judge(mid)){
			rig = mid-eps;
		}else lef = mid + eps;
	}
	return rig+eps;
}
int main()
{
	int cas;
	int i;
	freopen("B-small-attempt2.in","r", stdin);
	freopen("B.out","w", stdout);
	scanf ("%d", &cas);

	for(i = 1; i <= cas; i ++){
		printf ("Case #%d: %.10lf\n", i,solve());
		
	}
	return 0;
}