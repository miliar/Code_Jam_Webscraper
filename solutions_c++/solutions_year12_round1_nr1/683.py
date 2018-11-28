#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<windows.h>
using namespace std;

int t;
int a,b;
double p[110000];
double ans;

int main(){
	int h,i,j,k;
	double x,y,z;
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%d%d",&a,&b);
		for(i=0;i<a;i++)
			scanf("%lf",&p[i]);
		ans=b+2;x=1.0;z=b-a+1;
		for(i=0;i<=a;i++){
			if(i>0)x*=p[i-1];
			y=a-i+b-i+1+(1.0-x)*(b+1);
			if(ans>y)ans=y;
		}
		printf("Case #%d: %.6lf\n",h,ans);
	}
	//Sleep(1000);
	//while(1);
	return 0;
}