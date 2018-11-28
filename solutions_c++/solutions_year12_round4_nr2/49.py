#include<cstdio>
#include<iostream>
using namespace std;
const int N=10000+100;
int n,w,l;
int r[N],mark[N];
int x[N],y[N];
int Min(int a, int b){return a<b?a:b;}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int Test;
	cin>>Test;
	for (int test=1;test<=Test;test++){
		cin>>n>>w>>l;
		for (int i=0;i<n;i++){
			cin>>r[i];
			mark[i]=1;
		}
		int change=0;
		if (w>l){
			int tmp=w;w=l;l=tmp;
			change=1;
		}
		int last=-1,pos=0;
		for (int i=0;i<n;i++){
			int j=-1;
			for (int k=0;k<n;k++)
				if (mark[k] && (j==-1 || r[j]<r[k]))
					j=k;
			if (last==-1){
				x[j]=0;
				y[j]=0;
				pos=r[j];
			}else if (x[last]+r[last]+r[j]<=w){
				x[j]=x[last]+r[last]+r[j];
				y[j]=y[last];
			}else{
				x[j]=0;
				y[j]=pos+r[j];
				pos=y[j]+r[j];
			}
			last=j;
			mark[j]=0;
		}
		printf("Case #%d:", test);
		if (change)
			for (int i=0;i<n;i++)
				printf(" %d.0 %d.0",y[i],x[i]);
		else
			for (int i=0;i<n;i++)
				printf(" %d.0 %d.0",x[i],y[i]);
		printf("\n");
		if (y[last]>l)
			printf("error!\n");
	}
	return 0;
}
