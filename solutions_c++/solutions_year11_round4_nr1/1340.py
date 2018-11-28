#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define MAX 300005

vector<pair<int,int> > li;

int main(){
	int u,T,x,s,r,n,i,walk,a,b,w;
	double t,runt,mint;
	cin>>T;
	for (u=0; u<T; u++){
		li.clear();
		cin>>x>>s>>r>>t>>n;
		walk=x;
		for(i=0; i<n; i++){
			cin>>a>>b>>w;
			walk-=(b-a);
			li.push_back(make_pair(w,b-a));
		}
		li.push_back(make_pair(0,walk));
		//for (i=0; i<n; i++) cout<<li[i].first<<","<<li[i].second<<endl;
		sort(li.begin(),li.end());
		mint=0;
		for (i=0; i<li.size(); i++){
			runt=min(t,(double)(li[i].second)/(li[i].first+r));	
			mint+=runt+(li[i].second-(li[i].first+r)*runt)/(li[i].first+s);
			t-=runt;
		}
		printf("Case #%d: %.9lf\n", u+1, mint);
	}
	return 0;
}
