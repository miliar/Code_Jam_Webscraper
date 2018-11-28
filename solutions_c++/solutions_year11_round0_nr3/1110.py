#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int a,b,c,d,e,f,g,h,i,j,k,m,n,testcase;
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&testcase);
	for (f=1;f<=testcase;f++){
		printf("Case #%d: ",f);
		scanf("%d",&n);
		a=2147483647;b=0;m=0;
		for (i=1;i<=n;i++){
			scanf("%d",&c);
			b=b^c;m=m+c;
			if (c<a) a=c;}
		if (b!=0) printf("NO\n"); else 
			printf("%d\n",m-a);
		}
	return 0;
}
