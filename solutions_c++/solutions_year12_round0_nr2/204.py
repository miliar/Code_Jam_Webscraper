#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

int t,s,n,p;
int ti[1000];

int main(){
	int h,i,j,k;
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%d%d%d",&n,&s,&p);
		for(i=0;i<n;i++)
			scanf("%d",&ti[i]);
		sort(ti,ti+n);
		k=0;
		for(i=n-1;i>=0;i--){
			if(ti[i]>=3*p-2 && ti[i]>=p)k++;
			else if(s>0 && ti[i]>=3*p-4 && ti[i]>=p){k++;s--;}
		}
		printf("Case #%d: %d\n",h,k);
	}
	return 0;
}
