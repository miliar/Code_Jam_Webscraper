#include<iostream>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<cstdio>
using namespace std;
int gcd(int a,int b){
	if(b==0)return a;
	return gcd(b,a%b);
}
int main(){

	int y,n,i,j,m,k,t[3],d,c;
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	scanf("%d",&c);
	for(i=1;i<=c;i++){
		scanf("%d",&n);
		for(j=0;j<n;j++)
			scanf("%d",&t[j]);		
		sort(t,t+n);
		if(n==2)d=t[1]-t[0];
		else
			d=gcd(t[2]-t[0],t[1]-t[0]);
		if(t[0]%d==0)
			y=0;
		else y=d-t[0]%d;
		printf("Case #%d: %d\n",i,y);
	}
	return 0;
}