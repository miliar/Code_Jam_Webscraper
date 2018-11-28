#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<windows.h>
#include<set>
using namespace std;

int t,n;
int s[210];
double a[210];
int v[210];

bool cmp(const int&a,const int&b){
	return s[a]<s[b];
}

int main(){
	int h,i,j;
	double l,k;
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%d",&n);
		k=l=0;
		for(i=0;i<n;i++){
			scanf("%d",&s[i]);
			l+=s[i];
			v[i]=i;
		}
		k=l;
		sort(v,v+n,cmp);
		memset(a,0,sizeof(a));
		for(i=n-1;i>=0;i--){
			if((k+l)/(i+1)>s[v[i]]){
				for(j=0;j<=i;j++){
					a[v[j]]=((k+l)/(i+1)-s[v[j]])/l*100;
				}
				break;
			}else{
				k-=s[v[i]];
			}
		}
		printf("Case #%d:",h);
		for(i=0;i<n;i++){
			printf(" %.6lf",a[i]);
		}
		printf("\n");
	}
	//Sleep(1000);
	return 0;
}