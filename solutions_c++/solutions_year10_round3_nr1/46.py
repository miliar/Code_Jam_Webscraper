#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>
#include <sstream>
#include <map>
using namespace std;
int main(){
	int n,i,j,t,test,T,count;
	long long x1[1000],x2[1000];
	long long A1,B1,C1,A2,B2,C2,D,det;
	scanf("%d",&T);
	for (test=1;test<=T;test++){
		printf("Case #%d: ",test);
		scanf("%d",&n);
		for (i=0;i<n;i++)
			scanf("%lld%lld",&x1[i],&x2[i]);
		count=0;
		for (i=0;i<n;i++)
			for (j=i+1;j<n;j++){
				A1=10;
				B1=x1[i]-x2[i];
				C1=A1*x1[i]+B1*0;
				A2=10;
				B2=x1[j]-x2[j];
				C2=A2*x1[j]+B2*0;
				det=A1*B2-A2*B1;
				if (det==0) continue;
				D=A1*C2-A2*C1;
				if (det<0) {det=-det; D=-D;}
				if (D>=0&&D<=det*10) count++;
				//printf("%.3lf\n",(double)D/det);
			}
		printf("%d\n",count);
	}
  return 0;
}
