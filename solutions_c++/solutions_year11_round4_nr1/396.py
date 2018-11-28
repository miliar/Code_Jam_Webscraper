#include<iostream>
#include<sstream>
#include<vector>
#include<map>
#include<string>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<queue>
#include<stack>
#define INF (1<<29)
#define EPS (1e-14)
#define two(a) (1<<(a))
#define sca(t) scanf("%d",&t)
#define scal(t) scanf("%lld",&t)
#define rep(a,b) for(a=0 ; a<b ; ++a)
#define xrep(a,b,c) for(a=b ; a<c ; ++a)
typedef long long ll;
using namespace std;

struct Node{
	int st,ed,wi;
}node[1001];

int cmp(Node a,Node b){
	return a.wi<b.wi;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("pabig.txt","w",stdout);
	int i,j,k,t,tt;
	int x,s,r,n;
	double runlen,ans,tim;
	sca(tt);
	for(t=1 ; t<=tt ; t++){
		cin >> x >> s >> r >> tim >> n;
		rep(i,n){
			scanf("%d%d%d",&node[i].st,&node[i].ed,&node[i].wi);
		}
		sort(node,node+n,cmp);
		int alen(0);
		ans=0.0;
		alen=x;
		for(i=0 ; i<n ; i++) alen-=(node[i].ed-node[i].st);
		if(double(alen)/r>=tim){
			ans+=tim;
			alen-=r*tim;
			tim=0;
			ans+=double(alen)/s;
		}
		else{
			ans+=double(alen)/r;
			tim-=double(alen)/r;
		}
		for(i=0 ; i<n ; i++){
			double xlen=node[i].ed-node[i].st;
			if(xlen/(r+node[i].wi)>=tim){
				ans+=tim;
				xlen-=(r+node[i].wi)*tim;
				tim=0.0;
				ans+=xlen/(s+node[i].wi);
			}
			else{
				ans+=xlen/(r+node[i].wi);
				tim-=xlen/(r+node[i].wi);
			}
		}
		cout << "Case #" << t << ": ";
		printf("%.10lf\n",ans);
	}
}
