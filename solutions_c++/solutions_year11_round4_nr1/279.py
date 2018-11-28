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

double l,s,r,t;
int n,idx[1111111];
double x[1111111],y[1111111],z[1111111];

bool cmp(const int &p1,const int &p2){
	return x[p1]<x[p2];
}

vector<pair<double,double> > X;

void work(){
	cin >> l >> s >> r >> t >> n;
	for (int i=0;i<n;i++){
		scanf("%lf%lf%lf",&x[i],&y[i],&z[i]);
		idx[i]=i;
	}
	sort(idx,idx+n,cmp);
	double prev=0;
	X.clear();
	for (int i=0;i<n;i++){
		//cout << idx[i] <<" "<< x[idx[i]] <<" " << y[idx[i]] << endl;
		X.push_back(make_pair(s,x[idx[i]]-prev));
		X.push_back(make_pair(s+z[idx[i]],y[idx[i]]-x[idx[i]]));
		prev=y[idx[i]];
	}
	X.push_back(make_pair(s,l-prev));
	sort(X.begin(),X.end());
	double ret=0;
	for (int i=0;i<X.size();i++){
		if (t<=1e-8){
			ret+=X[i].second/X[i].first;
		}else if (t>=X[i].second/(X[i].first-s+r)){
			t-=X[i].second/(X[i].first-s+r);
			ret+=X[i].second/(X[i].first-s+r);
		}else {
			ret+=t+(X[i].second-(X[i].first-s+r)*t)/(X[i].first);
			t=0;
		}
	}
	printf("%.12lf\n",ret);
}

int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t;cin >> t;
	for (int i=1;i<=t;i++){
		cout << "Case #"<< i << ":" <<" ";
		work();
	}
	//system("pause");
	return 0;
}
/*
2
3
.10
0.1
10.
4
.11.
0.00
01.1
.10.
*/

