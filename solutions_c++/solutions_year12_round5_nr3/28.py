#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

long long m;
long long f;
int n;
pair<long long, long long> p[200];

long long check(long long v){
	long long d=m-f*v;
	long long ans=0;
	long long last=-1;
	for (int i=0; i<n; ++i){
		if (p[i].second<=last) continue;
		if (d>=(p[i].second-last)*p[i].first*v){
			ans+=(p[i].second-last)*v;
			d-=(p[i].second-last)*p[i].first*v;
		}
		else{
			ans+=d/p[i].first;
			break;
		}
		last=p[i].second;
	}
	return ans;
}

void solve(){
	cin>>m>>f>>n;
	for (int i=0; i<n; ++i){
		cin>>p[i].first>>p[i].second;
	}
	sort(p, p+n);
	long long l=1, r=m/f, f1, f2;
	while (r-l>10){
		f1=(2*l+r)/3;
		f2=(l+2*r)/3;
		if (check(f1)>check(f2))
			r=f2;
		else
			l=f1;
	}
	long long bestans=0;
	for (long long i=l; i<=r; ++i)
		bestans=max(bestans, check(i));
	cout<<bestans<<endl;
}

int main(){
	freopen("input.txt", "r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	for (int i=0; i<t; ++i){
		cout<<"Case #"<<i+1<<": ";
		solve();
	}
}