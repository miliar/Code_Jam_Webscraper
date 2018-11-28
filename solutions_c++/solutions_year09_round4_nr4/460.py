#include <cstdio>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <functional>
#include <vector>
#include <cmath>

using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,Q,i,j;
	double ans;
	scanf("%d",&Q);
	for(T=1;T<=Q;T++){
		int n;
		scanf("%d",&n);
		double X[3],Y[3],R[3];
		for(i=0;i<n;i++)scanf("%lf%lf%lf",&X[i],&Y[i],&R[i]);
		if(n==1)ans=R[0];
		if(n==2)ans=max(R[0],R[1]);
		if(n==3){
			double d1=max((sqrt((X[1]-X[0])*(X[1]-X[0])+(Y[1]-Y[0])*(Y[1]-Y[0]))+R[0]+R[1])*0.5,R[2]);
			double d2=max((sqrt((X[2]-X[0])*(X[2]-X[0])+(Y[2]-Y[0])*(Y[2]-Y[0]))+R[0]+R[2])*0.5,R[1]);
			double d3=max((sqrt((X[1]-X[2])*(X[1]-X[2])+(Y[1]-Y[2])*(Y[1]-Y[2]))+R[2]+R[1])*0.5,R[0]);
			ans=min(d1,min(d2,d3));
		}
		printf("Case #%d: %.9lf\n",T,ans);
	}

	return 0;
}
