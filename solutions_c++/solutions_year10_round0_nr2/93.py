#include<iostream>
#include<algorithm>
using namespace std;

int n;
int t[1001],d,y;

int gcd(int a,int b){
	int c;
	while(b){
		c=b;
		b=a%b;
		a=c;
	}
	return a;
}

int main()
{
	int ci,c,i;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	scanf("%d",&c);
	for(ci=1;ci<=c;++ci)
	{
		scanf("%d",&n);
		for(i=0;i<n;++i)
			scanf("%d",&t[i]);
		sort(t,t+n);
		for(i=n-1;i>=1;--i)
			t[i]=t[i]-t[i-1];
		d=t[1];
		for(i=2;i<n;++i)
			d=gcd(d,t[i]);
		y=((-t[0])%d+d)%d;
		printf("Case #%d: %d\n",ci,y);
	}
	//system("pause");
	return 0;
}