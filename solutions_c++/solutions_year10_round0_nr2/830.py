#include<iostream>
#include<stdio.h>
#include<cstring>
#include<cmath>
using namespace std;
int a[5];
int gcd(int a,int b){
	if (b==0)
		return a;
	else return gcd(b,a%b);
}
int main(){
	int test,i,j,k,temp,t,n;
	freopen("B-small-attempt3.in","r",stdin);
	freopen("B-small-attempt.out","w",stdout);
	scanf("%d",&test);
	for (t=1;t<=test;t++){
		scanf("%d",&n);
		for (i=1;i<=n;i++)
			scanf("%d",&a[i]);
		for (i=1;i<n;i++)
			for (j=i+1;j<=n;j++)
				if (a[i]<a[j])
					swap(a[i],a[j]);
		printf("Case #%d: ",t);
		if(a[1]==a[2]&&a[2]==a[3]){
			printf("%d\n",0);
			continue;
		}
		else if (a[1]==a[2]||a[2]==a[3]){
			temp=a[1]-a[3];
			j=0;
			while (j*temp<a[3]) j++;
			printf("%d\n",temp*j-a[3]);
			continue;
		}
		if (n==3){
			temp=gcd(a[1]-a[3],a[2]-a[3]);
			j=0;
			while (j*temp<a[3]) j++;
			printf("%d\n",j*temp-a[3]);
		}
		if (n==2){
			temp=a[1]-a[2];
			j=0;
			while (j*temp<a[2]) j++;
			printf("%d\n",j*temp-a[2]);
		}
	}
	return 0;
}
