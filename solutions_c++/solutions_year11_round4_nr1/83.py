#include<stdio.h>
#include<algorithm>
#include<utility>
using namespace std;
int n,len,walk,run;
pair<int,int> a[3000];
double tim;
int main(){
	int _,t;
	scanf("%d",&_);
	for(t=1; t<=_; t++){
		scanf("%d%d%d%lf%d",&len,&walk,&run,&tim,&n);
		for(int i=0; i<n; i++){
			int x,y;
			scanf("%d%d%d",&x,&y,&a[i].first);
			a[i].second=y-x;
			len-=a[i].second;
		}
		a[n++]=make_pair(0,len);
		sort(a,a+n);
		double ans=0;
		for(int i=0; i<n; i++){
			double u=a[i].second/(a[i].first+run+.0);
			if(u>tim){
				double newl=a[i].second-tim*(run+a[i].first+.0);
				ans+=tim;
				tim=0;
				ans+=newl/(a[i].first+walk+.0);
			}else{
				tim-=u;
				ans+=u;
			}
		}
		printf("Case #%d: %.10lf\n",t,ans);
	}
	return 0;
}
