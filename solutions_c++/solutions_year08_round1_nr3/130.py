#include<iostream>
struct W
{
	int a,b;
}I;
W mul(W a,W b)
{
	W rr;
	rr.a=a.a*b.a+a.b*b.b*5;
	rr.b=a.b*b.a+a.a*b.b;
	rr.a%=10000;
	rr.b%=10000;
	return rr;
}
W cal(int n)
{
	if(n==1)return I;
	else if(n%2==0)
	{
		W ttt=cal(n/2);
		return mul(ttt,ttt);
	}
	else
	{
		W ttt=cal(n/2);
		return mul(I,mul(ttt,ttt));
	}
}
int main()
{
	int i,n,cs,css,a,b,aa,bb;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	I.a=3;I.b=1;
	scanf("%d",&cs);
	for(css=1;css<=cs;css++)
	{
		scanf("%d",&n);
		W tt=cal(n);
		printf("Case #%d: %03d\n",css,tt.a*2%1000-1);
	}
	return 0;
}
