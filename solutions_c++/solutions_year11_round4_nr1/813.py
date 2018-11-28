#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
 
using namespace std;
 
#define pb push_back
#define mp make_pair
#define vs vector<string>
#define vi vector<int>
#define pii pair<int,int>
#define vvi vector< vector<int> >
#define vpi vector< pair<int,int> >
#define LL long long


int X,R,S,N;
double t;

#define INF 1e9

bool lt(pair<int,int> a, pair<int,int> b) {
return (a.second*(S+b.first) < b.second*(S+a.first));
}


int main() {
        int T; cin >> T;
        for(int iter=0;iter<T;iter++) {
			cin >> X >> S >> R >> t >> N;
			double ans = 0;
			vector< pair<int, int> > ws;
			for(int i=0;i<N;++i) {
				int a,b,s;
				cin >> a >> b >> s;
				ws.pb(mp(s,b-a));
				X-=(b-a);
			}
			ws.pb(mp(0,X));
			sort(ws.begin(),ws.end());
			for(int i=0;i<ws.size();++i) {
				if (t<=0)
					ans += 1.*ws[i].second/(S+ws[i].first);
				else if(t>=(1.*ws[i].second/(R+ws[i].first)))
					{
						t-=(1.*ws[i].second/(R+ws[i].first));
						ans+=(1.*ws[i].second/(R+ws[i].first));
					}
				else {
					ans += t;
					ans += 1.*(ws[i].second-t*(R+ws[i].first))/(S+ws[i].first);
					t = 0;
				}
			}
			printf("Case #%d: %.09lf\n",(iter+1),ans);
	}
}

