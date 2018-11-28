#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

const int maxn=20000;

int n,v;
struct node{
	int a0,a1;
}f[maxn];
struct node2{
	int g,c;
}a[maxn];

void init(){
	memset(f,0,sizeof(f));
	memset(a,0,sizeof(a));
	scanf("%d%d",&n,&v);
	for (int i=1;i<=(n-1)/2;i++) scanf("%d%d",&a[i].g,&a[i].c);
	for (int i=(n-1)/2+1;i<=n;i++) scanf("%d",&a[i].g);
}

int min(int x,int y){
	if (x==-1) return y;
	else if (y==-1) return x;
	return (x<y?x:y);
}

int calc(int k,int v){
	f[k].a0=f[k].a1=-1;
	if (k>(n-1)/2){
		if (a[k].g==1) f[k].a1=0;
		else f[k].a0=0;
	}
	else{
		calc(k*2,0);
		calc(k*2+1,0);
		if (a[k].c==0){
			if (a[k].g==0){
				if (f[k*2].a1!=-1) f[k].a1=f[k*2].a1;
				if (f[k*2+1].a1!=-1) f[k].a1=min(f[k].a1,f[k*2+1].a1);
				if (f[k*2].a0!=-1&&f[k*2+1].a0!=-1) f[k].a0=f[k*2].a0+f[k*2+1].a0;
			}
			else{
				if (f[k*2].a0!=-1) f[k].a0=f[k*2].a0;
				if (f[k*2+1].a0!=-1) f[k].a0=min(f[k].a0,f[k*2+1].a0);
				if (f[k*2].a1!=-1&&f[k*2+1].a1!=-1) f[k].a1=f[k*2].a1+f[k*2+1].a1;
			}
		}
		else{
			if (a[k].g==0){
				if (f[k*2].a1!=-1) f[k].a1=f[k*2].a1;
				if (f[k*2+1].a1!=-1) f[k].a1=min(f[k].a1,f[k*2+1].a1);
				if (f[k*2].a0!=-1&&f[k*2+1].a0!=-1) f[k].a0=f[k*2].a0+f[k*2+1].a0;

				if (f[k*2].a0!=-1) f[k].a0=min(f[k].a0,f[k*2].a0+1);
				if (f[k*2+1].a0!=-1) f[k].a0=min(f[k].a0,f[k*2+1].a0+1);
				if (f[k*2].a1!=-1&&f[k*2+1].a1!=-1) f[k].a1=min(f[k].a1,f[k*2].a1+f[k*2+1].a1+1);
			}
			else{
				if (f[k*2].a0!=-1) f[k].a0=f[k*2].a0;
				if (f[k*2+1].a0!=-1) f[k].a0=min(f[k].a0,f[k*2+1].a0);
				if (f[k*2].a1!=-1&&f[k*2+1].a1!=-1) f[k].a1=f[k*2].a1+f[k*2+1].a1;

				if (f[k*2].a1!=-1) f[k].a1=min(f[k].a1,f[k*2].a1+1);
				if (f[k*2+1].a1!=-1) f[k].a1=min(f[k].a1,f[k*2+1].a1+1);
				if (f[k*2].a0!=-1&&f[k*2+1].a0!=-1) f[k].a0=min(f[k].a0,f[k*2].a0+f[k*2+1].a0+1);
			}
		}
	}

	if (v==0) return f[k].a0;
	else return f[k].a1;
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int Q,num=0;
	scanf("%d",&Q);
	while (Q--){
		num++;
		init();
		int ans=calc(1,v);
		if (ans!=-1)
			printf("Case #%d: %d\n",num,ans);
		else printf("Case #%d: IMPOSSIBLE\n",num);
	}

	return 0;
}