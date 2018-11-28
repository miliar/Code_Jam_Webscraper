#include<queue>
#include<cstdio>
#include<algorithm>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

int main(){
	int T0; scanf("%d",&T0);
	for(int T=1;T<=T0;T++){
		int len,walk,run,n;
		double t_run;
		scanf("%d%d%d%lf%d",&len,&walk,&run,&t_run,&n);

		static int w[1000000];
		rep(x,len) w[x]=0;
		rep(i,n){
			int a,b,w0; scanf("%d%d%d",&a,&b,&w0);
			for(int x=a;x<b;x++) w[x]=w0;
		}

		sort(w,w+len);

		double ans=0;
		rep(x,len){
			int w0=w[x];
			if(t_run*(w0+run)>1){
				ans+=1.0/(w0+run);
				t_run-=1.0/(w0+run);
			}
			else{
				double dist=t_run*(w0+run);
				ans+=t_run+(1-dist)/(w0+walk);
				t_run=0;
			}
		}
		printf("Case #%d: %.9f\n",T,ans);
	}

	return 0;
}
