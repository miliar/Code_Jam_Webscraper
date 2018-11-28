#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
const int maxn=101;
int n;
double x[maxn],y[maxn],r[maxn];

double cost(int a,int b){
	return (hypot(x[a]-x[b],y[a]-y[b])+r[a]+r[b])*0.5;
}

void init(){
	scanf("%d",&n);
	for (int i=0;i<n;i++){
		scanf("%lf%lf%lf",&x[i],&y[i],&r[i]);
	}
	return;
}

double special(){
	double answer;
	if (n==1){
		return r[0];
	}
	if (n==2){
		return max(r[0],r[1]);
	}
	if (n==3){
		double ans;
		ans=max(r[0],cost(1,2));
		ans=min(ans,max(r[1],cost(0,2)));
		ans=min(ans,max(r[2],cost(0,1)));
		return ans;
	}
}

int main(){
	int t;
	scanf("%d",&t);
	for (int k=1;k<=t;k++){
		init();
		printf("Case #%d: %lf\n",k,special());
	}
	return 0;
}

