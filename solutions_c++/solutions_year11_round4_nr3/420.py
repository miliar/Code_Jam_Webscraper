#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
int x[1000010],p[1000001],zh[1000001];
int a,b,c,d,e,f,g,h,i,j,k,m;
int mi[10010],ma[10010];
long long w,n;
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	zh[1]=1;
	c=0;
	for (i=2;i<=1000000;i++) if (zh[i]==0){
		c++;p[c]=i;
		for(j=2;j<=1000000/i;j++) zh[i*j]=1;
		}
	g=c;
	//for (i=1;i<=1000;i++) printf("%d %d %d\n",mi[i],ma[i],mi[i]-ma[i]);
	int tcase;
	scanf("%d",&tcase);
	for (f=1;f<=tcase;f++){
		printf("Case #%d: ",f);
		scanf("%lld",&n);
		if (n==1){ printf("0\n");continue;}
		int ans=0;
		for (i=1;i<=c;i++) if (p[i]>sqrt(n)) break; else{
			w=p[i];
			e=0;
	//	if (f==3)	printf("%d\n",w);
			while (w<=n) {w=w*p[i];e++;}
					//if (f==3)	printf("%d %d\n",w,e);}
			ans=ans+e-1;
			}
		printf("%d\n",ans+1);
		}
	return 0;
}
