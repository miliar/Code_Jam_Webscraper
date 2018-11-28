#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>

#define maxn 1111111
#define maxC 1000000000

using namespace std;

int test,n,m,s,r,nheap;
double tt,res;
int cover[5*maxn];
int a[maxn];
int heap[maxn];
int pos[maxn];
bool use[maxn];

void up(int u,int v,int l,int r,int node,int num){
	int mid;
	if ((v<l)||(u>r)) return;
	if ((u<=l)&&(r<=v)){
		cover[node]=cover[node]+num;
		return;
	}
	mid=(l+r)/2;
	cover[2*node]=cover[2*node]+cover[node];
	cover[2*node+1]=cover[2*node+1]+cover[node];
	cover[node]=0;
	up(u,v,l,mid,2*node,num);
	up(u,v,mid+1,r,2*node+1,num);
}

int get(int i,int l,int r,int node,int add){
	int mid,x,y;
	if ((i<l)||(i>r)) return 0;
	if (l==r) return add+cover[node];
	mid=(l+r)/2;
	x=get(i,l,mid,2*node,add+cover[node]);
	y=get(i,mid+1,r,2*node+1,add+cover[node]);
	return x+y;
}

void input(){
	int i,j,u,v,w;
	cin>>n>>s>>r>>tt>>m;
	memset(cover,0,sizeof(cover));
	up(1,n,1,n,1,s);
	for (i=1;i<=m;i++){
		cin>>u>>v>>w;
		up(u+1,v,1,n,1,w);
	}
	for (i=1;i<=n;i++) a[i]=get(i,1,n,1,0);
}

void up(int node){
	int c;
	if (node==1) return;
	c=node/2;
	if (a[heap[node]]<a[heap[c]]){
		swap(heap[node],heap[c]);
		up(c);
	}
}

void down(int node){
	int c;
	if (2*node>nheap) return;
	c=2*node;
	if ((c<nheap)&&(a[heap[c+1]]<a[heap[c]])) c++;
	if (a[heap[node]]<=a[heap[c]]) return;
	swap(heap[node],heap[c]);
	down(c);
}

void push(int v){
	nheap++;
	heap[nheap]=v;
	up(nheap);
}

int pop(int node){
	int v=heap[node];
	heap[node]=heap[nheap];
	nheap--;
	up(node);
	down(node);
	return v;
}

void process(){
	int i,v;
	double w,len;
	memset(use,false,sizeof(use));
	nheap=0;
	for (i=1;i<=n;i++) push(i);
	res=0;
	while ((tt>0)&&(nheap>0)){
		v=pop(1);
		use[v]=true;
		w=(double)(1)/double(a[v]-s+r);
		if (w>tt){
			len=tt*(a[v]-s+r);
			res=res+tt+((double)(1)-(double)(len))/double(a[v]);
			break;
		}else{
			res=res+w;
			tt=tt-w;
		}
	}
	for (i=1;i<=n;i++)
		if (!use[i])
			res=res+(double)(1)/(double)(a[i]);
}

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	scanf("%d",&test);
	int i;
	for (i=1;i<=test;i++){
		input();
		process();
		printf("Case #%d: %0.6lf\n",i,res);
	}
}
