#include<cstdio>
#include<iostream>
#include<cmath>
using namespace std;
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int C,ccc,x,s,m,a,n;
	scanf("%d",&C);
	for(ccc=1;ccc<=C;++ccc){
		scanf("%d",&n);
		x=0;s=0;m=100000000;
		for(int i=0;i<n;++i){
			scanf("%d",&a);
			s+=a;
			x^=a;
			m=a<m?a:m;
		}
		printf("Case #%d: ",ccc);
		if(x)puts("NO");
		else printf("%d\n",s-m);
	}
	return 0;
}
