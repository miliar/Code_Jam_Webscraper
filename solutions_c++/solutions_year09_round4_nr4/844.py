#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;

const int N=3;

int n;
double x[N],y[N],r[N];

double min(double a,double b){
	return (a<b?a:b);
}

double max(double a,double b){
	return (a>b?a:b);
}
bool Input(){
	scanf("%d",&n);
	int i;
	for(i=0;i<n;++i){
		scanf("%lf%lf%lf",&x[i],&y[i],&r[i]);
	}
	return 1;
}

double GetR(int n1,int n2){
	double ret;
	double d=sqrt(pow(x[n1]-x[n2],2.0)+pow(y[n1]-y[n2],2.0));
	if(d<fabs(r[n1]-r[n2])){
		ret = max(r[n1],r[n2]);
	}else{
		ret=(r[n1]+r[n2]+d)/2;
	}
	return ret;
}

double Cal(int c[3]){
	if(n==1){
		return r[c[0]];
	}
	if(n==2){
		return max(r[c[0]],r[c[1]]);
	}
	return max(GetR(c[0],c[1]),r[c[2]]);
}

void Solve(int cn){
	int i,j,k;
	double ans=0;
	for(i=0;i<n;++i){
		ans=max(ans,r[i]);
	}
	int c[]={0,1,2};
	ans=Cal(c);
	while(next_permutation(c,c+n)){
		ans=min(ans,Cal(c));
	}
	printf("Case #%d: %.6lf\n",cn,ans);
	return;
}

int main()
{
	freopen("D-small.in","r",stdin);
	freopen("D-small.out","w",stdout);
	int tn,id=0;
	scanf("%d",&tn);
	while(tn--){
		Input();
		Solve(++id);
	}
	return 0;
}
