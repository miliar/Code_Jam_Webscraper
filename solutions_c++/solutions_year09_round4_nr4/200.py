#include <iostream>
#include <cmath>
using namespace std;

int x[10],y[10],r[10],t,tt,i,j,k,n;
double res;

double sqr(int x){return x*x ; };

int main(){
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	cin>>tt;
	for (t=1;t<=tt;++t){
		cin>>n;
		res=0;
		for (i=0;i<n;++i){
			cin>>x[i]>>y[i]>>r[i];
			res=max(res,(double)r[i]);
		};
		res*=2;
		if (n>2){
			res=1000000;
			for (i=0;i<n;++i)
				for (j=0;j<n;++j)if (i!=j)
					for (k=0;k<n;++k)if (i!=k && j!=k)
						res=min(res,max(sqrt(sqr(x[i]-x[j])+sqr(y[i]-y[j]))+r[i]+r[j],(double)r[k]*2));
		};
		printf("Case #%d: %.10lf\n",t,res/2);
	};
};