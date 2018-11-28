#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <cstring>
#include <queue>
#define vvi vector<vector<int> > 
#define pii pair<int,int>
#define vpii vector<vector<pair<int,int> > > 
#define mp(a,b) make_pair(a,b)
#define ll long long
#define vi vector<int>
#define vs vector<string>
#define sz size()
#define pb push_back
#define all(x) x.begin(),x.end()
using namespace std;
struct state{
	int i;
	int j;
	int w;
	state(): i(0) , j(0) , w(0) {}
	state(int ai,int aj,int aw) : i(ai) , j(aj),w(aw) {}
};
bool operator <(const state &a,const state &b)
{
	if(a.w!=b.w) return a.w<b.w;
	if(a.i!=b.i) return a.i<b.i;
	return a.j<b.j;
}
state ar[1010];
int main()
{
	int tc;
	scanf("%d",&tc);
	int caseno=1;
	while(tc--){
		int x,s,r,t,n;
		scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		int take = 0;
		for(int i=0;i<n;i++){
			scanf("%d%d%d",&ar[i].i,&ar[i].j,&ar[i].w);
			take +=ar[i].j-ar[i].i;
		}
		take=x-take;
		sort(ar,ar+n);
		double ret = 0;
		double T = t;
			int dist = take;
			if(dist<(r)*T) {
				ret += dist/((double)r);
				T-=dist/((double)r);
			}
			else{
				double gDist = T*(r);
				ret +=T;
				T=0;
				gDist =dist-gDist;
				ret += gDist/((double)s);
			}
		for(int i=0;i<n;i++){
			dist = ar[i].j-ar[i].i;
			if(dist<(ar[i].w+r)*T) {
				ret += dist/((double)ar[i].w+r);
				T-=dist/((double)ar[i].w+r);
			}
			else{
				double gDist = T*(ar[i].w+r);
				ret +=T;
				T=0;
				gDist =dist-gDist;
				ret += gDist/((double)ar[i].w+s);
			}
		}
			printf("Case #%d: %.9lf\n",caseno++,ret);
	}
	return 0;
}