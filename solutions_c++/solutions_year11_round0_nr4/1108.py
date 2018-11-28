#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int a,b,c,d,e,f,g,h,i,j,k,m,n,testcase;
int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	scanf("%d",&testcase);
	for (f=1;f<=testcase;f++){
		printf("Case #%d: ",f);
		scanf("%d",&n);
		c=0;
		for (i=1;i<=n;i++){
			scanf("%d",&e);
			if (e!=i) c++;}
		printf("%d.000000\n",c);
		}
	return 0;
}
