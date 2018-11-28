#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<ctime>
#include<cassert>
using namespace std;
#define y1 fndjifhwdn
#define ws vfsdkofsjd
#define fs first
#define sc second
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pi;
int w,n1,n2,g;
ld s0;
int x1[1000];
int x2[1000];
int y1[1000];
int y2[1000];

ld calcs(ld x){
	ld ans=0;
	for (int i=0;i<n1-1;i++){
		if (x1[i+1]<=x){
			ans-=(-x1[i]+x1[i+1])*(y1[i+1]+y1[i])*0.5;
		} else {
			ans-=(-x1[i]+x)*(2*y1[i]+(y1[i+1]-y1[i])*(-x1[i]+x)*1.0/(-x1[i]+x1[i+1]))*0.5;
			break;
		}
	}
	for (int i=0;i<n2-1;i++){
		if (x2[i+1]<=x){
			ans+=(-x2[i]+x2[i+1])*(y2[i+1]+y2[i])*0.5;
		} else {
			ans+=(-x2[i]+x)*(2*y2[i]+(y2[i+1]-y2[i])*(-x2[i]+x)*1.0/(-x2[i]+x2[i+1]))*0.5;
			break;
		}
	}
	return ans;
}
ld cut(ld s){
	ld l,r,m;
	l=0;
	r=w;
	for (int it=0;it<=200;it++){
//		cerr<<l<<" "<<r<<" "<<m<<" "<<calcs(m)<<" "<<s<<endl;
		m=(l+r)/2;
		if (calcs(m)<s) l=m;
			       else r=m;
	}
	return l;
}
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tt;
	scanf("%d",&tt);
	for (int ti=0;ti<tt;ti++){
		printf("Case #%d:\n",ti+1);
		scanf("%d%d%d%d",&w,&n1,&n2,&g);
		for (int i=0;i<n1;i++){
			scanf("%d%d",&x1[i],&y1[i]);
			y1[i]+=2000;
		}
		for (int i=0;i<n2;i++){
			scanf("%d%d",&x2[i],&y2[i]);
			y2[i]+=2000;
		}
		s0=calcs(w);
		for (int i=0;i<g-1;i++){
			printf("%.18lf\n",(double)cut((s0*(i+1))/g));
		}
	}
    return 0;
}









