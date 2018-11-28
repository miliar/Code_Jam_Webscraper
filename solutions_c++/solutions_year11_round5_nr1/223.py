#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <iterator>
#include <bitset>
#include <sstream>
#include <cmath>
#include <cstring>

using namespace std;

double w;
int u,d,g;
double ux[111],uy[111],dx[111],dy[111];

double operator ^(pair<double,double> a,pair<double,double> b){
	return a.first*b.second-a.second*b.first;
}

double calc_area(vector<pair<double,double> > v){
	double ret=0;
	for (int i=0;i<v.size();i++){
		int nxt=(i+1)%v.size();
		ret+=v[i]^v[nxt];
	}
	return fabs(ret);
}

double req;

pair<double,double> calc_point(pair<double,double> a,pair<double,double> b,double pos){
	return make_pair(pos,a.second+(a.second-b.second)/(a.first-b.first)*(pos-a.first));
}

bool check(double L,double R){
	vector<pair<double,double> > v;v.clear();
	for (int i=0;i<u;i++){
		if (i+1<u&&ux[i]<=L&&ux[i+1]>=L){
			v.push_back(calc_point(make_pair(ux[i],uy[i]),make_pair(ux[i+1],uy[i+1]),L));
		}
		if (ux[i]>=L&&ux[i]<=R){
			v.push_back(make_pair(ux[i],uy[i]));
		}
		
		if (i+1<u&&ux[i]<=R&&ux[i+1]>=R){
			v.push_back(calc_point(make_pair(ux[i],uy[i]),make_pair(ux[i+1],uy[i+1]),R));
		}
	}
	
	for (int i=d-1;i>=0;i--){
		if (i+1<d&&dx[i]<=R&&dx[i+1]>=R){
			v.push_back(calc_point(make_pair(dx[i],dy[i]),make_pair(dx[i+1],dy[i+1]),R));
		}
		if (dx[i]>=L&&dx[i]<=R){
			v.push_back(make_pair(dx[i],dy[i]));
			continue;
		}
		
		if (i+1<d&&dx[i]<=L&&dx[i+1]>=L){
			v.push_back(calc_point(make_pair(dx[i],dy[i]),make_pair(dx[i+1],dy[i+1]),L));
		}
	}
	//cout << L <<" "<< R <<" "<< calc_area(v) <<" "<< req <<endl;
	//for (int i=0;i<v.size();i++)
	//	cout << v[i].first <<" " << v[i].second <<endl;
	return (calc_area(v)>=req);
}

void work(){
	cin >> w >> u >> d >> g;
	for (int i=0;i<u;i++)
		cin >> ux[i]>> uy[i];
	for (int i=0;i<d;i++)
		cin >> dx[i]>> dy[i];
	vector<pair<double,double> > v;v.clear();
	for (int i=0;i<u;i++) v.push_back(make_pair(ux[i],uy[i]));
	for (int i=d-1;i>=0;i--) v.push_back(make_pair(dx[i],dy[i]));
	double tot=calc_area(v);
	req=tot/double(g);
	double cur=0;
	for (int i=0;i<g-1;i++){
		double lo=cur,hi=w;
		for (int rt=0;rt<200;rt++){
			double mid=(lo+hi)/2;
			if (check(cur,mid)) hi=mid;
			else lo=mid;
		}
		printf("%.10lf\n",lo);
		cur=lo;
	}
}

int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t;cin >> t;
	for (int i=1;i<=t;i++){
		cout << "Case #"<< i << ":" <<endl;
		work();
	}
	//system("pause");
	return 0;
}
/*
2
15 3 3 3
0 6
10 8
15 9
0 10
5 11
15 13
8 3 4 2
0 2
5 4
8 3
0 5
3 4
4 7
8 5
*/
