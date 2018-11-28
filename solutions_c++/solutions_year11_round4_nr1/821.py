#include<iostream>
#include<vector>
#include<queue>
#include<set>
#include<cstdio>
#include<algorithm>
#include<string>
#include<map>
#include<cmath>
#include<cstdlib>
#include<ctime>
using namespace std;


bool cmp (pair<int,pair<int,int> > a, pair<int,pair<int,int> > b) {
	return a.second.first<b.second.first;
}

bool cmp2 (pair<int,pair<int,int> > a, pair<int,pair<int,int> > b) {
	return a.first<b.first;
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t; cin >> t;
	for (int z=0;z<t;z++) {
		vector<pair<int,pair<int,int> > > v;
		vector<pair<int,pair<int,int> > > w;
		int X,S,R;
		double T;
		int n;
		cin >> X >> S >> R >> T >> n;
		for (int i=0;i<n;i++) {
			int l,r,wi;
			cin >> l >> r >> wi;
			w.push_back(make_pair(wi,make_pair(l,r)));
		}
		sort(w.begin(),w.end(),cmp);
		int cl=0;
		if (cl<w[0].second.first)
			v.push_back(make_pair(0,make_pair(cl,w[0].second.first)));
		for (int i=0;i<n-1;i++)
			if (w[i].second.second<w[i+1].second.first)
				v.push_back(make_pair(0,make_pair(w[i].second.second,w[i+1].second.first)));
		if (w[n-1].second.second<X)
			v.push_back(make_pair(0,make_pair(w[n-1].second.second,X)));
		for (int i=0;i<n;i++)
			v.push_back(w[i]);
		double res=0.0;
		sort(v.begin(),v.end(),cmp2);
		for (int i=0;i<v.size();i++) {
			if (T>0) {
				double s=v[i].second.second-v[i].second.first;
				double toV=v[i].first+R;
				double toV2=v[i].first+S;
				double time=s/toV;
				if (time>T) {
					res+=T;
					s-=toV*T;
					res+=(s/toV2);
					T=0;
				} else {
					T-=time;
					res+=time;
				}
			} else {
				double s=v[i].second.second-v[i].second.first;
				double toV2=v[i].first+S;
				double time=s/toV2;
				res+=time;
			}
		}
		printf("Case #%d: %.6f\n",z+1,res);
	}
	return 0;
}
