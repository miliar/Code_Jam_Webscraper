#include<stdio.h>
#include<string.h>
#include<math.h>



struct Ci{
	double x,y,r;
}ft[111];


double dis(Ci a,Ci b){
	return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}

double MIN(double x,double y){
	return x>y?y:x;
}

double MAX(double x,double y){
	return x>y?x:y;
}


int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,t;
	int T,ca=0;
	int n;
	double ans,temp;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		for(i=0;i<n;i++) scanf("%lf%lf%lf",&ft[i].x,&ft[i].y,&ft[i].r);
		printf("Case #%d: ",++ca);
		if(n==1){
			printf("%.6lf\n",ft[0].r);
		}
		else if(n==2){
			printf("%.6lf\n",MAX(ft[0].r,ft[1].r));
		}
		else{
			ans=1000000000;
			temp=MAX(ft[0].r,(dis(ft[1],ft[2])+ft[1].r+ft[2].r)/2.0);
			ans=MIN(temp,ans);
			temp=MAX(ft[1].r,(dis(ft[0],ft[2])+ft[0].r+ft[2].r)/2.0);
			ans=MIN(temp,ans);
			temp=MAX(ft[2].r,(dis(ft[1],ft[0])+ft[1].r+ft[0].r)/2.0);
			ans=MIN(temp,ans);
			printf("%.6lf\n",ans);
		}
	}
	return 0;
}
