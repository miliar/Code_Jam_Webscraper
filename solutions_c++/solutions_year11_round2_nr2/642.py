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

int n;
int d;
vector <ld> a;
vector <ld> tek;

bool checkans(ld tim){
	tek.clear();
	tek.pb(a[0]-tim);
	for (int i=1;i<a.size();++i)
		if (tek.size()==0 || a[i]-tek[tek.size()-1]>=d)
			tek.pb(max(a[i]-tim,tek[tek.size()-1]+d));
		else 
			tek.pb(min(a[i]+tim,tek[tek.size()-1]+d));
	bool f=true;
	for (int i=1;i<tek.size();++i)
		if (tek[i]-tek[i-1]<d)
			f=false;
	return f;
}

int main(){
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif
	int t;
	scanf("%d",&t);
	for (int z=1;z<=t;++z){
		printf("Case #%d: ",z);
		scanf("%d %d",&n,&d);
		a.clear();
		for (int i=0;i<n;++i){
			int p,v;
			scanf("%d %d",&p,&v);
			for (int j=0;j<v;++j)
				a.pb(p);
		}
		sort(a.begin(),a.end());
		ld l=0;
		ld r=10000;
		for (int it=0;it<200;++it){
			ld m=(l+r)/2;
			if (checkans(m))
				r=m;
			else l=m;
		}
		cout.precision(10);
		cout<<fixed<<l<<endl;
	}
	return 0;
}