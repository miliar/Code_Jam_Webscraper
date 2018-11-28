#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int w,l, n;
pair<int, int> r[1000];
pair<int, int> ans[1000];
pair<pair<int, int>, int> p[100500];
int mxp=0;

void solve(){
	cin>>n;
	cin>>w>>l;
	for (int i=0; i<n; ++i)
		cin>>r[i].first, r[i].second=i;
	sort(r, r+n);
	reverse(r, r+n);
	mxp=1;
	p[0]=make_pair(make_pair(0, l), 0);
	for (int i=0; i<n; ++i){
		for (int j=0; j<mxp; ++j){
			if (p[j].first.second - p[j].first.first<0 || p[j].first.first!=0 && p[j].first.first+r[i].first>l || p[j].first.second-p[j].first.first<2*r[i].first && p[j].first.first!=0 && p[j].first.second!=l || p[j].second+2*r[i].first>w && p[j].second!=0)
				continue;
			if (p[j].first.first==0){
				p[mxp].first=make_pair(r[i].first, p[j].first.second);
				p[mxp].second=p[j].second;
				p[j].second+=2*r[i].first;
				p[j].first.second=r[i].first;
				ans[r[i].second]=make_pair(p[mxp].second+r[i].first, 0);
				if (p[j].second == 2*r[i].first)
					p[j].second = r[i].first, ans[r[i].second].first=0;
				mxp++;
				sort(p, p+mxp);
				goto l;
			}
			p[mxp].first=make_pair(p[j].first.first+2*r[i].first, p[j].first.second);
			p[mxp].second=p[j].second;
			p[j].second+=2*r[i].first;
			p[j].first.second=p[j].first.first+2*r[i].first;
			ans[r[i].second]=make_pair(p[mxp].second+r[i].first, p[j].first.first+r[i].first);
			if (p[j].second == 2*r[i].first)
				p[j].second = r[i].first, ans[r[i].second].first=0;
			mxp++;
			sort(p, p+mxp);
			goto l;
		}
		return;
		l:;
	}
	for (int i=0;i<n; ++i)
		swap(r[i].first, r[i].second);
	sort(r, r+n);
	for (int i=0; i<n; ++i){
		if (ans[i].first<0 || ans[i].first>w || ans[i].second<0 || ans[i].second>l) return;
		for (int j=i+1; j<n; ++j)
			if (max(abs(ans[i].second-ans[j].second), abs(ans[i].first-ans[j].first))<r[i].second+r[j].second)
				return;
	}
	for (int i=0; i<n; ++i)
		cout<<ans[i].first<<' '<<ans[i].second<<' ';
}

int main(){
	freopen("input.txt","r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin>>t;
	for (int i=1; i<=t; ++i){
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<endl;
		cerr<<i<<endl;
	}
}