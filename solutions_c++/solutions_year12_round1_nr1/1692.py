#include<stdio.h>
#include<math.h>
#define MAX 100005
double posi[MAX];
double pro[MAX];
int t[MAX];
double temp;

int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int t,a,b,ti;
	double ans;
	scanf("%d",&t);
	for(ti=1;ti<=t;ti++){
		scanf("%d %d",&a,&b);
		int i,j,k;
		for(i=0;i<a;i++)scanf("%lf",&pro[i]);
		pro[a]=0;
		ans=99999999;
		printf("Case #%d: ",ti);
		double tsum=posi[0];
		for(i=0;i<=a;i++){
			posi[i]=1-pro[i];
			for(j=0;j<i;j++)posi[i]*=pro[j];
		}
		/*for(i=0;i<=a;i++)printf("%lf ",posi[i]);
		printf("\n");*/
		ans=(b+1-a)+(b+1)*(1-posi[a]);
		//printf("%lf\n",ans);
		if(ans>(b+2))ans=b+2;
		//printf("%lf\n",ans);
		for(i=1;i<=a;i++){
			double ts=posi[a];
			//for(j=a;j>=a-i;j--)ts+=posi[j];
			ts+=posi[a-i];
			temp=ts*(i+i+b+1-a)+(1-ts)*(i+i+b+2-a+b);
			if(ans>temp)ans=temp;
			//printf("%lf\n",temp);
		}
		printf("%lf\n",ans);
	}
	return 0;
}