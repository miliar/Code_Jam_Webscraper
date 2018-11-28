//A
#include<iostream>
using namespace std;
#define eps 1e-6
#define inf 10000000
double p[100000],t[100000];
int main(){
	int T,a,b;
	double ans,y;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>T;
	for(int cnt=1;cnt<=T;cnt++)
	{
		cin>>a>>b;
		for(int i=0;i<a;i++) scanf("%lf",&p[i]);
		ans=inf;
		t[0]=p[0];
		for(int i=1;i<a;i++) t[i]=t[i-1]*p[i];
		y=t[a-1]*(b-a+1)+(1-t[a-1])*(b-a+2+b);
		if(y<ans) ans=y;
		for(int i=1;i<=a;i++)
		{			
			y=t[a-i-1]*(i+i+b-a+1)+(1-t[a-i-1])*(i+i+b+b-a+2);
			if(y<ans) ans=y;
		}
		if(b+2<ans) ans=b+2;
		printf("Case #%d: %.6lf\n",cnt,ans);
	}
	return 0;
}
