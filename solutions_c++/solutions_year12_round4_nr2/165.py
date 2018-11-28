#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<set>
using namespace std;

int n,w,l;
int r[2100];
int v[2100];
int x[2100],y[2100];

bool cmp(const int&a,const int&b){
	return r[a]>r[b];
}

int main(){
	int h,i,j,k,t;
	int la,lb;
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%d",&n);
		scanf("%d%d",&w,&l);
		for(i=0;i<n;i++)
			scanf("%d",&r[i]);
		for(i=0;i<n;i++)
			v[i]=i;
		sort(v,v+n,cmp);
		la=lb=-1;j=0;
		for(i=0;i<n;i++){
			if(i==0){
				x[v[i]]=y[v[i]]=0;
			}else{
				if(x[v[i-1]]+r[v[i-1]]+r[v[i]]<=w){
					x[v[i]]=x[v[i-1]]+r[v[i-1]]+r[v[i]];
					if(y[v[i-1]]==0)y[v[i]]=0;
					else{
						while(j<lb && x[v[i]]-x[v[j]]>=r[v[i]]+r[v[j]]){
							j++;
						}
						y[v[i]]=y[v[j]]+r[v[j]]+r[v[i]];
					}
				}else{
					la=lb+1;
					lb=i-1;
					j=la;
					while(y[v[j]]+r[v[j]]+r[v[i]]>l)j++;
					x[v[i]]=x[v[j]]-r[v[j]]+r[v[i]];
					if(x[v[i]]<0)x[v[i]]=0;
					y[v[i]]=y[v[j]]+r[v[j]]+r[v[i]];
				}
			}
		}
		for(i=0;i<n;i++){
			if(x[i]<0 || x[i]>w || y[i]<0 || y[i]>l)while(1);
			for(j=i+1;j<n;j++){
				if(abs(x[j]-x[i])<r[j]+r[i] && abs(y[j]-y[i])<r[j]+r[i])while(1);
			}
		}
		printf("Case #%d:",h);
		for(i=0;i<n;i++)
			printf(" %d %d",x[i],y[i]);
		printf("\n");
	}
	return 0;
}