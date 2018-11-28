#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
struct node{
	char s[3];
	int t;
}A[105];
bool a[103],b[103],tmp[103];
int ABS(int a){
	if(a<0)a=-a;
	return a;
}
void Q(bool *x,int t,bool *y,int &ans){
	int dd=103;
	int c;
	for(int i=1;i<=100;i++){
		if(x[i]&&ABS(i-t)<dd){
			dd=ABS(i-t);
			c=i;
		}
	}
	ans=ans+dd+1;
	for(int i=1;i<=100;i++)x[i]=false;
	x[t]=true;
	for(int i=1;i<=100;i++)tmp[i]=y[i];
	for(int i=1;i<=100;i++)y[i]=false;
	for(int i=1;i<=100;i++){
		if(tmp[i]){
			int s=i-dd-1;
			int e=i+dd+1;
			if(s<1)s=1;
			if(e>100)e=100;
			for(int j=s;j<=e;j++)y[j]=true;
		}
	}
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int th=1;th<=cas;th++){
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf("%s%d",&A[i].s,&A[i].t);
		}
		for(int i=1;i<=100;i++){
			a[i]=false;
			b[i]=false;
		}
		a[1]=true;
		b[1]=true;
		int ans=0;
		for(int i=0;i<n;i++){
			if(A[i].s[0]=='O')Q(a,A[i].t,b,ans);
			else Q(b,A[i].t,a,ans);
		}
		printf("Case #%d: %d\n",th,ans);
	}
	return 0;
}