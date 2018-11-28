#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<windows.h>
using namespace std;

int t,n;
int a[1100],b[1100],c[1100],d[1100],u[1100];

bool cmp1(const int&x,const int&y){
	return b[x]<b[y];
}

int main(){
	int h,i,j,k,l,x,y;
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%d%d",&a[i],&b[i]);
			d[i]=c[i]=i;
			u[i]=0;
		}
		sort(d,d+n,cmp1);
		j=0;
		k=0;
		l=0;
		for(i=0;i<n;i++){
			while(j<b[d[i]]){
				y=-1;
				for(x=0;x<n;x++){
					if(j>=a[x] && u[x]==0){
						if(y==-1 || b[y]<b[x])y=x;
					}
				}
				if(y!=-1){
					u[y]=1;
					j++;
					l++;
				}else break;
			}
			if(j>=b[d[i]]){
				if(u[d[i]]==1)j++;
				else j+=2;
				u[d[i]]=1;
				l++;
			}else{
				break;
			}
		}
		printf("Case #%d: ",h);
		if(i<n)printf("Too Bad\n");
		else printf("%d\n",l);
	}
	//Sleep(1000);
	return 0;
}