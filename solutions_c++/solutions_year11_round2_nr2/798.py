#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

typedef vector <int> vi;
#define pb push_back
#define rep(i,n) for (int i=0;i<(n);i++)

double max(double a, double b){
	return (a>b)?a:b;
}

int main(){
	freopen("hotdog.in","r",stdin);
	freopen("hotdog.out","w",stdout);
	int t=0;
	scanf("%d",&t);
	rep(k,t){
		double ans=0.0;
		int c, d;
		vi p, v, sv;
		int sum=0;
		scanf("%d %d",&c,&d);
		rep(i,c){
			int tp, tv;
			scanf("%d %d",&tp,&tv);
			if (tv>1){
				ans=max(ans,(double)((tv-1)*(d-1)+tv-1)/2.);
			}
			sum+=tv;
			p.pb(tp);
			v.pb(tv);
			sv.pb(sum);
		}
		for(int i = p.size()-1;i>-1;i--){
			for(int j=p.size()-1;j>i;j--){
				/*double ln = (double)(p[i]-p[0]+1);
				double ls = (double)((sv[i]-1)*(d-1)+sv[i]);
				ans=max(ans,(ls-ln)/2.);*/
				double ln = (double)(p[j]-p[i]+1);
				double ls;
				if (i>0) ls = (double)((sv[j]-sv[i-1]-1)*(d-1)+sv[j]-sv[i-1]);
				else ls = (double)((sv[j]-1)*(d-1)+sv[j]);
				ans=max(ans,(ls-ln)/2.);
			}
		}
		printf("Case #%d: %lf\n",k+1,ans);
		
	}
	return 0;
}