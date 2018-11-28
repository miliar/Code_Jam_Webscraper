#include <cstdio>

int i,j,k,s,t,n,m;
int a[50];
int b[4][4];
int T,I;
int aa,bb,cc,dd;

void calc(int a,int b,int c,int d,int n,int &e,int &f,int &g,int &h)
{
	int a1,b1,c1,d1;
	if (n==1) {
		e=a;f=b;g=c;h=d;
		return;
	}
	else if (n%2==0)
	{
		calc(a,b,c,d,n/2,a1,b1,c1,d1);
		e=(a1*a1+b1*c1+10000000)%1000;
		f=(a1*b1+b1*d1+10000000)%1000;
		g=(c1*a1+d1*c1+10000000)%1000;
		h=(c1*b1+d1*d1+10000000)%1000;
		return;
	}
	else
	{
		calc(a,b,c,d,n/2,a1,b1,c1,d1);
		int ee,ff,gg,hh;
		ee=(a1*a1+b1*c1+10000000)%1000;
		ff=(a1*b1+b1*d1+10000000)%1000;
		gg=(c1*a1+d1*c1+10000000)%1000;
		hh=(c1*b1+d1*d1+10000000)%1000;
		e=(ee*a+ff*c+10000000)%1000;
		f=(ee*b+ff*d+10000000)%1000;
		g=(gg*a+hh*c+10000000)%1000;
		h=(gg*b+hh*d+10000000)%1000;
		return;
	}
}
		
main()
{
	a[0]=2;
	a[1]=6;
	for (i=2;i<=30;++i)
		a[i]=(6*a[i-1]%1000-4*a[i-2]%1000+1000)%1000;
	scanf("%d",&T);
	while (T--){
		scanf("%d",&n);
		calc(0,1,-4,6,n-1,aa,bb,cc,dd);
//		printf("%d\n",n);
		printf("Case #%d: %03d\n",++I,(cc*2%1000+dd*6%1000+10000999)%1000);
	}
	return 0;
}
	
