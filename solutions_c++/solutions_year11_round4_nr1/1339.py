#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <queue>
#include <memory.h>
#include <stack>

using namespace std;

#define pb push_back
#define mp make_pair
#define fir first
#define fi first
#define sec second
typedef long long int64;
typedef long double ld;

const int inf=2000000000;
const ld eps=1e-07;

ld x,s,r,l;
int n;
ld ans;
vector <pair <ld,ld> > a;
set < pair <ld,int> > prof;

ld getprof(ld l,int i){
	if (l>=a[i].first/(a[i].second+r))
		return a[i].first/(a[i].second+r)-a[i].first/(a[i].second+s);
	else return (l+(a[i].first-l*(a[i].second+r))/(a[i].second+s))-a[i].first/(a[i].second+s);
}

void noprof(int i){
	if (l>=a[i].sec/(a[i].fir+r)){
		ans+=a[i].sec/(a[i].fir+r);
		l-=a[i].sec/(a[i].fir+r);
	}
	else {
		ans+=(l+(a[i].sec-l*(a[i].fir+r))/(a[i].fir+s));
		l=0;
	}
}

int main(){
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif
	int z;
	scanf("%d",&z);
	for (int t=1;t<=z;++t){
		cin>>x>>s>>r>>l>>n;
		a.clear();
		for (int i=0;i<n;++i){
			int l,r,v;
			scanf("%d %d %d",&l,&r,&v);
			a.pb(mp(v,r-l));
			x-=r-l;
		}
		if (x>0)
			a.pb(mp(0,x));
		ans=0;
		sort(a.begin(),a.end());
		for (int i=0;i<a.size();++i)
			noprof(i);
		/*for (int i=0;i<a.size();++i)
			prof.insert(mp(getprof(l,i),i));
		
		while (!prof.empty()){
			pair <ld,int> ab=*prof.begin();
			if (abs(getprof(l,ab.second)-ab.first)>eps){
				prof.erase(prof.begin());
				prof.insert(mp(getprof(l,ab.second),ab.second));
			}
			else {
				prof.erase(prof.begin());
				noprof(ab.second);
			}
		}*/
		cout.precision(8);
		printf("Case #%d: ",t);
		cout<<fixed<<ans<<endl;
	}
	return 0;
}