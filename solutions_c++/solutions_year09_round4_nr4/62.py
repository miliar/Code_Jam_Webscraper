
#include <iostream>
#include <cstring>
#include <deque>
#include <vector>
#include <cstdio>
#include <stack>
#include <cmath>
#include <map>
#include <algorithm>
using namespace std;

typedef pair<int,int> pii;
#define f first
#define s second

int main(){
	int nn;scanf("%d",&nn);
	while(nn--){
		int n;scanf("%d",&n);

		int x[n],y[n],r[n];
		for(int i=0;i<n;i++)scanf("%d%d%d",x+i,y+i,r+i);

		double ans=1e100;
		if(n==1){
			ans=r[0];
		}else if(n==2){
			ans=max(r[0],r[1]);
		}else if(n==3){
			for(int i=0;i<3;i++){
				int k=(i+1)%3;
				int t=(i+2)%3;
				double dist=hypot((double)x[i]-x[k],(double)y[i]-y[k]);
				ans=min(ans,max((dist+r[i]+r[k])/2,(double)r[t]));
			}
		}else{
			puts("ERR");
		}

		static int npr=1;
		printf("Case #%d: %.6lf\n",npr++,ans);
	}
}
