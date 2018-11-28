#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#include<iostream>
using namespace std;
struct point{
	int p;
	int v;
}node[300];

const double eps=1e-9;

bool cmp(point a,point b){
	return a.p<b.p;
}

bool check(double mid,int c,int d){
	double pre=node[0].p-mid;
//	printf("%f\n",pre);
	for(int i=0;i<c;++i){
		for(int j=0;j<node[i].v;++j){
			if(pre+d>node[i].p+mid+eps)return false;
//			printf("%f\n",pre);
			pre=max(node[i].p-mid,pre+d);
		}
	}
	return true;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		int c,d;
		scanf("%d%d",&c,&d);
		for(int i=0;i<c;++i)
			scanf("%d%d",&node[i].p,&node[i].v);
	//	sort(node,node+c,cmp);
		double low=0.0,high=1e13;
		--node[0].v;
		while(fabs(low-high)>eps){
			double mid=(low+high)/2.0;
			if(check(mid,c,d)){
				high=mid;
			}else{
				low=mid;
			}
		}		
		printf("Case #%d: %.12f\n",t,low);
	}
	return 0;
}
