#include <stdio.h>
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <string.h>
#include <queue>
#include <algorithm>
#include <math.h>
#include <sstream>
using namespace std;
typedef pair<int, int> pi;
typedef long long int li;
typedef vector<int> vi;
void solve();
#define mp make_pair
#define pb push_back

int main(){
#ifdef DEBUG
    freopen("input", "r", stdin);
    freopen("output","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}
    return 0;
}

void solve(){
	int n;
	scanf("%d",&n);
	vi bl[2];
	vector<pi> ob;
	for(int i=0;i<n;++i){
		char c;
		int d;
		scanf(" %c%d",&c,&d);
		if(c=='B')
			bl[0].pb(d);
		else
			bl[1].pb(d);
		ob.pb(pi((int)(c=='O'),d));
	}
	bl[0].pb(1LL<<30);
	bl[1].pb(1LL<30);
	li ans=0;
	int cnt[2]={0,0};
	int pos[2]={1,1};
	while(cnt[0]+cnt[1]<n){
		int first=ob[cnt[0]+cnt[1]].first;
		int second=1-first;
		int hod=abs(pos[first]-bl[first][cnt[first]])+1;
		ans+=hod;
		pos[first]=bl[first][cnt[first]++];
		if(hod>=abs(pos[second]-bl[second][cnt[second]]))
			pos[second]=bl[second][cnt[second]];
		else if(pos[second]-bl[second][cnt[second]]>0){
			pos[second]-=hod;
		}
		else
			pos[second]+=hod;
	}
	printf("%lld\n",ans);
}