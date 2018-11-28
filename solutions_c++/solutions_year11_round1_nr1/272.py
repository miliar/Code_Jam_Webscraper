#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
int a,b,c,d,e,f,g,h,i,j,k,m,tcase,pd,pg;
double p,r,l;
long long n;
const double lim=1e-9;
int main()
{
	//freopen("A.in","r",stdin);
	//freopen("A.out","w",stdout);
	scanf("%d",&tcase);
	for (f=1;f<=tcase;f++){
		printf("Case #%d: ",f);
		bool can=1;
		scanf("%lld%d%d",&n,&pd,&pg);
		if (n<100 && pd>0){
			e=1;
			for (i=1;i<=n;i++){
				p=i*100;
				p=p/pd;
				//printf("%.7lf %d %d %d\n",p,i,pd,n);
				if (fabs(p-int(p+0.5))<lim && int(p+0.5)<=n) {e=0;break;}
				}
			if (e) can=false;
			}
		if (pd<100 && pg==100) can=0;
		if (pd>0 && pg==0) can=0;
		if (can) printf("Possible\n"); else printf("Broken\n");
		}
	return 0;
}
