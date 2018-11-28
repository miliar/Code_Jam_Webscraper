#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<iostream>
#include<map>
using namespace std;
#define see(x) (cerr<<"Line:["<<__LINE__<<"]: "<<#x<<" : "<<x<<"\n")
double pro[110000];
double dp[110000];
double current[110000];
int main(){
	int T;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int tt=0;tt<T;tt++){
		int A,B;
		scanf("%d%d",&A,&B);
		for(int i=1;i<=A;i++){
			scanf("%lf",&pro[i]);	
		}	
		memset(dp,0,sizeof(dp));
		memset(current,0,sizeof(current));
		current[0]=1;
		for(int i=1;i<=A;i++){
			current[i] = current[i-1] * pro[i];	
		}
		//keep typing
		double ans = 1e20;
		ans = min(ans,current[A]*(B-A+1)+(1-current[A])*(B-A+1+B+1));
		//back space
		double tmp = 0;
		for(int i=1;i<=A;i++){
			tmp = current[A-i] * (i+i+B-A+1) + (1-current[A-i])*(i+i+B-A+1+B+1);
			ans = min(ans,tmp);
		}
		//enter right now
		ans = min(ans,1.0+B+1.0);
		printf("Case #%d: %.6lf\n",tt+1,ans);
	}
}
