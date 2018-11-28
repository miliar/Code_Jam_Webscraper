#include<cstdio>
#include<algorithm>
using namespace std;
double prev,a[1000001],t;
int n;
bool pos(double first){
	int i;
	double prev;
	prev = a[1]-first;
	for(i=2;i<=n;i++){
		if(((prev+t)-(a[i]+first))>=-0.00000001){
			return 0;
		}
		prev=max(prev+t,a[i]-first);
	}
	return 1;
}
main(){
	int k,i,cur,V,j,test;
	double P;
	scanf("%d",&k);
	for(test=1;test<=k;test++){
		scanf("%d",&n);
		scanf("%lf",&t);
		cur=0;
		for(i=1;i<=n;i++){
			scanf("%lf %d",&P,&V);
			for(j=0;j<V;j++)
				a[++cur]=P;
		}
		n=cur;
		double mid=0,ub=100000000000000LL,lb=0;
		int x=400;
		while(x--){
			mid=(ub+lb)/2.0;
			if(pos(mid))
				ub=mid;
			else
				lb=mid;
		}
		fprintf(stderr,"%d\n",test);
		printf("Case #%d: %0.8lf\n",test,mid);
	}
}
